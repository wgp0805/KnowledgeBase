---
title: "重型项目两大痛点：变更影响分析与新需求规划的工具组合"
type: synthesis
tags: [CodeGraph, GSDCore, 变更影响分析, 需求规划, 重型项目, 棕地项目, 选型]
sources:
  - wiki/entities/CodeGraph.md
  - wiki/entities/GSDCore.md
  - wiki/sources/摘要-codegraph-deep-dive.md
  - wiki/sources/摘要-gsd-core-ai工作流.md
  - wiki/syntheses/project-analysis-planning-tool-selection.md
last_updated: 2026-08-28
---

# 重型项目两大痛点：变更影响分析与新需求规划的工具组合

> **核心问题**：项目很重，自己知道功能都是干什么的，但有两个痛点：① 改了代码后发现影响其他代码，之前写的都要重构；② 新需求过来不知道该怎么做。应该使用什么框架或工具？

## 一、痛点拆解与工具对应

| 痛点 | 本质 | 工具 | 核心能力 |
|------|------|------|---------|
| 改了代码发现影响其他代码 → 要重构 | 缺乏**事前变更影响分析** | [[CodeGraph]] | `codegraph impact` 变更影响分析 |
| 新需求过来不知道怎么做 | 缺乏**需求到方案的引导流程** | [[GSDCore]] | `/gsd-discuss-phase` → `/gsd-plan-phase` |

## 二、痛点一：变更影响分析 — CodeGraph

根据 [[CodeGraph]] 和 [[摘要-codegraph-deep-dive]]，CodeGraph 用 tree-sitter 解析代码构建知识图谱（函数/类/方法为节点，调用/继承/引用为边，存入本地 SQLite+FTS5），让 AI 直接查图分析影响范围。

### 核心命令

```bash
codegraph impact <符号名> --depth 2    # 变更影响分析——改这个会影响哪些，深度2层
codegraph callers <函数名>             # 谁调用了这个函数——改签名前先看谁在用
codegraph callees <函数名>             # 这个函数调用了谁
codegraph trace <符号A> <符号B>        # 追踪两个符号间完整调用路径
codegraph affected                     # 受改动影响的测试文件
```

### 为什么能解决"改完才发现要重构"

**在改之前**就知道影响面。`codegraph impact` 基于代码知识图谱分析出完整影响范围，而不是改完才发现。通过 MCP 接入 Claude Code 后，AI 可以直接查图分析影响，不用反复 grep/Read。

### 性能数据

根据 [[摘要-codegraph-deep-dive]]，官方测试（7 个真实代码库）：工具调用减少 71%，Token 消耗降低 57%，任务速度提升 46%。

### 适合重型项目的点

- 纯本地运行，代码不上传
- 自动增量同步，`codegraph sync` 更新索引
- 支持 Java（tree-sitter 多语言解析）
- MCP 接入 Claude Code/Cursor/Codex

## 三、痛点二：新需求规划 — GSD Core

根据 [[GSDCore]] 和 [[摘要-gsd-core-ai工作流]]，GSD Core 的核心定位是"给 AI 编码助手加上项目管理大脑"，引导 AI 先理解项目、再拆解阶段、按计划执行。

### 核心工作流

```
/gsd-map-codebase     # 分析现有代码库结构
/gsd-new-project      # 建立项目上下文
/gsd-discuss-phase 1  # 需求讨论，理清边界
/gsd-plan-phase 1     # 生成执行计划
/gsd-execute-phase 1  # 执行
/gsd-verify-work 1    # 验证
```

### 为什么能解决"新需求不知道怎么做"

新需求来时，`/gsd-discuss-phase` 帮你理清需求边界，`/gsd-plan-phase` 基于对项目的理解生成执行计划。AI 围绕项目上下文持续工作，而不是"想到哪改到哪"。

### 适合个人使用的点

- 轻量：`npx @opengsd/gsd-core@latest`，有 `--minimal` 模式
- 支持 Claude Code、Codex、Cursor 等多平台

## 四、两个工具的配合工作流

```
新需求来了
    │
    ├─ /gsd-map-codebase          # GSD Core：AI 理解项目结构
    │
    ├─ /gsd-discuss-phase 1       # GSD Core：讨论需求，理清边界
    │
    ├─ codegraph impact <符号>    # CodeGraph：分析改动影响面（防遗漏核心）
    │                              # 在动手前就知道会影响哪些代码
    │
    ├─ /gsd-plan-phase 1          # GSD Core：基于影响面生成考虑全面的方案
    │
    ├─ /gsd-execute-phase 1       # GSD Core：执行
    │
    └─ /gsd-verify-work 1         # GSD Core：验证
```

**CodeGraph 解决"改了才发现要重构"**（事前影响分析），**GSD Core 解决"新需求不知道怎么做"**（需求到方案的引导流程）。两个都通过 MCP 接入 Claude Code，都支持 Java，都纯本地运行适合重型项目。

## 五、本质认知

这两个痛点的根源是同一个：**项目太重，人脑无法同时持有所有代码的依赖关系**。

- 痛点一（改完才发现要重构）= 人脑无法穷举变更影响面 → 需要 CodeGraph 的图谱分析
- 痛点二（新需求不知道怎么做）= 人脑无法同时考虑所有约束和可能性 → 需要 GSD Core 的结构化引导

**规划框架（OpenSpec/SpecSuperflow）解决的是"怎么记录和执行方案"，而这两个工具解决的是"怎么发现和制定方案"**——后者才是你的痛点。

## 六、与已有 synthesis 的关系

- [[project-analysis-planning-tool-selection]] — 结合项目分析的工具选型（GSD Core 为首选）
- [[openspec-brownfield-usage-guide]] — OpenSpec 棕地项目使用方案
- [[openspec-team-sync-personal-use]] — OpenSpec 个人使用同步策略

本页聚焦"**变更影响分析 + 新需求规划**"两大具体痛点的工具组合，补充了 CodeGraph 这个在之前选型中未充分覆盖的代码理解工具。

## 关联连接

- [[CodeGraph]] - 痛点一工具：变更影响分析
- [[GSDCore]] - 痛点二工具：新需求规划
- [[摘要-codegraph-deep-dive]] - CodeGraph 深度解析来源
- [[摘要-gsd-core-ai工作流]] - GSD Core 工作流来源
- [[project-analysis-planning-tool-selection]] - 配套：结合项目分析的工具选型
- [[TreeSitter]] - CodeGraph 底层 AST 解析引擎
- [[MCP]] - 两个工具的接入协议
- [[ClaudeCode]] - 承载平台
- [[规范驱动开发]] - 上层方法论
