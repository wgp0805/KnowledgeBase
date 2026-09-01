---
title: "ReAct 会死循环吗？如何设计可靠的终止机制"
type: source
tags: ["ReAct", "AI-Agent", "面试题"]
sources: ["raw/01-articles/ReAct 会死循环吗？如何设计可靠的终止机制？.md"]
last_updated: 2026-09-01
---

# ReAct 会死循环吗？如何设计可靠的终止机制

面试题讲解 ReAct 死循环问题：Agent 陷入 Thought-Action-Observation 无限循环。沉默王二分析死循环成因（工具返回不变、目标不明确、上下文污染），给出终止机制设计——最大迭代数、重复检测、目标完成判断、Harness 兜底。

## 关联连接
[[ReAct]], [[HarnessEngineering]], [[沉默王二]]
