---
title: "Worktree"
type: concept
tags: [Git, 隔离, Agent, 工作流, Codex]
sources: [raw/01-articles/3 分钟掌握 Codex 97% 的功能，超实用教程！.md]
last_updated: 2026-07-07
---

## 定义
Worktree（工作树隔离）是给 AI Agent 开一个隔离工作区的机制，Agent 可以在其中改代码、试功能、跑实验，但不直接污染主项目。做坏了直接丢掉，不用在主目录收拾残局。

## 关键信息
- 核心价值：多个需求并行时互不影响（一个分支做登录、一个做支付、一个修 bug）
- 选择标准：
  - **Local**：小修补（如改一句文案）
  - **Worktree**：重要构建、大范围改代码、多需求并行
  - **Cloud**：长时间运行的自动化任务
- 大部分情况下 Worktree 是最安全的选择

## 关联连接
- [[Codex]] — 核心使用工具
- [[Git]] — 底层版本控制机制
- [[摘要-codex-97percent-技巧]] — 来源
