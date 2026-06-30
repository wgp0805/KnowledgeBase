---
title: "Agent工作流编排"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md]
last_updated: 2026-06-30
---

## 定义
Agent 工作流编排是把多个 AI 智能体的决策、工具调用、状态传递、条件分支、循环和人工介入组织成可执行流程的方法论。

## 关键信息
- 轻量 AI 应用通常只需要一次模型调用、RAG 或单 Agent 工具调用；复杂业务则需要显式编排。
- 图式编排用节点表示智能体行为，用边表示执行顺序和条件路由，用状态对象作为共享上下文。
- 状态管理能避免多节点之间直接耦合，使下游节点通过共享状态读取上游结果。
- 条件分支和循环让 Agent 流程可以根据执行结果动态选择下一步，而不是固定链式调用。
- Checkpointing 能让长流程在崩溃后从最近成功节点恢复，避免全链路重跑。
- 常见协作模式包括 Supervisor Pattern、Fan-out 和 Human-in-the-Loop。

## 关联连接
- [[摘要-langchain4j-langgraph4j-comparison]] — 来源
- [[LangGraph4j]] — Java 图式 Agent 编排框架
- [[LangChain4j]] — 常与编排层组合的能力接入框架
- [[Agent]] — 被编排的执行单元
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[dynamic-workflow]] — Claude Code 中代码即编排的相邻范式
