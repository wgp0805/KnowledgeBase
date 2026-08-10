---
title: "GitHubFlow"
type: concept
tags: [Git, 分支模型, 敏捷开发, 持续交付]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
GitHub Flow 是 GitHub 官方推荐的工作流，比 Git Flow 简单得多：核心只有一条长期分支 `main`，所有开发都在短期 feature 分支上进行，适合持续交付、快速迭代的项目。

## 关键信息

### 核心流程
1. 从 `main` 创建 feature 分支
2. 在 feature 分支上开发并提交
3. 创建 Pull Request
4. 代码审查通过后合并到 `main`
5. 合并后立即部署

### 优缺点
- ✅ 流程简单、适合快速迭代、持续交付
- ❌ 不支持多版本同时维护
- Google 内部大量采用类似策略

## 关联连接
- [[Git]] — 所属工具
- [[GitHub]] — 提出者
- [[GitFlow]] — 更复杂的经典模型
- [[TrunkBasedDevelopment]] — 理念相近的主干开发
- [[code-review]] — PR 审查是流程核心环节
- [[摘要-一线大厂Git规范]] — 来源