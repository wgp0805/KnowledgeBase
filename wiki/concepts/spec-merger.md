---
title: "spec-merger"
type: concept
tags: [概念, OpenSpec, spec-superflow]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-08-03
---

## 定义
spec-merger 是 spec-superflow 八状态机的 archiving（归档）阶段组件，负责把已实现的 delta spec 智能合并回主规范，防止规范腐烂。

## 关键信息
- **所属状态机**：`workflow-start → need-explorer → spec-writer → contract-builder → DP-3 → build-executor → bug-investigator → release-archivist → spec-merger`
- **作用**：将 delta spec 合并回主 spec，让主规范保持最新，避免代码与规范脱节（规范腐烂）
- **前提**：改动必须走了 delta spec 流程，spec-merger 才有可合并的增量
- **关联机制**：基于 [[delta-spec]]（ADDED/MODIFIED/REMOVED）增量变更

## 关联连接
- [[eight-state-machine]] — 所属状态机
- [[SpecSuperflow]] — 所属框架
- [[delta-spec]] — 合并的输入
- [[openspec-archive-modify-and-token-tradeoff]] — 规范腐烂分析
