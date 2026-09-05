---
title: "AgentHarness"
type: concept
tags: [AI, Agent设计, Harness, MiMo Code]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md, raw/09-archive/Trellis使用手册.md, raw/01-articles/从 vibe coding 到 spec coding：我一年多使用AI开发的实践总结.md, raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md]
last_updated: 2026-08-18
---

## 定义
Harness 是大模型之外让 Agent 表现更好的设计总称，包括上下文管理、工具调度、记忆机制、权限控制、流程编排等。同样一个大模型，harness 不同，效果差别非常大。

## 关键信息
- Claude Code 的 harness 被认为是业界标杆
- Harness 核心组件：LLM Loop、工具系统、记忆系统、权限模式、上下文压缩
- 好的 harness 让 Agent 在有限空间内最小化修改，出现错误时能及时回滚
- harness 工程是 Agent 产品差异化的关键因素

### 各框架的 Harness 实现
- **Solon AI**：`solon-ai-harness` 模块提供 Harness 马具框架，智能体脚手架能力
- **AgentScope-Java**：HarnessAgent 提供 Middleware + Toolkit 两个扩展通道，集成工作区、记忆、沙箱、子 Agent、技能与计划模式
- **AgentScope-Java 特色**：Middleware 五层钩子（onAgent/onReasoning/onActing/onModelCall）、沙箱执行（本地/Docker/E2B 一行切换、快照恢复）、自学习闭环
- **[[MiMoCode]]**：Harness 围绕计算、记忆、进化三个主题设计
  - **计算**：[[max-mode]]（并行候选评估）、[[goals]]（目标验证器）、[[dynamic-workflow]]（代码化流程编排）
  - **记忆**：[[checkpoint-rebuild]]（上下文窗口管理）和四层记忆体系（Session/Project/Global/History）
  - **进化**：通过 dream/distill 实现自我进化
- **[[Trellis]]**：将 Harness 外延到项目资产，借助 Spec、Task、Workflow 与 Journal 解决跨会话恢复、跨平台共享和经验回流；详见 [[项目级AI工作流]]。
- **[[DeepSeekHarness]]**：DeepSeek 官方 2026-08-13 开源（MIT），TypeScript 实现，基于 Cordis 插件内核，"一切皆插件"设计。GitHub 史上涨星最快项目（42 小时约 10 万 Star）。不绑定 DeepSeek API，认 OpenAI 兼容端点，可接入本地 [[LlamaCpp]] / [[Ollama]] + 任意开源模型，是 [[本地Agent工作站]] 的框架支柱。

## 关联连接
- [[Agent]] — harness 所属概念
- [[ClaudeCode]] — harness 标杆产品
- [[MiMoCode]] — 计算/记忆/进化三主题 Harness
- [[max-mode]] — 并行候选评估
- [[goals]] — 目标验证器
- [[dynamic-workflow]] — 代码化编排
- [[checkpoint-rebuild]] — 上下文管理
- [[ContextManagement]] — harness 核心组件
- [[AgentScope_Java]] — HarnessAgent 实现
- [[SolonAI]] — solon-ai-harness 模块
- [[Trellis]] — 项目级工作流 Harness
- [[项目级AI工作流]] — Spec/Task/Journal 闭环
- [[摘要-mimo-code发布]] — MiMo Code Harness 来源
- [[摘要-trellis使用手册]] — Trellis 工作流来源
- [[摘要-人类智力基线与2张显卡]] — DSH 本地部署实战来源
- [[DeepSeekHarness]] — DeepSeek 官方开源 Harness
- [[本地Agent工作站]] — 完整本地方案
- [[LlamaCpp]] — 本地推理引擎
- [[Qwen3.8-27B]] — 本地部署配套模型
- [[RTX5090]] — 配套硬件
