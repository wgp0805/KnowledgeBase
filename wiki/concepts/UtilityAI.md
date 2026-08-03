---
title: "UtilityAI"
type: concept
tags: [概念, 规划, Agent]
sources:
  - raw/01-articles/2026-08-01-Spring之父再次出山，开发了新的AI框架！ - 苏三说技术.md
last_updated: 2026-08-03
---

## 定义
Utility AI（效用 AI）是一种 Agent 决策模式：每个 Action 由可配置的效用函数打分，每一步执行得分最高的 Action。与 GOAP 相比，它不做全局路径规划，而是基于当前状态做即时最优选择。

## 关键信息
- **Embabel 中的定位**：作为 GOAP 之外的第二种规划模式
- **典型场景**：在 Stashbot（RAG 文档助手）中，Utility AI 模式让 LLM 自主决定何时以及如何搜索文档
- **特点**：打分逻辑灵活可配置，适合决策与全局顺序关系较弱的场景

## 关联连接
- [[Embabel]] — 采用框架
- [[GOAP]] — 并列的规划模式
- [[Agent]] — 所属概念
- [[摘要-embabel]] — 来源
