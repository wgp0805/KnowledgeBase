---
title: "单Agent"
type: concept
tags: [概念, Agent, 架构]
sources: [raw/01-articles/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md]
last_updated: 2026-09-20
---

## 定义
单 Agent 架构是让一个 Agent 独立完成整个任务的模式，适合路径写不死、需要自主决策的任务。相比 Workflow（路径写死）更灵活，相比多 Agent 更简单。

## 关键信息
- **适用场景**：路径写不死、需要自主决策的任务
- **与 Workflow 区别**：路径写得死用 Workflow，写不死上单 Agent
- **与多 Agent 区别**：拆多 Agent 看能不能多出新信息，不能则保持单 Agent
- **优势**：简单、上下文统一、无协调开销
- **局限**：单点能力受限，复杂任务可能力不从心

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[Agent]] — 核心概念
- [[Workflow]] — 路径写死的模式
- [[多Agent]] — 拆分的模式
- [[多智能体编排]] — 相关概念