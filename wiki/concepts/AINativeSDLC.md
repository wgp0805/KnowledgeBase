---
title: "AINativeSDLC"
type: concept
tags: [概念, SDLC, AI工程, Anthropic, 工程实践]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
AI 原生软件开发生命周期（AI-Native SDLC）是 Anthropic 提出的工程框架，核心论点是：当 AI 接管编码后，瓶颈从"构建"转移到流程左右两侧（规划、审查/测试、部署），传统线性 SDLC 不再适用。AI 原生 SDLC 把线性流程改造成循环，AI 嵌入每个节点，并以"提交的产物（committed artifact）"作为阶段间衔接的契约——每个阶段结束往版本控制写一个产物，下一阶段从读取该产物开始。

## 核心机制
- **committed artifact 链**：intent.md（意图）→ spec.md（需求设计）→ plan.md（实施计划）→ 代码 diff + 测试 → PR + REVIEW.md → 事故记录。commit 链即审计链。
- **六阶段 Play**：规划 / 设计 / 构建 / 测试 / 部署 / 运维，每阶段都有 AI 嵌入点。
- **反馈回路**：始终给 Claude 验证工作的方式；修 bug 先写失败测试；修代码的 agent 不能同时削弱对那段代码的检查。
- **闭合循环**：确定性脚本监控生产，控制带突破时调用 Claude；bands.yaml 定义 1σ/2σ/3σ 响应分级。

## 关键转变
- 瓶颈从构建转移到规划/审查/部署
- 逐行审查跟不上 agent 产出速度
- 治理成本上升，需要新的管控手段

## 关联连接
- [[SDLC]] — 传统软件开发生命周期，AI 原生 SDLC 的演进基础
- [[Anthropic]] — 框架提出方
- [[ClaudeCode]] — 框架核心工具
- [[IntentMd]] — 意图产物
- [[SpecMd]] — 需求设计产物
- [[PlanMd]] — 实施计划产物
- [[ReviewMd]] — 审查指令产物
- [[PlanMode]] — 计划模式，工程师默认起点
- [[CLAUDEmd]] — 机构知识文件
- [[AgentSkills]] — 机构知识可执行化
- [[Hooks]] — 确定性护栏
- [[Subagent]] — 子 Agent，并行会话
- [[AgentEval]] — CI 持续 Eval
- [[ClaudeTag]] — 闭合循环的频道成员
- [[Bands]] — 监控响应分级
- [[LouisClaxton]] — 原文作者
