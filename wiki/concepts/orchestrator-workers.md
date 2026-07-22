---
title: "orchestrator-workers"
type: concept
tags: [AI, Agent, 工作流, 编排]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
协调器-工作者工作流（Orchestrator-Workers）是 Anthropic 提出的五大 Agent 工作流之一，由一个中央 LLM 动态拆解任务并分配给多个工作者 LLM 执行。

## 关键信息
- **适用场景**：复杂任务无法预知子任务数量和类型
- **协调器角色**：分析任务、制定计划、分配子任务、汇总结果
- **工作者角色**：执行具体子任务
- **优点**：灵活应对动态任务拆分
- **代表框架**：LangGraph（StateGraph 管理状态和流程）

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[augmented-llm]] — 增强型 LLM
- [[LangGraph]] — 协调器-工作者模式的框架实现
- [[摘要-agent-engineering]] — 来源
