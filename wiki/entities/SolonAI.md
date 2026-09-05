---
title: "SolonAI"
type: entity
tags: [AI框架, 轻量, Java, 全场景]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/2026-07-04-用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅.md]
last_updated: 2026-07-06
---

## 定义
全场景轻量级 Java AI 框架。无需框架容器，纯 JDK 即可运行，支持 Java 8 到 Java 26（极致兼容性），核心内存约 1MB。

## 关键信息
- GitHub Stars: 2,745 | AI 版本: v3.10.7
- GitHub: `opensolon/solon`
- 框架依赖: 无（纯 JDK）
- 模型支持: 5+

### Spring Boot → Solon 注解迁移
Solon 不是 Spring 的分支或封装，而是独立发展的全栈应用开发框架。在设计哲学上遵循 Java 主流的 IoC、AOP、MVC 范式——概念相同，注解名不同。对于正在做技术选型或迁移调研的 Java 开发者，如果会 Spring Boot，则已会了一大半 Solon。

### ChatModel — 统一 LLM 客户端
Solon 4.0 的 `ChatModel` 使用 Builder API 封装了与不同 LLM 交互的样板代码，核心特性：
- **同步调用**：`chatModel.prompt(question).call()` 三行业务代码完成
- **流式调用**：基于 Project Reactor 的 `Flux<ChatResponse>`，支持 SSE 端点
- **会话记忆**：`ChatSession` 自动维护对话历史，内置三种存储实现
- **多消息 Prompt**：`Prompt.of()` 组合多条消息构建复杂上下文
- **RAG 模式**：`ChatMessage.ofUserAugment()` 将参考上下文注入 Prompt
- **方言模式**：通过 `standard/provider` 字段自动适配不同服务商协议

### 方言支持（Dialect Pattern）
| 方言标识 | apiUrl 示例 | 模型 |
|----------|-------------|------|
| `openai`（默认） | `https://api.openai.com/v1/...` | GPT、DeepSeek、Qwen、GLM、Kimi |
| `ollama` | `http://127.0.0.1:11434/api/chat` | 本地 Ollama 模型 |
| `anthropic` | `https://api.anthropic.com/v1/messages` | Claude |
| `gemini` | `https://generativelanguage.googleapis.com/...` | Gemini |
| `dashscope` | 阿里云 DashScope 端点 | Qwen（DashScope 原生） |

### ChatSession 三种实现
- `InMemoryChatSession` — 本地 Map，适合开发与单节点
- `FileChatSession` — 文件系统，适合 CLI/桌面应用
- `RedisChatSession` — Redis 存储，适合生产分布式

### AI 模块体系
- `solon-ai` — LLM 基础（模型、Prompt、Tool、Skill、方言）
- `solon-ai-skills` — 技能开发（独立模块，v3.9.0+）
- `solon-ai-rag` — RAG 知识库
- `solon-ai-flow` — AI 工作流编排
- `solon-ai-agent` — Agent（SimpleAgent、ReActAgent、TeamAgent）
- `solon-ai-harness` — Harness 智能体马具框架
- `solon-ai-mcp` — MCP 协议

### Skill 支持（原生，功能最丰富）
Solon AI Skills 概念原型参考了 Claude Code Agent Skills 的设计思想。

核心特色：两种构建方式（声明式/编程式）、技能多态（同一接口不同实现）、动态 Prompt、SkillRegistry + 优先级排序、按需动态加载、分布式 Remote Skills、内置 20 个预置技能、生态兼容 Claude Skills。

Skill 类型体系：
- **CliSkill** — 对接海量 Claude Agent Skills 生态（兼容 agentskills.io）
- **RestApiSkill** — 对接海量 WebAPI
- **ToolGatewaySkill** — 对接 Tool（或 MCP 服务）
- **Text2SqlSkill** — 数据库自然语言查询
- **Remote Skill** — 分布式技能，跨服务调用

### Agent 支持
SimpleAgent（简单对话）、ReActAgent（推理+行动循环）、TeamAgent（多智能体团队协作），另有 Harness 马具框架提供脚手架能力。

## 关联连接
- [[ReAct_Agent]] — Agent 模式
- [[Skill_Registry]] — 技能注册中心
- [[AgentHarness]] — 马具框架
- [[MCP]] — 模型上下文协议
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[SpringBoot]] — 注解迁移对比基准
- [[IoC]] — 控制反转原则
- [[AOP]] — 面向切面编程
- [[SpringMVC]] — MVC 框架对比
- [[摘要-Spring-Boot-to-Solon-注解迁移]] — 来源
- [[摘要-solon-chatmodel-java-llm]] — 来源
- [[ChatSession]] — 对话记忆会话管理
- [[DialectPattern]] — 方言模式
