---
title: "ChatMemory"
type: concept
tags: [AI, 对话记忆, 上下文]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md, raw/01-articles/Spring AI 2.0真香！.md, "raw/09-archive/2026-10-23-Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP.md"]
last_updated: 2026-10-26
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

## 关联连接
- [[LangChain4j]] — ChatMemory 框架
- [[RAG]] — 检索增强（长期知识）
- [[CLAUDEmd]] — 长期指令记忆
- [[ContextManagement]] — 上下文管理策略
- [[AdvisorChain]] — Advisor 链模式
- [[摘要-spring-ai-2-agent-tips]] — 来源
- [[摘要-spring-ai-2-对话记忆实战]] — Spring AI 2.0 对话记忆实战
- [[摘要-spring-ai-alibaba-文生图文生音向量化]] — 来源（SAA starter-memory-redis 侧实践）
