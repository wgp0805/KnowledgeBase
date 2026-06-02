---
title: "goals"
type: concept
tags: [AI Agent, 任务管理, 验证, Codex]
sources: [raw/01-articles/如何把Codex用到极致.md]
last_updated: 2026-06-02
---

## 定义
Goals（目标）是 AI Agent 中带验证器的长跑型任务，Agent 持续向一个明确的、可验证的终点推进，而非一次性对话指令。

## 关键信息
- **弱目标**："按这个 Markdown 里的计划实现一下"（无验证器，只是愿望）
- **强目标**："把这个内部工具从 Python 迁到 Rust。目录要建好，功能要对齐，单元测试全部通过才算完成"（有验证器）
- 没有验证器的目标只是愿望。测试、benchmark、复现脚本、端到端流程把"继续努力"变成"有没有更接近完成"
- 不是任务越大越适合交给 Agent，而是越能被验证的任务，越适合让 Agent 长时间推进

## 关联连接
- [[摘要-把Codex用到极致]] — 来源
- [[Codex]] — 所属产品
- [[durable-threads]] — 长线程承载 goals 的持续上下文
- [[Automations]] — 定期执行的自动化任务
