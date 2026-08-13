---
title: "GitFlow"
type: concept
tags: [Git, 分支模型, 版本管理, 团队协作]
sources: [raw/09-archive/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Git Flow 是 2010 年由 Vincent Driessen 提出的分支模型，定义了两种长期分支和三种短期分支，是至今仍被大厂采用的经典企业级分支策略，适合有明确版本发布计划的大型项目。

## 关键信息

### 两种长期分支（永久存在）
- **master/main**：生产环境分支，存放已发布稳定版本，**禁止直接提交代码**
- **develop**：日常开发主分支，汇总所有正在推进的功能

### 三种短期分支
| 分支 | 从哪创建 | 完成后合并到 |
| --- | --- | --- |
| feature | develop | develop |
| release | develop | master 和 develop |
| hotfix | master | master 和 develop |

### 适用与简化
- **适用场景**：有明确版本发布计划的大型项目、需同时维护多个版本的软件
- **轻量版 Git Flow**：只保留 master + develop 两条长期分支，feature 从 develop 拉、hotfix 从 master 拉，去掉 release 分支用 tag 代替——中小团队常用

## 关联连接
- [[Git]] — 所属工具
- [[ConventionalCommits]] — 配合的提交规范
- [[语义化版本]] — release 分支对应的版本号
- [[GitHubFlow]] — 更轻量的替代模型
- [[TrunkBasedDevelopment]] — 另一种主流模型
- [[code-review]] — 配合的审查实践
- [[摘要-一线大厂Git规范]] — 来源