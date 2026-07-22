---
title: "摘要-AgentScope入门指南"
type: source
tags: [来源, 原始文件, AI框架, Java, Agent, 初学者]
sources: [raw/01-articles/AgentScope入门指南.md]
last_updated: 2026-07-22
---

## 核心摘要
本文由苏三撰写，是一份面向 Java 开发者的 AgentScope-Java 入门实战指南。文章从"Java 开发者怎么做 AI Agent"的角度出发，系统介绍了 AgentScope-Java 2.0 的核心概念（ReActAgent、HarnessAgent）、@Tool 注解驱动的工具系统、基于文件驱动的子 Agent 机制、MCP 协议集成、分层架构原理，并提供了 Hello World、天气查询、旅行助手三个完整实战案例。文章强调 Java 开发者不需要为了 Agent 去学 Python，AgentScope 是专为 Java 生态设计的 Agent 框架。

## 关键提炼
- **ReActAgent** — 最轻量的推理核心，适合单次对话、无状态场景
- **HarnessAgent** — 生产级入口，封装工作区/记忆/会话/子Agent/沙箱/压缩
- **@Tool 注解** — 将任意 Java 方法注册为 Agent 可调用工具
- **子 Agent 文件驱动** — workspace/subagents/*.md 声明式定义，主 Agent 动态决定调用
- **MCP 集成** — tools.json 声明 MCP Server，Agent 启动时自动发现注册工具
- **orchestrator + workers** — 主 Agent 拆解委派，SubAgent 并行执行

## 关联连接
- [[苏三]] — 作者
- [[AgentScope_Java]] — 主角框架
- [[ReActAgent]] — 轻量推理 Agent
- [[HarnessAgent]] — 生产级工程 Agent
- [[Workspace]] — 文件驱动架构
- [[子Agent编排]] — 多 Agent 协作机制
- [[MCP]] — 模型上下文协议
- [[SpringAI_Alibaba]] — 对比框架
