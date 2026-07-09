---
title: "SpecSuperflow"
type: entity
tags: [AI编程, 工作流, 规范驱动, Claude Code插件, 开源]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

SpecSuperflow 是一个开源的 Claude Code 插件（v0.3.0，MIT 协议，零外部依赖），由 [[MageByte-Zero]] 开发。它将 [[OpenSpec]]（规划引擎）与 [[Superpowers]]（执行纪律框架）融合为一个自动化工作流，用一张「执行契约」把规划与执行连起来，由状态机自动驱动流转，消除手动在两个框架间切换、归档、检查漂移的"人肉胶水"成本。

## 关键信息

- **GitHub**：https://github.com/MageByte-Zero/spec-superflow
- **版本**：v0.3.0（2026-07 起步阶段）
- **协议**：MIT，零外部依赖（纯 TypeScript 接口定义 + 正则工件解析，无 npm 包）
- **支持平台**：v0.2.0 起 7 个平台（Claude Code、Cursor、Copilot 等），核心逻辑为纯 Markdown 工件，任何支持文件读写的 AI 编码工具均可适配

### 整合策略：去重叠、留异同、加独创

1. **去重叠**：功能重复的合并——brainstorming 融入 spec-explorer；writing-plans 融入 spec-forger；executing-plans 并入 execution-governor；archive/finishing 并入 closure-archivist
2. **留异同**：各自独有全部保留——systematic-debugger（Superpowers 精华）、spec-syncer（[[delta-spec|OpenSpec delta 同步]]）、code-reviewer
3. **加独创**：新增三个组件——[[execution-contract|bridge-contract]]（解析引擎，自动提取执行契约）、workflow-orchestrator（内容级状态检测）、七状态机

### 七状态机

`exploring → specifying → bridging → approved → executing → debugging → closing`

每个状态对应一到两个 skill，workflow-orchestrator 为入口，说"开始"或"继续"即检测当前状态决定下一步。关键设计：检测文件**内容**而非文件**存在性**（避免 AI 生成空占位文件骗过状态机）。

### 安装

```
/plugin marketplace add MageByte-Zero/spec-superflow
/plugin install spec-superflow@spec-superflow
```

### 适用边界

- **适合**：大型功能开发、多人协作需统一规格、长期维护需可追溯变更、需严格 TDD 与 Review Gate、棕地项目精确增量描述
- **不适合**：快速原型、<100 行小改动、纯探索性开发、单纯 bug 修复、个人实验项目
- **经验法则**：不需要写 proposal 和 design doc 就能想清楚的事，spec-superflow 太重；ROI 在中大型变更上才体现

### 已验证案例

- add-dark-mode：Next.js 项目加暗色模式，七状态全流程，spec 漂移率低
- refactor-auth-boundary：单体认证逻辑抽模块，delta spec 描述变更，rewind trigger 中途触发一次人工评估

## 关联连接

- [[OpenSpec]] - 融合的规划层
- [[Superpowers]] - 融合的执行层
- [[execution-contract]] - 核心创新机制
- [[seven-state-machine]] - 工作流状态机
- [[delta-spec]] - 增量变更机制
- [[review-gate]] - 审查门禁
- [[subagent-driven-development]] - 子代理开发
- [[规范驱动开发]] - 上层方法论
- [[MageByte-Zero]] - 开发者
- [[ClaudeCode]] - 宿主工具
- [[摘要-spec-superflow-融合工作流]] - 来源
