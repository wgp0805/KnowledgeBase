---
title: "StateGraph"
type: concept
tags: [LangGraph, 状态图, 工作流编排, Agent]
sources: [raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md]
last_updated: 2026-07-06
---

## 定义
LangGraph 的核心图编排抽象，一种带状态的有向图执行引擎。开发者通过定义 State（状态类型）、Node（节点逻辑）和 Edge（执行边）来构建 Agent 工作流，框架自动管理状态传播和节点调度。

## 关键信息
- **State**：TypedDict 定义的状态类型，核心字段 `messages: Annotated[list[BaseMessage], add_messages]`（消息链）和 `tool_call_count: int`（安全计数器）
- **Node**：一个处理函数，接收 state 返回 state 更新，如 `agent_node` 和 `tool_executor_node`
- **Edge**：有向边连接节点，支持条件边（`add_conditional_edges`）根据 state 内容路由
- **Reducer**：`add_messages` 是消息累加器，新消息追加而非覆盖 — 没有它 ReAct 循环会断
- 最小 ReAct Agent 只需 2 个 Node + 1 条条件边

### 典型结构
```
START → agent_node → conditional_edge ─→ tools_node → agent_node ...
                                         └→ END
```

### 与 Graph/StateMachine 的区别
- StateGraph 是专为 LLM Agent 设计的，state 天然包含消息链
- Edge 条件由 LLM 输出（`tool_calls`）驱动，而非硬编码规则
- 支持 `recursion_limit` 防止无限递归

## 关联连接
- [[LangGraph]] — 所属框架
- [[ReAct_Agent]] — StateGraph 的典型应用模式
- [[LangGraph4j]] — Java 移植版中 StateGraph 的原型
- [[Agent工作流编排]] — 所属方法论
- [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]] — 来源

