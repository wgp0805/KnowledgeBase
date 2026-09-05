---
title: "role-isolation"
type: concept
tags: [AI, Agent, 架构设计, 多Agent协作]
sources: [raw/09-archive/multi-agent-collaboration.md]
last_updated: 2026-08-06
---

## 定义

角色隔离是一种通过**工具白名单 + 硬约束**来强制区分 AI Agent 职责边界的机制，防止 Agent 在协作中越界执行不属于自己的任务。核心原则是"不靠自觉，靠物理闸门"。

## 关键信息

### 三层隔离手段

| 角色 | 隔离方式 | 具体做法 |
|------|----------|----------|
| Planner | 不给执行工具 | `tools` 不含 Bash，物理上不能跑代码 |
| Coder | 文件清单约束 | 只改 `spec.md` "文件清单"内列出的文件 |
| Reviewer | 给验证工具但不给修改工具 | 有 Bash（独立重跑），无 Edit（不能改代码） |

### 工具白名单设计原则

- 各角色 `tools` 精确到能/不能，宁可少给
- 工具白名单写错，整道隔离就形同虚设
- 最常见的错误：Reviewer 不给 Bash，导致它只能采信 Coder 的自证

### 硬约束编写要点

- 每条可验证（"不写实现逻辑"优于"保持克制"）
- 写死"不能做什么"，越界即违规
- Agent 天然倾向"帮人把事做完"，硬约束是对抗这种倾向的防线

## 关联连接

- [[multi-agent-collaboration]] — 框架中的角色隔离实现
- [[subagent-driven-development]] — 子代理上下文隔离机制
- [[adversarial-review]] — 对抗性评审（隔离的验证环节）
- [[摘要-多Agent协作开发框架]] — 来源