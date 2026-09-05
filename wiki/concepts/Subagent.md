---
title: "Subagent"
type: concept
tags: [概念, AI工程, ClaudeCode, 多智能体]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md, raw/01-articles/2026-08-26-Claude Code 与 Grok Bot 被拆开后：AI Agent 真正难复制的是什么？.md]
last_updated: 2026-08-27
---

## 定义
Subagent（子 Agent）是 [[ClaudeCode]] 的并行执行单元。在 [[AINativeSDLC]] 中，并行会话用各自 git worktree 隔离，子 agent 定义在 .claude/agents/，拥有独立上下文和工具权限。子 Agent 让复杂任务可分解、可并行，是 [[TaskDelegationSystem]] 中"控制能力"的体现。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[ClaudeCode]] — 所属工具
- [[TaskDelegationSystem]] — 任务托付能力
- [[子Agent编排]] — 相关概念
- [[subagent-driven-development]] — 相关实践
- [[Worktree]] — 并行会话的隔离手段
