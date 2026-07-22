---
title: "guardrails"
type: concept
tags: [AI, Agent, 安全, 架构]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
安全护栏（Guardrails）是 AI Agent 系统的安全防护体系，确保 Agent 在授权范围内安全运行，防止越权操作、数据泄露和意外行为。

## 关键信息
- **乐观执行机制**：主智能体正常运行，护栏并行实时检测
- **七大分类**：输入过滤、输出审核、权限控制、速率限制、操作确认、审计日志、降级处理
- **人工干预兜底**：HITL（Human-in-the-Loop），关键决策点暂停等待人工审批
- **实现方式**：可以通过 Hooks 拦截、Middleware 中间件、独立 Guardrail Agent 等方式实现

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[HITL]] — 人工干预兜底机制
- [[Hooks]] — 场景化防护机制
- [[摘要-agent-engineering]] — 来源
