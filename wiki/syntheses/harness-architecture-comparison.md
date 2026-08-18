---
title: "Harness 架构分类与 Agent 选型"
type: synthesis
tags: [AI, Agent, Harness, 架构, 选型, DeepSeek, MiMo, AgentScope, Trellis]
sources:
  - wiki/concepts/Harness.md
  - wiki/concepts/AgentHarness.md
  - wiki/concepts/HarnessAgent.md
  - wiki/concepts/BetterHarness.md
  - wiki/concepts/max-mode.md
  - wiki/concepts/dynamic-workflow.md
  - wiki/entities/DeepSeekHarness.md
  - wiki/entities/MiMoCode.md
  - wiki/syntheses/loop-vs-harness.md
  - wiki/sources/摘要-deepseek-harness内测.md
last_updated: 2026-08-18
---

# Harness 架构分类与 Agent 选型

## 核心定义

**Harness 是 AI Agent 中"大模型之外的一切基础设施层"**，核心公式为 **Model + Harness = Agent**：模型负责推理，Harness 负责把推理能力转化为可执行的工程化操作（见 [[Harness]]、[[AgentHarness]]）。

> 同一个大模型，harness 不同，效果差别非常大。Harness 工程是 Agent 产品差异化的关键因素，[[ClaudeCode]] 被认为是业界标杆。

## Harness 八大核心组件

依据 [[Harness]] 与 [[loop-vs-harness]]：

1. 工具调用系统（注册表 / Schema / HITL 审批）
2. 记忆管理（短期 / 长期 / 项目记忆）
3. 上下文控制（窗口 / 摘要压缩 / Token 预算）
4. MCP 协议（外部服务集成）
5. Skills 体系（可复用行为模块）
6. 多 Agent 协作（Sub-agent 编排、任务分解）
7. 流程编排 ← Loop Engineering 专注
8. 安全护栏 ← Loop Engineering 专注

## 主流 Harness 架构分类与区别

知识库中收录的 Harness 实现按设计哲学可分为四类：

### 1. 一切皆插件型 — [[DeepSeekHarness]]（DSH）
- **设计**：基于 Cordis 插件内核，工具/技能/MCP/记忆全部插件化，5 天社区插件超 1400+
- **特色**：不绑定 DeepSeek API，认 OpenAI 兼容端点，可接本地 [[Ollama]] / [[LlamaCpp]]
- **适合**：追求极致可扩展、想本地部署、想自定义插件的开发者；CI/CD 自动化（headless 模式）

### 2. 计算/记忆/进化三主题型 — [[MiMoCode]]
- **计算**：[[max-mode]]（并行 N 候选选最优，4-5× token 换 10-20% 可靠性提升）、[[goals]]（串行自我检查）、[[dynamic-workflow]]（代码即编排，图灵完备沙箱）
- **记忆**：[[checkpoint-rebuild]] + 四层记忆体系（Session/Project/Global/History）
- **进化**：dream/distill 自我进化机制
- **适合**：长任务、一步走错全盘皆输的高可靠性场景；程序员驱动、需要代码化编排的复杂工作流

### 3. 薄包装工程外壳型 — [[HarnessAgent]]（AgentScope Java 2.0）
- **设计**：不重写 ReAct 循环，只在 [[ReActAgent]] 外包一层"壳"，用 Builder 串起工作区/记忆/沙箱/子 Agent/Plan Mode
- **特色**：Middleware 五层钩子（onAgent/onReasoning/onActing/onModelCall）、沙箱一行切换（本地/Docker/E2B）、MCP 自动扫描注册
- **适合**：Java 企业级生产 Agent；需要长期运行、跨会话恢复、子 Agent 委派的业务场景

### 4. 项目级工作流外延型 — [[Trellis]]
- **设计**：把 Harness 外延到项目资产，借 Spec / Task / Workflow / Journal 解决跨会话恢复、跨平台共享、经验回流
- **适合**：跨会话、跨平台、需要经验沉淀回流的项目级 AI 开发工作流

## 容易混淆的"假 Harness"

[[BetterHarness]] 不是 Agent 产品，而是 [[PaiCLI]] 内置的**审计工具**——通过三个并行取证通道（会话证据/项目配置/Skill 配置）按五维度给 Agent 干活质量打分。与上述 Harness 是完全不同的概念。

## Loop 与 Harness 的关系

依据 [[loop-vs-harness]]：**Loop ⊂ Harness**，不是并列关系。
- **Harness** = 系统架构层，造整个 Agent runtime（造车）
- **Loop Engineering** = 运行流程层，讲循环边界、刹车、状态落地（这车怎么开才不撞墙），寄生在 Claude Code / Codex 等 Harness 实例上

## 选型速查

| 需求 | 推荐 |
|------|------|
| 极致插件扩展 / 本地部署 | [[DeepSeekHarness]] |
| 高可靠长任务 / 代码化编排 | [[MiMoCode]] |
| Java 企业级生产 / 子 Agent 编排 | [[HarnessAgent]]（AgentScope Java） |
| 跨会话项目级工作流 | [[Trellis]] |
| 评估 Agent 干活质量 | [[BetterHarness]]（审计工具，非 Agent） |

## 关联连接
- [[Harness]] — 基础设施层定义
- [[AgentHarness]] — Harness 工程总称
- [[DeepSeekHarness]] — 一切皆插件型代表
- [[MiMoCode]] — 计算/记忆/进化三主题型代表
- [[HarnessAgent]] — 薄包装工程外壳型代表
- [[Trellis]] — 项目级工作流外延型代表
- [[BetterHarness]] — 易混淆的审计工具
- [[max-mode]] — 并行候选评估机制
- [[dynamic-workflow]] — 代码化流程编排
- [[loop-vs-harness]] — Loop 与 Harness 包含关系
- [[ClaudeCode]] — Harness 业界标杆
- [[Codex]] — 同类 Harness 实例
- [[PaiCLI]] — 开源 Harness 实例
- [[ReActAgent]] — Harness 核心循环模式
- [[SolonAI]] — solon-ai-harness 模块
- [[AgentScope_Java]] — HarnessAgent 所属框架
- [[摘要-deepseek-harness内测]] — Harness 来源
- [[摘要-mimo-code发布]] — MiMo Code Harness 来源
- [[摘要-trellis使用手册]] — Trellis 工作流来源
- [[摘要-AgentScopeJava2.0发布]] — HarnessAgent 来源
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — BetterHarness 来源
