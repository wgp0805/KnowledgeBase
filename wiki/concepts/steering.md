---
title: "steering"
type: concept
tags: [AI Agent, 人机交互, 控制机制, Codex]
sources: [raw/09-archive/如何把Codex用到极致.md]
last_updated: 2026-06-02
---

## 定义
Steering（转向）是 AI Agent 运行过程中，用户可随时打断并纠正方向的控制机制，让 Agent 不必从头开始即可调整执行策略。

## 关键信息
- 任务跑到一半时，用户可打断 Agent 立刻纠偏
- 与传统"停止→重新写 prompt"不同，steering 是增量修正
- 与 [[queuing]] 互补：steering 是即时干预，queuing 是不打断当前任务排入下一步
- 核心哲学：人没有被踢出回路，Agent 不是替你拍板，而是把决策点提前暴露

## 关联连接
- [[摘要-把Codex用到极致]] — 来源
- [[Codex]] — 所属产品
- [[queuing]] — 互补的控制机制
