---
title: "ChatMemory"
type: concept
tags: [AI, 对话记忆, 上下文]
sources: [raw/09-archive/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/09-archive/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md, raw/09-archive/Spring AI 2.0真香！.md, "raw/09-archive/2026-10-23-Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP.md", "raw/09-archive/2026-11-22 - 夯爆了，Spring AI 2.1 正式发布 ！.md"]
last_updated: 2026-11-24
---

## 定义
让无状态的 LLM 拥有"上下文"的机制，通过维护历史消息并在每次调用时重新注入，实现多轮对话的连贯性。

## 关键信息

### LangChain4j 实现
- `@MemoryId` 区分不同用户/会话，每个 ID 对应独立记忆
- `MessageWindowChatMemory`：滑动窗口策略，按消息数裁剪
- `TokenWindowChatMemory`：按 token 预算裁剪，更精准
- `ChatMemoryStore` 接口支持持久化到 Redis/MySQL/自建数据库

### Spring AI 2.0 实现
- `MessageChatMemoryAdvisor` Advisor 自动读写会话历史，通过 `ChatMemory.CONVERSATION_ID` 参数区分用户
- `MessageWindowChatMemory` 滑动窗口策略，保留最近 N 条消息
- 无需手动维护
- Redis 对话记忆实战（Spring AI 2.0）：需 redis-stack（非普通 redis），用 RedisChatMemoryRepository + MessageWindowChatMemory（maxMessages 配置）；ChatMemory 的 add/get/clear 均绑定 conversationId，流式输出完成后通过 doOnComplete 保存助手回复
 `List<Message>`，Advisor 自动注入历史

### 记忆 vs 历史记录（关键区分）
LangChain4j 提供的是"记忆"而非"历史记录"。记忆会根据算法对历史进行改造——淘汰某些消息、总结多条消息、去除不重要的细节、注入额外信息等。这意味着 ChatMemory 不是简单的消息堆叠，而是智能的上下文管理。

### 与 Agent 记忆的关系
ChatMemory 是对话级短期记忆（一次会话内），CLAUDE.md/Auto Memory 是跨会话的长期记忆。

### Spring AI Alibaba Redis 持久化（starter-memory-redis，2026-10-23 NE_STOP 教程）
- 前提论断：LLM 本身无状态，服务重启记忆即丢，必须持久化；四种记忆类型——内存存储（开发测试）、持久化存储（生产数据库）、分布式存储（可扩展应用）、自定义存储（特定需求）
- 完整链路：依赖 `spring-ai-alibaba-starter-memory-redis` + jedis，`RedisChatMemoryRepository.builder().host(host).port(port).build()` 注册 Bean；`MessageWindowChatMemory.builder().chatMemoryRepository(redisChatMemoryRepository).maxMessages(10).build()` 经 `MessageChatMemoryAdvisor` 挂到 ChatClient 的 defaultAdvisors
- 会话隔离：调用时 `advisors(advisorSpec -> advisorSpec.param("conversationId", userId))` 以 userId 作会话 ID；deepseek-v3 与 qwen-max 两个 ChatClient（DashScopeChatModel 构建）可共用同一 Repository
- **版本边界（对本页上文"需 redis-stack"说法的更新）**：Redis Stack 只是官方扩展模块打包发行版；Redis 8.0 起模块已内置进原版 Redis、Redis Stack 独立包标记弃用，新项目直接用 Redis 8+（需 RediSearch 能力的对话记忆/向量场景同理）

### Spring AI 2.1 的替代：Session API（版本边界，来源：[[摘要-spring-ai-2-1发布]]）
[[SpringAI]] 2.1 起，`ChatMemory` 相关类**已标记废弃、计划 3.0.0 移除**，新项目应直接用 Session API。两者差别不只是改个名字：

- **存储模型**：ChatMemory 是"按会话 ID 存一串消息"；Session 是**只追加的事件日志**，可持久化（`JdbcSessionRepository` 支持 PG/MySQL/MariaDB/SQL Server/H2）
- **压缩方式**：Session 的历史压缩一定在**轮次边界**切，不会出现"有工具调用、没工具结果"的残缺状态；压缩不改原始日志，只追加边界标记
- **可回溯**：被压缩掉的内容仍在日志里，模型可通过内置 `conversation_search` 工具自己翻旧账（ChatMemory 截断即丢失）
- **无默认会话**：框架故意不提供默认会话（避免不同用户记录混在一起）；Advisor 本身不保存状态，因此多实例部署时任意实例都能接着处理同一会话
- 本页上文的 `MessageChatMemoryAdvisor` 等基于 ChatMemory 的用法，在 2.1 新项目中应迁移为 Session Advisor

## 关联连接
- [[LangChain4j]] — ChatMemory 框架
- [[RAG]] — 检索增强（长期知识）
- [[CLAUDEmd]] — 长期指令记忆
- [[ContextManagement]] — 上下文管理策略
- [[AdvisorChain]] — Advisor 链模式
- [[摘要-spring-ai-2-agent-tips]] — 来源
- [[摘要-spring-ai-2-对话记忆实战]] — Spring AI 2.0 对话记忆实战
- [[摘要-spring-ai-alibaba-文生图文生音向量化]] — 来源（SAA starter-memory-redis 侧实践）
- [[SpringAI]] — 所属框架（2.1 起用 Session API 取代本机制）
- [[摘要-spring-ai-2-1发布]] — 来源（Session API 取代 ChatMemory 的版本依据）
