---
title: "context-compression"
type: concept
tags: [AI, Agent, 上下文, 优化]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
上下文压缩（Context Compression）是指自动压缩 LLM 上下文窗口的技术，通过阈值控制（threshold）、目标压缩比（target_ratio）、保护最近消息数（protect_last_n）等参数，在保留关键信息的同时减少 Token 消耗。

## 关键信息
- **核心参数**：threshold（触发压缩的上下文长度）、target_ratio（目标压缩比例）、protect_last_n（保护最近的 N 条消息）
- **适用场景**：长对话、连续任务执行的上下文管理
- **实现方式**：可通过摘要总结、丢弃低优先级内容等方式实现

## 关联连接
- [[HermesAgent]] — 内置上下文压缩的 Agent 系统
- [[ContextManagement]] — AI 上下文窗口管理策略
- [[摘要-hermes-agent-complete-guide]] — 来源
