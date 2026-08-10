---
title: "摘要-一线大厂Git规范"
type: source
tags: [Git, 分支模型, 提交规范, Code Review, 团队协作]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 核心摘要
本文系统梳理一线互联网大厂的 Git 工程规范，涵盖四大板块：分支模型（Git Flow / GitHub Flow / Trunk-Based 三种主流模型的对比与混合实践）、分支命名规范（`<类型>/<内容>`，可关联工单号与版本号）、Commit Message 规范（Conventional Commits 约定式提交）、代码审查（分支保护 + PR 模板 + CI 门禁）与自动化工具链（Commitlint + Husky + Pre-commit + CI 质量门禁）。文章强调"规范的本质是省事不是管人"，需用工具强制落地而非靠自觉。

## 关联连接
- [[Git]] — 本文核心实体
- [[GitFlow]] — 经典企业级分支模型
- [[ConventionalCommits]] — 约定式提交规范
- [[语义化版本]] — 版本号管理规范
- [[code-review]] — 代码审查实践
- [[Commitlint]] — 提交信息校验工具
- [[Husky]] — Git 钩子工具
- [[CI-CD]] — 自动化流水线
- [[GitHub]] — GitHub Flow 来源
- [[苏三]] — 作者