---
title: "SpringAI_Alibaba"
type: entity
tags: [AI框架, 阿里, 多智能体, Java]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/09-archive/Spring AI 2.0 和 Spring AI Alibaba，哪个更好？.md, "raw/09-archive/2026-10-03 - Spring AI Alibaba已停更了，Java还有希望吗？.md", "raw/09-archive/2026-10-23-Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP.md"]
last_updated: 2026-10-26
---

## 定义
阿里推出的独立 AI 框架项目（GitHub: `alibaba/spring-ai-alibaba`），专攻多智能体系统和工作流编排，深度集成 Spring AI 生态，核心运行在 Graph Runtime 上。

## 关键信息
- GitHub Stars: 10k+ | 1.0 GA 于 2026-05-13 | 版本: 1.1.2.0（2026-02）
- 框架依赖: Spring Boot | Java 17+
- 模型支持: 通义为主（多模型）
- 与 Spring Cloud Alibaba 无关（后者是微服务中间件）

### 定位与 Graph 引擎
- 定位：企业级编排运行时，类比 LangGraph；Spring AI 类比 JDBC（接入 AI），Alibaba 类比 Spring Cloud（编排多个 AI）
- Graph 引擎：低级别工作流和多代理协调框架，多智能体协作（ReAct Agent、Supervisor）、20+ 种标准组件（条件分支/并行处理/异常捕获）、流程快照（故障恢复）、记忆持久化（跨会话）、人工干预节点
- 1.1.2.0 新增：Agent Skills 支持、多智能体并行执行（AllOf/AnyOf 聚合策略）、异步工具执行与 returnDirect 增强

### Agent 支持（完善）
- **单 Agent（ReactAgent）**：ReAct 范式，思考→行动→观察循环
- **多 Agent 工作流**：SequentialAgent（链式）、ParallelAgent（并行）、LlmRoutingAgent（LLM 路由分发）、LoopAgent（循环迭代）
- **Graph Core**：DAG 工作流 + 条件路由 + 状态管理 + PlantUML/Mermaid 可视化
- **A2A（Agent-to-Agent）**：通过 Nacos 实现分布式 Agent 间通信

### Skill 支持（原生）
通过 **SkillRegistry + SkillsAgentHook** 提供原生 Skill 支持，遵循 Agent Skills 规范：
- SkillRegistry：技能注册中心，管理所有 Skill 的元信息
- SkillsAgentHook：Agent 钩子，自动注入 `read_skill` 工具和技能列表到 System Prompt
- FileSystemSkillRegistry：从本地文件系统加载 Skill 目录
- 渐进式披露：先注入技能列表（name, description, skillPath），按需加载完整 SKILL.md

### RAG 支持
内置 RAG 支持，集成 DashScope 通义模型实现检索增强生成。

### Starter 生态与多模态接入（2026-10-23 NE_STOP 教程）
接入层实战侧补充（现页主体为 Graph 编排视角）：官方 starter 三件套——`spring-ai-alibaba-starter-dashscope`（模型接入）、`spring-ai-alibaba-starter-memory-redis`（对话记忆 Redis 持久化，配合 jedis 客户端）、`spring-ai-starter-vector-store-redis`（Redis 向量库）。多模型接入范式：`DashScopeChatModel.builder().dashScopeApi(DashScopeApi.builder().apiKey(apiKey).build()).defaultOptions(DashScopeChatOptions.builder().withModel("deepseek-v3" / "qwen-max").build())` 构建双 ChatModel Bean，各自包成 ChatClient（@Qualifier 区分），共享同一 RedisChatMemoryRepository。多模态：ImageModel 调 `wanx2.1-t2i-turbo` 文生图（DashScopeImageOptions）、SpeechSynthesisModel 调 `cosyvoice-v2`（音色 longyingcui）文生音、EmbeddingModel 调 `text-embedding-v3` 向量化——均为 Spring AI 标准接口 + DashScope 侧实现。工程结构：parent 工程 springAiAlibaba-workV1 多 module（saa08-persistent、saa11-Embed2vector），JDK 17，api-key 经 `${aliQwen-apikey}` 环境变量注入。

### 停更传闻核查（2026-10-03，苏三，详见 [[摘要-spring-ai-alibaba停更分析]]）
- **传闻为真的部分**：GitHub 10.8k Star，最后一个正式版 v1.1.2.2（2026-03-10）后半年无新版；期间仅有 v2.0.0-M1.1（2026-06-25，跟进 Spring AI 2.0）
- **另一半真相**：main 分支未停——v1.1.2.2 后累计 137 个提交（Graph 序列化修复、Admin 中文化、JUnit 5 迁移等，以养护为主无大功能主线）
- **"换心脏"证据**：v1.1.2.2 最大特性是引入 AgentScope Java 集成（`spring-ai-alibaba-starter-agentscope`，用 AgentScopeAgent 封装 ReActAgent 进 Graph 编排）；官方公告称 SAA（Graph 编排）与 AgentScope（Agentic）独立发展不替代，但节奏对比悬殊——AgentScope 四天一版 vs SAA 半年一版
- **选型结论**：进入"养护模式"，已用者不必恐慌性迁移，新项目需评估"半年一更"是否可接受；分层选型见 [[JavaAI三层台阶]]

## 知识冲突
- **编排层还是接入层？（2026-10-08 标注）**
  - 旧说法（[[AgentScope_Java]] 页面，2026-07）：「Spring AI Alibaba 偏重'AI 能力接入'（RAG、聊天机器人），AgentScope 偏重'Agent 工程化'」——即把 SAA 归入接入层
  - 新说法（[[摘要-spring-ai-alibaba停更分析]]，2026-10-03）：Java AI 分三层，**接入层是 Spring AI 2.0 / LangChain4j，SAA 在编排层**（Graph 工作流、条件路由、状态持久化），运行时层才是 AgentScope
  - 两种说法并列保留（**状态：⏳ 待查**，待后续来源裁决）；按 SAA 自身 Graph Runtime/工作流编排的核心特性，新说法（编排层）与本页"多智能体系统和工作流编排"的定义更一致

## 关联连接
- [[摘要-spring-ai-alibaba停更分析]] — 来源（停更传闻核查与三层选型）
- [[JavaAI三层台阶]] — 该文提出的选型框架
- [[AgentScope_Java]] — 兄弟框架（含不同的分层表述）
- [[SpringAI]] — 兼容的 Spring AI 生态
- [[DashScope]] — 底层模型 API
- [[ReAct_Agent]] — Agent 模式
- [[A2A]] — Agent 间通信协议
- [[Skill_Registry]] — 技能注册中心
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-spring-ai-2-vs-alibaba选型]] — Spring AI 2.0 vs Alibaba 选型
- [[LangGraph]] — 类比框架
- [[spring-ai-vs-langchain4j]] — 相关框架对比
- [[摘要-spring-ai-alibaba-文生图文生音向量化]] — 来源（Starter 生态与多模态接入教程）
