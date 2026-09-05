---
title: "AgentEval"
type: concept
tags: [概念, AI工程, SDLC, 评测, CI]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
Agent Eval 是 [[AINativeSDLC]] 中 CI 持续评测的实践：把 20-50 个真实任务写成 eval 套件，在 CI 中持续运行；每个生产事故变成 eval 永久留在套件里。这保证 Agent 能力不退化，且事故教训被固化。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[CI-CD]] — 持续集成
- [[EvaluationAsPRD]] — 评测即需求
