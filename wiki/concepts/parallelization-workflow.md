---
title: "parallelization-workflow"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
并行化工作流（Parallelization）是 Anthropic 提出的五大 Agent 工作流之一，含分段并行与投票并行两种形态，多个 LLM 同时执行后聚合结果。

## 关键信息
- **分段并行**：将一个任务分拆为多个子任务并行处理
- **投票并行**：多个 LLM 使用相同 Prompt 独立推导后投票选出最佳结果
- **适用场景**：子任务互相独立、需要多角度验证的场景
- **优点**：提速显著、结果更可靠

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[augmented-llm]] — 增强型 LLM
- [[摘要-agent-engineering]] — 来源
