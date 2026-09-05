---
title: "Loop Engineering 与 Harness 工程区别"
type: synthesis
tags: [AI, Agent, Loop, Harness, 工程化, 架构]
sources:
  - wiki/concepts/LoopEngineering.md
  - wiki/sources/摘要-loop-engineering-guide.md
  - wiki/concepts/Harness.md
  - wiki/concepts/AgentHarness.md
  - wiki/sources/摘要-deepseek-harness内测.md
last_updated: 2026-08-13
---

# Loop Engineering 与 Harness 工程区别

## 核心结论
两者不是并列，而是包含关系：**Loop ⊂ Harness**。核心公式 **Model + Harness = Agent**——Harness 是大模型之外让 Agent 表现更好的一切基础设施层，Loop 是 Harness 内部"流程编排 + 安全护栏"两块的工程方法论。

## 一句话分清
- **Harness 工程** = Agent 基础设施层总称，"大模型之外让 Agent 表现更好的一切"——工具调用、记忆、上下文控制、MCP、Skills、多 Agent 协作、流程编排、安全护栏（见 [[Harness]]、[[AgentHarness]]）。
- **Loop Engineering** = Harness 里"流程编排 + 安全护栏"两块的一个具体方法论——三文件驱动循环、三级模式、五大坑（见 [[LoopEngineering]]）。

## 三个本质区别

### 1. 范畴：窄 vs 宽
- Loop 很窄，只讲"循环怎么设计才不失控"。
- Harness 很宽，是"未来五年 AI 工程化的核心主题"，各大厂都在造（DeepSeek Harness、阿里 Qoder、Kimi Code、智谱 Zcode，[[ClaudeCode]] 是标杆）。

### 2. 抽象层级：运行流程 vs 系统架构
- Loop 在**运行流程层**——讲循环边界、刹车、状态落地。
- Harness 在**系统架构层**——讲整个 Agent runtime 的组件构成。[[ReAct_Agent]] 循环是 Harness 的核心模式之一，但 Harness 还要管上下文压缩、记忆衰减、工具并行、权限审批这些 Loop 不碰的东西。

### 3. 产物：方法论文件 vs 整个 Agent 产品
- Loop 产出是**三份 Markdown + 工程纪律**，自己跑不起来，寄生在 Claude Code / Codex 上。
- Harness 产出是**一个完整 Agent 产品**——Claude Code、[[DeepSeekHarness]]、[[PaiCLI]] 都是"Harness 实例"。wiki 直言："所有 Agent 本质上都是在做 Harness"。

## Harness 八大核心组件
1. 工具调用系统（注册表/Schema/HITL 审批）
2. 记忆管理（短期/长期/项目记忆）
3. 上下文控制（窗口/摘要/Token 预算）
4. MCP 协议
5. Skills 体系
6. 多 Agent 协作
7. 流程编排 ← Loop 专注
8. 安全护栏 ← Loop 专注

## Java 视角落地
Java 生态的 Harness 实现：
- [[SolonAI]] 的 `solon-ai-harness` 模块——把 Harness 写进名字
- [[AgentScope_Java]] 的 HarnessAgent——Middleware 五层钩子 + 沙箱执行 + 自学习闭环，较完整
- [[MiMoCode]]——围绕计算/记忆/进化三主题做 Harness

手搓 Agent 实际是在**造 Harness**（套住 LLM 的工程外壳）；Loop Engineering 教的是"这个 Harness 里的循环 + 护栏该怎么设计"。一个是造车，一个是这车怎么开才不撞墙。

## 关联连接
- [[LoopEngineering]] — 循环工程方法论
- [[摘要-loop-engineering-guide]] — 三文件体系来源
- [[Harness]] — 基础设施层定义
- [[AgentHarness]] — Harness 工程总称
- [[摘要-deepseek-harness内测]] — Harness 来源
- [[DeepSeekHarness]] — DeepSeek 原生 Harness
- [[ClaudeCode]] — Harness 标杆产品
- [[PaiCLI]] — 开源 Harness 实例
- [[ReAct_Agent]] — Harness 核心循环模式
- [[SolonAI]] — solon-ai-harness
- [[AgentScope_Java]] — HarnessAgent
- [[MiMoCode]] — 计算/记忆/进化 Harness
- [[agent-architecture-landscape]] — Agent 架构全景
- [[loop-vs-hermes]] — Loop 与 Hermes 区别
