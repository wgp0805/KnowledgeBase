---
title: "delta-spec"
type: concept
tags: [AI编程, 规范驱动, 增量变更]
sources:
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

Delta Spec 是 [[OpenSpec]] 的增量变更描述机制，用 ADDED/MODIFIED/REMOVED 三个标记描述变更差异，不动已有 spec，只描述差异。专为棕地项目设计--改一处不必重写整份 spec。

## 关键信息

- 三个标记：ADDED（新增）、MODIFIED（修改）、REMOVED（删除）
- 通过 `/opsx:sync` 将 delta spec 同步到主 spec
- 在棕地重构场景下极其好用：如"认证边界从 A 移到 B"只描述这个变更，不动原有 spec
- [[SpecSuperflow]] 的 spec-syncer 组件保留了这一机制

## 关联连接

- [[OpenSpec]] - 所属框架
- [[SpecSuperflow]] - 融合后保留该机制
- [[规范驱动开发]] - 上层方法论
- [[摘要-spec-superflow-融合工作流]] - 来源
