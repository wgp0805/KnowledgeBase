---
title: "GraphWorkflow"
type: concept
tags: [Agent, 工作流, 图编排]
sources: [raw/01-articles/2026-09-04-谷歌真的急了！Gemini 3.8 Flash 刚发布，Google Harness 就跟随其后.md]
last_updated: 2026-09-05
---

## 定义
Graph Workflow 是 Google ADK 2.0 引入的工作流编排模式，将 Agent、Tool 和普通函数统一为 Workflow Graph 中的节点，开发者可通过图结构定义分支、循环、重试、并行、状态恢复。

## 关键信息
- 相比旧模式（Sequential、Parallel、Loop）的改进：更灵活的图结构编排
- 核心思路：模型负责解决开放问题，Workflow 负责守住流程
- 企业 Agent 架构："确定性流程 + 非确定性 Agent"的结合
- Google ADK 2.0 的 Graph Workflow 本质上是给这两部分提供共同执行环境

## 关联连接
- [[GoogleADK]] — Google Agent 开发套件
- [[HarnessEngineering]] — Harness 工程
- [[Workflow]] — 工作流概念
- [[摘要-谷歌gemini38flash-harness-engineering]] — 来源
