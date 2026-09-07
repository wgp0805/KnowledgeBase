---
title: "HarnessEngineering"
type: entity
tags: [Agent, Harness, 工程架构]
sources: [raw/01-articles/2026-09-04-谷歌真的急了！Gemini 3.8 Flash 刚发布，Google Harness 就跟随其后.md]
last_updated: 2026-09-05
---

## 定义
Harness Engineering（驾驭工程）是确保 Agent 能持续、稳定、安全完成复杂任务的工程架构。模型决定 Agent 有多聪明，Harness 决定这份智能能不能稳定输出。

## 关键信息
- 典型 Harness 架构：Model → Context → Tools → Execution → State → Verification → Repair Loop
- 三大厂商路线差异：
  - OpenAI：从真实 Coding Agent 倒推 Harness
  - DeepSeek：把 Harness 本身做成产品（Everything is a Plugin）
  - Google：Model + Runtime + Workflow Engine + Enterprise Platform
- NVIDIA AVO 实验：Harness 对最终效果产生巨大影响，评估 Agent 不能只测底层模型
- 四件值得马上实践的事：权限边界代码化、测试融入 Workflow、设置预算与 Kill Switch、优化 Agent Legibility

## 关联连接
- [[AgentHarness]] — Agent 运行基础设施
- [[RepairLoop]] — 自动循环修复机制
- [[GraphWorkflow]] — 图工作流编排
- [[摘要-谷歌gemini38flash-harness-engineering]] — 来源
- [[OpenAI]] — OpenAI Harness 路线
- [[DeepSeek]] — DeepSeek Harness 路线
- [[GoogleADK]] — Google ADK 2.0
