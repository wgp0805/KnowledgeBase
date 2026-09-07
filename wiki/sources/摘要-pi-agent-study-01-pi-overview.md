---
title: "摘要-pi-agent-study-01-pi-overview"
type: source
tags: [来源, pi-agent, 学习笔记, Agent基座]
sources: [raw/01-articles/pi-agent-study-01-pi-overview.md]
last_updated: 2026-08-07
---

## 核心摘要

本篇是 Pi (pi.dev) 系统学习的第一课笔记，主要讲解 Pi 的定位、核心理念以及与其他 Agent 工具的对比。Pi 是 Earendil 公司出品的极简终端编程基座（minimal terminal coding harness），采用"小内核、强扩展"的设计哲学，通过 TypeScript Extensions、Skills、Packages 等多层扩展机制实现高度定制化。笔记还对比了 Prompt/Skill/Extension 三个扩展层级的本质差异，强调 Extension 是在代码层面修改基座行为，模型无法绕过。

## 关键知识点

1. **Pi 的定位**：不是成品 Agent，而是 Agent 基座（harness），核心极简，能力靠扩展
2. **设计哲学**：小内核，强扩展（minimal core, strong extension）
3. **三层扩展模型**：Prompt/配置 < Skill < Extension，深度逐级递增
4. **Skill vs Extension**：Skill 改模型行为（可能不遵守），Extension 改基座行为（100% 生效）
5. **与 Hermes 的共性**：都遵循 Agent Skills 标准，Skill 可跨平台迁移

## 关联连接
- [[Pi (coding harness)]] — 学习对象，Earendil 出品的终端编程 Agent 基座
- [[AgentHarness]] — Harness 概念，Pi 是典型的 Harness 设计
- [[Agent扩展层级]] — Prompt / Skill / Extension 三层扩展模型
- [[Agent]] — Agent 核心概念
- [[Hermes]] — 另一个 Agent 基座，与 Pi 设计理念相似
