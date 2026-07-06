---
title: "react-vs-plan-execute"
type: synthesis
tags: [AI, Agent, ReAct, Plan-and-Execute, 工作流]
sources:
  - wiki/concepts/ReAct_Agent.md
  - wiki/concepts/Research-Plan-Execute-Review-Ship.md
  - wiki/concepts/Agent.md
  - wiki/concepts/AICoding.md
last_updated: 2026-07-06
---

# ReAct vs Plan-and-Execute 对比分析

## 核心区别

| 维度 | [[ReAct_Agent]] | [[Research-Plan-Execute-Review-Ship]] |
|------|----------------|--------------------------------------|
| **层级** | 微循环（Agent 内部） | 宏观工作流（跨 Agent 会话） |
| **本质** | LLM 自主的"思考→行动→观察"循环 | 人与 AI 协作的"研究→计划→执行→审查→交付"分阶段流程 |
| **决策者** | LLM 自主决定每一步 | 人在阶段间做检查点决策 |
| **Token 消耗** | 每步都要 LLM 思考，消耗大 | 分阶段隔离，避免上下文污染 |
| **上下文管理** | 所有步骤共享同一上下文窗口 | 每阶段新开会话，上下文干净 |
| **典型场景** | 一个 Agent 实时处理用户的复杂问题 | 整个开发任务从需求到交付的全流程 |
| **可校验性** | 最终结果可校验，中间过程难插手 | 每阶段有明确产出物，可逐段验收 |
| **风险控制** | 依赖模型自主判断，容易跑偏 | 人在回路中，跑偏范围有限 |

## 各自定位

### [[ReAct_Agent]] — Agent 的"发动机"
ReAct 是 Agent 内部的微循环——模型自己决定"下一步该思考还是该调工具"。它是 [[Agent]] 概念中 LLM Loop 机制的核心实现：
- 收到用户问题 → **思考**需要什么工具 → **行动**调用工具 → **观察**工具结果 → 循环直到完成
- 适合无固定流程的开放问题，模型自主探索
- 各框架实现：[[SolonAI]] 的 ReActAgent、[[SpringAI_Alibaba]] 的 ReactAgent、[[AgentScope_Java]] 的 HarnessAgent

### [[Research-Plan-Execute-Review-Ship]] — 项目的"分阶段流水线"
Plan-and-Execute 是人的工作流编排，把任务切为 5 个可校验阶段：
| 阶段 | 任务 | 人是否介入 |
|------|------|-----------|
| Research | 读项目、需求、相关代码 | 确认上下文完整 |
| Plan | 输出实现方案 | 确认方案可行 |
| Execute | 按方案写代码 | 不介入，让 AI 执行 |
| Review | 自审、测试、子 Agent 审查 | 审查评审报告 |
| Ship | 提交/PR/发布 | 最终决策 |

它本质是 [[VibeEngineering]] 在 Agent 上的工程化落地——拆阶段使用 Agent，而不是一上来就让它写代码。

## 互补关系

两者不是二选一，而是不同抽象层级上的互补：

> **Plan-and-Execute 的"执行阶段"内部，完全可以跑 ReAct 循环。**

- 宏观上：用 Plan-and-Execute 管理整个开发流程，人在关键节点把关
- 微观上：每个执行步骤内，Agent 用 ReAct 自主调工具、看结果、做决策

社区已验证的模式（来自 [[claude-code-best-practice]]）：
1. Plan 阶段产出 commit 到 Markdown 文档
2. 新开 Session 让 Agent 读 Markdown 执行
3. 执行阶段内部 Agent 自主 ReAct 循环处理具体问题
4. 完成后进入 Review 阶段

## 关联连接
- [[ReAct_Agent]] — ReAct 模式详解
- [[Research-Plan-Execute-Review-Ship]] — Plan-and-Execute 五阶段范式
- [[Agent]] — Agent 核心概念
- [[AICoding]] — AI 编程范式
- [[VibeEngineering]] — Vibe Engineering 理念
- [[claude-code-best-practice]] — 最佳实践仓库
- [[SolonAI]] — ReActAgent 实现框架
- [[SpringAI_Alibaba]] — ReactAgent 实现框架
- [[AgentScope_Java]] — HarnessAgent 实现框架
- [[摘要-claude-code-best-practice-苏三视角]] — Plan 与 Execute 分 Session 实践来源
