---
title: "durable-threads"
type: concept
tags: [AI Agent, 上下文管理, 工作流, Codex]
sources: [raw/01-articles/如何把Codex用到极致.md]
last_updated: 2026-06-02
---

## 定义
持久化工作线程（Durable Threads），指 AI Agent 不再每次对话从零开始，而是拥有长期、连续的上下文环境，保留工作习惯、决策记录、半成品材料和项目状态。

## 关键信息
- 不同于简单的聊天记录保存，长线程能保留一整套工作习惯：哪些来源可信、哪些步骤要先跑、哪些人需要被提醒、哪些检查不能漏
- 可同时存在多个专用线程：发布线程、文档审查线程、外部监控线程、Chief of Staff 线程
- 短聊天里的 AI 像临时工，每次重新交代背景；长线程更像持续工作的项目房间
- 长线程 + Automation 形成工作闭环：线程定期醒来检查 Slack/Gmail/PR 评论等

## 关联连接
- [[摘要-把Codex用到极致]] — 来源
- [[Codex]] — 所属产品
- [[ContextManagement]] — 上下文管理策略
- [[AutoMemory]] — 自动记忆
- [[automations]] — 长线程与自动化形成闭环
