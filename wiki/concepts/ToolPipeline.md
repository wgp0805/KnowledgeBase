---
title: "ToolPipeline"
type: concept
tags: [AI, Agent, 工具编排, 批量执行]
sources: [raw/01-articles/2026-07-05-AI Agent 30天速成｜Day10 笔记 - 云淡风轻YangG.md]
last_updated: 2026-07-06
---

## 定义
工具流水线编排（Tool Pipeline）是一种批量工具执行模式，一次性定义串行/并行多工具步骤，由网关自动调度执行，替代传统 ReAct 多轮循环，大幅减少 Token 消耗。

## 关键信息

### 两种编排模式
- **串行流水线（依赖型）**：上一个工具输出作为下一个工具输入，顺序执行；示例：rag_search → calculator
- **并行流水线（无依赖）**：多个工具同时并发执行，结果统一汇总；示例：同时执行多条 rag_search

### 变量传递机制
流水线定义 output_var 变量键名，网关缓存每一步工具结果，后续步骤可通过 `${变量名}` 动态引用前序输出，无需模型重复拼接上下文。

### 与 ReAct 对比
- ReAct：单轮单工具、多轮 LLM 思考、Token 消耗大，适合无固定流程的开放式问题
- ToolPipeline：一次规划多工具批量执行、网关调度、Token 消耗低，适合流程固定、多依赖/多并行的标准化任务

## 关联连接
- [[ReAct_Agent]] — 传统 ReAct 模式对比
- [[Agent]] — 所属核心概念
- [[RAG]] — 检索增强生成
- [[摘要-ai-agent-day10-tool-pipeline]] — 来源
