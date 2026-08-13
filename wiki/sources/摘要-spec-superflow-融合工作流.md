---
title: "摘要-spec-superflow-融合工作流"
type: source
tags: [来源, AI编程, 规范驱动, 工作流]
sources:
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/09-archive/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
last_updated: 2026-07-14
---

## 核心摘要

程序员追风介绍了开源 Claude Code 插件 **spec-superflow**（GitHub: MageByte-Zero/spec-superflow，MIT，零依赖），它将 [[OpenSpec]]（60k+ Star 规划引擎）与 [[Superpowers]]（253k+ Star 执行纪律框架）**源码级融合**为一个自动化工作流。核心创新是 contract-builder 桥接层：从 OpenSpec 的四份规划工件（proposal/specs/design/tasks）自动提取六类约束（Intent Lock、Scope Fence、Non-Goals、Test Obligations、Review Gates、Rewind Triggers），形成一份 execution-contract.md，作为规划到实现的唯一交接层（Guarded Handoff），解决"规划与执行脱节"问题。整套流程由 [[eight-state-machine|八状态机]]（workflow-start 入口，内容级状态检测）驱动，9 个核心 Skill 各对应一个阶段，跨 17 个平台分发。热点：DP-3 人工审批是唯一一次人工介入点；spec-merger 负责 delta spec 合并防规范腐烂；hotfix（≤2 文件）和 tweak（≤4 文件纯配置）提供快速路径。

## 关联连接

- [[SpecSuperflow]] - 核心实体
- [[OpenSpec]] - 融合的规划层框架
- [[Superpowers]] - 融合的执行层框架
- [[execution-contract]] - 核心创新机制
- [[eight-state-machine]] - 工作流状态机
- [[DP-3]] - 人工审批检查点
- [[delta-spec]] - OpenSpec 增量变更机制
- [[review-gate]] - 审查门禁
- [[subagent-driven-development]] - 子代理驱动开发
- [[规范驱动开发]] - 上层方法论
- [[程序员追风]] - 文章作者
- [[MageByte-Zero]] - spec-superflow 开源者
- [[FissionAI]] - OpenSpec 开源方
- [[摘要-spec-superflow-融合工作流-源码级详解]] — 配套来源（源码级深度解读）
