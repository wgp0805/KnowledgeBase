---
title: "LangGraph4j"
type: entity
tags: [Java, AI框架, Agent, 工作流编排]
sources: [raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md]
last_updated: 2026-06-30
---

## 定义
LangGraph4j 是 LangGraph 的 Java 移植版，是用于构建有状态、多智能体工作流的图式编排框架，负责解决复杂 Agent 流程“如何编排”的问题。

## 关键信息
- 核心定位是 Agent 工作流编排层，而不是模型调用层；模型调用通常依赖 [[LangChain4j]] 或 [[SpringAI]]。
- 核心抽象包括 `AgentState`、`StateGraph`、Node、Edge、Checkpoint。
- 支持条件分支、循环控制、并行节点、多智能体协作、子图嵌套和 Human-in-the-Loop。
- Checkpointing 能在每次状态更新后持久化状态和执行上下文，支持崩溃恢复和失败节点重试。
- 多智能体模式包括 Supervisor Pattern、Fan-out、人工介入审批等。
- 适合长流程审批、复杂多轮决策、跨来源验证、代码 Review 多智能体系统和需要断点恢复的长周期任务。
- 文章给出的版本状态为 1.7.10 / 1.8-beta（2026-01），版本相对较新，生态成熟度低于 LangChain4j。

## 关联连接
- [[摘要-langchain4j-langgraph4j-comparison]] — 来源
- [[LangChain4j]] — 常见组合使用的 AI 能力接入层
- [[Agent工作流编排]] — 所属方法论
- [[Agent]] — 被编排的智能体单元
- [[SpringAI]] — 可作为底层模型与工具接入框架
- [[multi-agent-collaboration]] — 多 Agent 协作模式
