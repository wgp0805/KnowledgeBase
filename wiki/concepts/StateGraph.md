---
title: "StateGraph"
type: concept
tags: [LangGraph, 状态图, Agent编排]
sources: [raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 定义
StateGraph 是 LangGraph 的核心抽象，基于状态图（State Machine）建模 Agent 工作流。每个节点代表一个处理单元（LLM 推理、工具执行等），边代表节点间的流转，条件边支持动态路由。

## 关键信息
- **核心组件**：Node（处理单元）、Edge（固定跳转）、Conditional Edge（动态路由）、State（全局状态定义）
- **ReAct Agent 最小构建**：2 个节点 + 1 条条件边
  - `agent` 节点：LLM 推理决策
  - `tools` 节点：工具执行
  - 条件边：检查 AIMessage 是否包含 `tool_calls`
- **状态定义**：使用 TypedDict 定义，包含 messages、tool_results、done 等字段
- **编译**：`graph.compile()` 生成可执行的 Runnable，支持 `invoke`、`stream`、`batch` 等调用方式

## 关联连接
- [[摘要-langchain-langgraph-llamaindex对比]] — 来源
- [[LangGraph]] — 所属框架
- [[检查点机制]] — 状态持久化配套
- [[ReAct_Agent]] — 典型应用模式
- [[Agent工作流编排]] — 所属方法论