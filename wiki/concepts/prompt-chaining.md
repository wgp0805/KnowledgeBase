---
title: "prompt-chaining"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
提示链（Prompt Chaining）是 Anthropic 提出的五大 Agent 工作流之一，将复杂任务拆分为固定串行步骤，每一步的 LLM 输出作为下一步的输入。

## 关键信息
- **适用场景**：任务可明确拆分为多个固定阶段
- **优点**：结构清晰、易于调试、每步可单独优化
- **缺点**：灵活性低、无法动态调整路径

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[augmented-llm]] — 增强型 LLM
- [[摘要-agent-engineering]] — 来源
