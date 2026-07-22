---
title: "task-delegation"
type: concept
tags: [AI, Agent, 编排, 多Agent]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
任务委派（Task Delegation）是 Agent 将子任务分配给其他 Agent 执行的机制，支持单任务委派和并行批量委派两种模式，子 Agent 的上下文可精细控制。

## 关键信息
- **单任务委派**：一个子任务分配给一个子 Agent
- **并行批量委派**：多个子任务同时分配给多个子 Agent
- **上下文控制**：可精确控制传递给子 Agent 的上下文信息
- **嵌套委派**：子 Agent 可继续向下委派

## 关联连接
- [[HermesAgent]] — 内置任务委派机制的 Agent
- [[kanban-swarm]] — 多 Agent 集群协作
- [[multi-agent-collaboration]] — 多 Agent 协作
- [[摘要-hermes-agent-complete-guide]] — 来源
