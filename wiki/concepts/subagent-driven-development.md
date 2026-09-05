---
title: "subagent-driven-development"
type: concept
tags: [AI编程, Agent架构, 多Agent协作]
sources:
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

Subagent-Driven Development（SDD，子代理驱动开发）是 [[Superpowers]] 的杀手级能力：每个任务分发给一个独立的子代理执行，上下文隔离、文件交接。子代理不会被其他任务上下文污染，完成后还有双裁决审查（既查 spec 合规性，又查代码质量）。

## 关键信息

- **上下文隔离**：每个子代理独立上下文，避免任务间污染
- **双裁决审查**：完成后同时检查 spec 合规性与代码质量
- **效果数据**（Superpowers v6.0 评测）：token 消耗砍约 50%，速度翻倍
- 在 [[SpecSuperflow]] 中，executing-plans 融入 execution-governor，执行与治理合一

## 关联连接

- [[Superpowers]] - 所属框架
- [[子Agent编排]] - 相关机制
- [[multi-agent-collaboration]] - 多 Agent 协作模式
- [[SpecSuperflow]] - 融合后体现
- [[摘要-spec-superflow-融合工作流]] - 来源
