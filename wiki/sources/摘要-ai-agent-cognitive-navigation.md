---
title: "摘要-ai-agent-cognitive-navigation"
type: source
tags: [AI, Agent, 可观测性, 诊断]
sources: [raw/01-articles/2026-07-17-当AI Agent开始"自己拿主意"，你怎么知道它没在犯错？.md]
last_updated: 2026-07-20
---

## 核心摘要
Agent 在生产环境的最大风险不是宕机而是"跑偏"——仍在运行但仍出错。本文提出认知导航（Cognitive Navigation）诊断框架：通过健康度公式 S = T - C - D（推进力 - 约束力 - 内部消耗）实时量化 Agent 状态，输出 CONTINUE/NARROW_SCOPE/RESET_CONTEXT/HALT 四种导航指令。在 Qoder CN 金融尽调场景中，合规质量从 0.24 提升至 0.86（+258%），Token 消耗降低 38%。

## 关联连接
- [[CognitiveNavigation]] — 核心概念
- [[Agent]] — 被诊断的目标
- [[Qoder]] — 应用平台
- [[WorkBuddy]] — 多 Agent 协作验证
