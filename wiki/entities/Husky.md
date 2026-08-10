---
title: "Husky"
type: entity
tags: [Git, 工具, Git钩子, 工程化]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Husky 是 Git Hooks 管理工具，用于在 git 提交、推送等生命周期节点自动执行校验脚本（如 [[Commitlint]] 校验、pre-commit 代码检查），是"用工具强制落地 Git 规范"的关键基础设施。

## 关键信息
- 管理 `.husky/` 目录下的钩子脚本（commit-msg、pre-commit 等）
- **commit-msg 钩子**：配合 commitlint 校验提交信息格式，不符合拒绝提交
- **pre-commit 钩子**：提交前自动执行格式化（Prettier/Black）与静态检查（ESLint/Checkstyle/TypeScript）
- 命令示例：`.husky/commit-msg` 中写 `npx --no -- commitlint --edit $1`
- 与 Commitlint 配合调用是最典型的工程化组合

## 关联连接
- [[Git]] — Git 钩子机制
- [[Commitlint]] — commit-msg 钩子配合对象
- [[ConventionalCommits]] — 配合保证提交规范
- [[CI-CD]] — 与流水线门禁互补的本地防线
- [[摘要-一线大厂Git规范]] — 来源