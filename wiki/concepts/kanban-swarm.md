---
title: "kanban-swarm"
type: concept
tags: [AI, Agent, 多Agent, 协作]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
Kanban Swarm 是 Hermes Agent 的多 Agent 集群协作模式，采用三层架构（Dispatcher → Orchestrator → Worker）和 9 种状态流转（backlog/ready/in_progress/blocked/review/done/archived/failed/cancelled），支持 6 种协作模式和 swarm 命令。

## 关键信息
- **三层架构**：Dispatcher（任务分发）、Orchestrator（任务编排）、Worker（任务执行）
- **9 种状态**：backlog → ready → in_progress → blocked/review → done → archived，以及 failed/cancelled 终止态
- **6 种协作模式**：
  - fan-out（扇出）：一拆多并行执行
  - fan-in（扇入）：多汇总为一
  - pipeline（流水线）：阶段式传递执行
  - human-in-the-loop（人工介入）：blocker 等待审批
  - stale-recovery（异常恢复）：超时任务自动恢复
  - atomic-claim（原子认领）：SQLite 原子 CAS 任务认领

## 关联连接
- [[HermesAgent]] — Kanban Swarm 的宿主系统
- [[task-delegation]] — 任务委派机制
- [[multi-agent-collaboration]] — 多 Agent 协作
- [[摘要-hermes-agent-complete-guide]] — 来源
