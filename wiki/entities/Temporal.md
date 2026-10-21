---
title: "Temporal"
type: entity
tags: [工具, 分布式, 工作流, 基础设施, 开源]
sources:
  - raw/01-articles/2026-10-21-斯坦福新课直接讲 personal agent，Grok Bot 工程师分享如何打造出 always-on agent.md
last_updated: 2026-10-21
---

## 定义

开源的分布式工作流编排引擎，提供 **durable workflow**（可持久化工作流）能力——执行状态持久化、任意步骤可安全重试、失败后能从中断点继续。

## 关键信息

### 在 always-on agent 架构中的角色
Lee Robinson 团队处理复杂任务（第一步、第二步、第三步，中间可能碰到基础设施故障）时用的就是 Temporal，**没有自己从头造这套复杂的东西**。

### 与普通任务队列（job queue）的区别
- **普通队列**：崩溃之后重启，要把一到三步**重放一遍**，这会出很多问题（重复的副作用、丢失的中间状态）
- **Durable workflow**：可以安全重试，失败之后**直接从第三步接着做**

### 为什么对 Agent 关键
Agent 要连续干几周甚至几个月，**可靠性不是锦上添花，而是前提**——每个子智能体本身也是一个 durable workflow，崩溃了、内存用爆了，重启后接着干，不丢进度。

## 关联连接

- [[DurableWorkflow]] — 提炼概念
- [[LeeRobinson]] — 使用者
- [[常驻智能体]] — 所属场景
- [[Subagent]] — 子智能体即 durable workflow
- [[摘要-always-on-agent-斯坦福分享]] — 来源
