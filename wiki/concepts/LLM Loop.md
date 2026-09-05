---
title: "LLM Loop"
type: concept
tags: [AI, Agent, 运行机制, Harness]
sources: [raw/01-articles/pi-study-02-architecture.md]
last_updated: 2026-08-09
---

## 定义

LLM Loop（大模型循环）是 AI Agent 的核心运行机制：大模型在一个循环中不断思考、调用工具、观察结果、再思考，直到任务完成。这是 Agent 与普通对话式 AI 的本质区别。

## 关键信息

### 基本循环

```
while 任务未完成:
    1. 将当前上下文发送给 LLM
    2. LLM 返回响应（文本回复 或 工具调用请求）
    3. 如果是工具调用 → 执行工具 → 将结果追加到上下文
    4. 如果是最终回答 → 结束循环
```

### 工程化挑战（Harness 的价值所在）

同样的模型，在不同 Harness 中表现差异巨大，核心就在于循环的工程化处理：

| 问题 | 解决方案 |
|------|---------|
| 上下文太长 | Compaction（上下文压缩） |
| 工具调用失败 | 错误回灌，让模型重试或修正 |
| 模型死循环 | 最大步数限制 + 干预钩子 |
| 用户打断 | 中断信号处理（AbortSignal） |
| 工具输出过大 | 输出截断 + 摘要 |
| 多工具并行 | 并行调度 + 结果合并 |
| 敏感操作 | 调用前权限检查/确认 |

### 参与 Loop 的各组件

- **LLM**：做决策（说什么、调什么工具）
- **工具系统**：执行工具调用，返回结果
- **Session 管理**：维护上下文历史
- **上下文压缩**：控制上下文长度在窗口内
- **事件系统**：在循环各节点触发钩子，供扩展介入

### 与 ReAct 模式的关系

LLM Loop 是 ReAct（Reasoning + Acting）模式的工程实现。ReAct 是论文里的方法论，LLM Loop 是实际代码里的 while 循环。

## 关联连接
- [[Agent]] — Agent 核心概念，LLM Loop 是其心脏
- [[AgentHarness]] — Harness 就是把 LLM Loop 工程化的全套设施
- [[Pi (coding harness)]] — Pi 是 LLM Loop 的一个具体实现
- [[ContextCompaction]] — 上下文压缩，Loop 的必要配套
- [[Agent扩展层级]] — 扩展通过事件钩子介入 LLM Loop
- [[摘要-pi-study-02-architecture]] — 来源：Pi 架构学习笔记
