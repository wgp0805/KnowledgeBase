---
title: "摘要-matt-openspec配合开发教程"
type: source
tags: [AI编程, OpenSpec, MattPocock, 工作流, 配合开发, Java后端]
sources: [raw/01-articles/Matt-Pocock-Skills与OpenSpec配合开发完整教程.md]
last_updated: 2026-09-05
---

## 核心摘要

本文是关于 Matt Pocock Skills 与 OpenSpec 配合开发的完整教程，回答了三个核心问题：1) 使用 Matt Skills 开发功能的完整流程（7 步）；2) Matt 的规划能力与 OpenSpec 的对比分析（互补而非替代）；3) OpenSpec 中如何穿插 Matt Skills 的详细流程整理（三种配合方式）。核心结论是 OpenSpec 作为规划引擎，Matt Skills 作为执行纪律箱，两者组合使用可覆盖从需求探索到代码归档的全流程。

## 关键信息

### Matt Skills 开发流程（7 步）
1. 需求澄清：`/grill-with-docs` 盘问对齐
2. 领域建模：`/domain-model` 梳理概念（可选）
3. 写规格：`/to-spec` 产出技术方案
4. 人工审查：你的绝对主动权
5. 实现：`/tdd` + `/implement` 先写测试再实现
6. 代码审查：`/code-review` 两轴审查
7. 修复 + 提交

### Matt vs OpenSpec 规划能力对比
- **OpenSpec**：强规划（四阶段命令 + 四份 DAG 工件 + Delta Spec）
- **Matt Skills**：弱规划（只有需求澄清和领域建模）
- **结论**：互补而非替代，OpenSpec 管规划，Matt 管执行纪律

### OpenSpec + Matt Skills 配合方式
- **方式一**：执行前约定（推荐）——在 `/opsx:apply` 前约定 TDD 纪律
- **方式二**：手动叫停——随时打断切换到 `/tdd`
- **方式三**：跳过 apply——直接用 `/tdd` 逐项实现

### 核心穿插点
- `/opsx:explore` 可穿插 `/grill-with-docs` 盘问对齐
- `/opsx:apply` 可穿插 `/tdd` 强制 TDD 纪律
- 实现后必须穿插 `/code-review` 代码审查
- 跑不起来时穿插 `/diagnosing-bugs` 系统化调试

## 关联连接
- [[OpenSpec]] — 规划引擎
- [[MattPocock]] — 执行纪律箱作者
- [[mattpocock-skills]] — 执行纪律箱仓库
- [[GrillMe]] — 需求澄清 skill
- [[TDD]] — 测试驱动开发
- [[code-review]] — 代码审查
- [[diagnosing-bugs]] — 系统化调试
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] — 框架全景对比
- [[openspec-matt-skills-execution-workflow]] — OpenSpec + Matt 配合执行详解
- [[optimal-framework-combination-heavy-project]] — 重型项目最优组合
