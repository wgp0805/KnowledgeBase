---
title: "Harness²"
type: entity
tags: [实体, 开源框架, AgentHarness, Google]
sources: [raw/09-archive/2026-10-19-周一上线 DeepSeek 开始卷“许愿式编程”，Agent 手机来了，Character.AI 申请破产 - 小七-七牛开发者.md]
last_updated: 2026-10-20
---

## 定义
Harness² 是 Google Research 开源的递归优化 Agent Harness 框架：模型权重不变，围绕 Harness 的 8 类组件自动提出修改、试跑候选并比较执行差异，组合出新的 Harness。

## 关键信息
- **优化对象（8 类组件）**：系统提示词、记忆、Skill、子 Agent、工具指导、插件等
- **方法**：自动提出修改 → 试跑候选 Harness → 比较执行差异 → 组合出新 Harness；被采用的 Harness 与有证据支持的经验会保留下来用于后续任务（经验复利）
- **支持平台**：OpenCode、Codex；评测基准 JobBench、LAB、WorkBuddy-Bench
- **定位**：与"改模型"路线相对，走"不改模型、只改 Harness"的工程优化路线，是 [[HarnessEngineering]] 的自动化实践

## 关联连接
- [[摘要-周一上线-许愿式编程与agent手机]] — 来源
- [[AgentHarness]] — 优化对象概念
- [[HarnessEngineering]] — 所属工程范式
- [[Google]] — 研发方
