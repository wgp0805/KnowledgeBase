---
title: "evaluator-optimizer"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
评估器-优化器工作流（Evaluator-Optimizer）是 Anthropic 提出的五大 Agent 工作流之一，采用双 LLM 循环协作模式，一个负责生成输出，另一个负责评估和反馈，迭代优化结果。

## 关键信息
- **评估器角色**：检查生成结果的质量、给出改进建议
- **优化器角色**：根据反馈迭代改进输出
- **适用场景**：需要反复打磨的内容生成、代码审查、翻译等
- **优点**：产出质量高、可设置终止条件

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[augmented-llm]] — 增强型 LLM
- [[摘要-agent-engineering]] — 来源
