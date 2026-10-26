---
title: "CoT"
type: concept
tags: [概念, 提示工程, 推理, 思维链]
sources: [raw/09-archive/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md]
last_updated: 2026-09-20
---

## 定义
CoT（Chain of Thought，思维链）是让模型在回答前先展示中间推理步骤的提示技术，通过引导模型"想清楚再答"提升复杂推理任务的准确率。

## 关键信息
- **核心思想**：把隐式的推理过程显式化，让模型逐步推导而非直接给答案
- **与 ReAct 关系**：CoT 管"想"，ReAct 在 CoT 基础上加"做"（行动）
- **与 Plan-and-Execute 关系**：CoT 是单步推理，Plan-and-Execute 先想全局再执行
- **与 Self-Refine 关系**：CoT 是推理前引导，Self-Refine 是推理后审查
- **选型**：CoT 管想、ReAct 加做、Plan 先想全局、Refine 做完再审，生产环境混着用

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[ReAct]] — 加"做"的范式
- [[Plan-and-Execute]] — 先想全局的范式
- [[Self-Refine]] — 做完再审的范式
- [[Agent]] — 应用场景