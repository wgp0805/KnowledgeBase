---
title: "Commitlint"
type: entity
tags: [Git, 工具, 提交规范, lint]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Commitlint 是校验 Commit Message 是否符合规范的文件信息检查工具，配合 [[Husky]] 在 git commit 时自动拦截不合规的提交，是大厂"用工具强制落地规范"的核心手段。

## 关键信息
- 常用规则配置：`@commitlint/config-conventional`（Conventional Commits 规范预设）
- 常见规则：`type-enum`（提交类型枚举）、`subject-max-length`（subject 最大长度 50）、`body-max-line-length`（正文行最大长度 72）
- 工作原理：在 `.husky/commit-msg` 钩子中执行 `npx --no -- commitlint --edit $1`，不符合规范直接拒绝提交
- 与 [[Husky]] 配合是前端工程化标配

## 关联连接
- [[ConventionalCommits]] — 校验的规范标准
- [[Husky]] — 执行 commitlint 的 Git 钩子
- [[Git]] — 所属环境
- [[CI-CD]] — 更大范围的质量门禁
- [[摘要-一线大厂Git规范]] — 来源