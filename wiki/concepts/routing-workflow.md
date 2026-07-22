---
title: "routing-workflow"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
路由工作流（Routing）是 Anthropic 提出的五大 Agent 工作流之一，对输入进行分类后分发至专属流程，实现任务的差异化处理。

## 关键信息
- **适用场景**：不同类型输入需要不同处理逻辑
- **优点**：分类清晰、各流程独立优化
- **常见实现**：先通过分类器（LLM 或传统分类模型）判断类型，再路由到对应 Handler

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[augmented-llm]] — 增强型 LLM
- [[摘要-agent-engineering]] — 来源
