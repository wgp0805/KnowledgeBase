---
title: "摘要-spec-superflow-融合工作流"
type: source
tags: [来源, AI编程, 规范驱动, 工作流]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 核心摘要

程序员追风介绍了开源 Claude Code 插件 **spec-superflow**（GitHub: MageByte-Zero/spec-superflow，v0.3.0，MIT，零依赖），它将 [[OpenSpec]]（5.7 万星规划引擎）与 [[Superpowers]]（24 万星执行纪律框架）融合为一个自动化工作流。核心创新是 [[execution-contract|执行契约]]（bridge-contract）：从 OpenSpec 的四个规划工件（proposal/specs/design/tasks）自动提取六类约束（Intent Lock、Scope Fence、Non-Goals、Test Obligations、Review Gates、Rewind Triggers），形成一份可验证的执行锚点，解决"规划与执行脱节"问题。整套流程由 [[seven-state-machine|七状态机]]（exploring→specifying→bridging→approved→executing→debugging→closing）驱动，采用内容级状态检测而非文件存在性检查。

## 关联连接

- [[SpecSuperflow]] - 核心实体
- [[OpenSpec]] - 融合的规划层框架
- [[Superpowers]] - 融合的执行层框架
- [[execution-contract]] - 核心创新机制
- [[seven-state-machine]] - 工作流状态机
- [[delta-spec]] - OpenSpec 增量变更机制
- [[review-gate]] - 审查门禁
- [[subagent-driven-development]] - 子代理驱动开发
- [[规范驱动开发]] - 上层方法论
- [[程序员追风]] - 文章作者
- [[MageByte-Zero]] - spec-superflow 开源者
- [[FissionAI]] - OpenSpec 开源方
