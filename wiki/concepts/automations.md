---
title: "automations"
type: concept
tags: [AI Agent, 自动化, 工作流, Codex]
sources: [raw/01-articles/如何把Codex用到极致.md]
last_updated: 2026-06-02
---

## 定义
Automations（自动化）指 AI Agent 按预定计划自动启动执行的工作流程，是 Agent 从被动响应走向主动运行的关键能力。

## 关键信息
- 典型场景：每日生成报告、定期检查 repo、定时唤醒线程检查 Slack/Gmail/PR 评论
- 与 [[durable-threads]] 结合形成工作闭环：线程持有关联连接醒来时自动检查新动态
- 与 [[Goals]] 的区别：automations 是定期执行的维护型任务，goals 是持续向特定目标推进的长跑任务

## 关联连接
- [[摘要-把Codex用到极致]] — 来源
- [[Codex]] — 所属产品
- [[durable-threads]] — 长线程与自动化形成闭环
- [[Goals]] — 互补的目标驱动模式
