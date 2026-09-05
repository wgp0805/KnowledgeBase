---
title: "摘要-构建你的第一个Tool-Agent-从零理解ReAct循环"
type: source
tags: [来源, LangGraph, ReAct, Agent]
sources: [raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md]
last_updated: 2026-07-06
---

## 核心摘要
LangGraph 系列教程第二篇，手写等价 ReAct 循环来揭示 `create_react_agent` 背后的封装原理。ReAct Agent 只需 **2 个节点（agent + tools）+ 1 条条件边** 即可构成完整循环：agent 节点负责推理决策，tools 节点负责执行工具，条件边检查最后一条消息是否有 `tool_calls` 来决定继续还是结束。文章强调 ToolMessage 必须写回 messages（否则 Agent "失忆"），以及业务层 `MAX_ITERATIONS` + 框架层 `recursion_limit` 双重安全阀防止无限循环。

## 关联连接
- [[LangGraph]] — 所属框架
- [[ReAct_Agent]] — ReAct Agent 核心概念
- [[StateGraph]] — LangGraph 状态图抽象
- [[FunctionCalling]] — 工具调用能力

