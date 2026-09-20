---
title: "Self-Refine"
type: concept
tags: [概念, 提示工程, 推理, 自我修正]
sources: [raw/01-articles/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md]
last_updated: 2026-09-20
---

## 定义
Self-Refine 是让模型在生成答案后自我审查、发现错误并修正的范式，通过"做完再审"提升输出质量。

## 关键信息
- **核心思想**：生成 → 自我评估 → 修正，形成反馈闭环
- **与 CoT 关系**：CoT 是推理前引导，Self-Refine 是推理后审查
- **与 ReAct 关系**：ReAct 在行动中反思，Self-Refine 在产出后审查
- **选型**：CoT 管想、ReAct 加做、Plan 先想全局、Refine 做完再审，生产环境混着用

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[CoT]] — 推理前引导
- [[ReAct]] — 行动中反思
- [[Plan-and-Execute]] — 先想全局
- [[Agent]] — 应用场景