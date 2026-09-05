---
title: "code-first-orchestration"
type: concept
tags: [概念, Agent, 编排]
sources:
  - raw/09-archive/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md
last_updated: 2026-08-03
---

## 定义
代码优先编排（Code-First Orchestration）是一种 Agent 编排方式：不依赖 DSL 或框架黑盒，而是通过常规编程代码（条件、循环、函数调用）显式控制 Agent 流程与分支。

## 关键信息
- **代表**：[[OpenAIAgentsSDK]] 采用代码优先编排，支持动态 Agent 流程
- **对比**：与声明式/图编排（如 [[LangGraph4j]] 的状态图）相对，代码优先更灵活但需要显式管理控制流
- **适用场景**：流程复杂、需要动态分支与细粒度控制的 Agent 应用

## 关联连接
- [[OpenAIAgentsSDK]] — 代表实现
- [[LangGraph4j]] — 图编排对比方案
- [[Agent工作流编排]] — 编排方法论
- [[multi-agent-collaboration]] — 多 Agent 协作模式
