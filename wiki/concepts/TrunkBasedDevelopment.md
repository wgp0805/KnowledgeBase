---
title: "TrunkBasedDevelopment"
type: concept
tags: [Git, 分支模型, 主干开发, 持续交付]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Trunk-Based Development（主干开发）是 Google 等大厂推崇的分支策略，核心理念是所有开发者都在主干（trunk/main）上工作，通过短生命周期的 feature 分支进行变更。

## 关键信息

### 关键规则
- feature 分支生命周期**不超过 1-3 天**
- 保持 `main` **始终可部署**
- 通过 **Feature Toggle**（功能开关）控制未完成的功能（见 [[FeatureToggle]]）

### 适用场景与边界
- **适用**：需要极速迭代的互联网产品、DevOps 成熟度高的团队、任何规模
- **注意**：多版本维护为"有限支持"，依赖功能开关与特性标记

### 三种模型对比
| 对比维度 | Git Flow | GitHub Flow | Trunk-Based |
| --- | --- | --- | --- |
| 复杂度 | 高 | 低 | 中 |
| 适合团队 | 大团队 | 中小团队 | 任何规模 |
| 发布节奏 | 按版本发布 | 持续交付 | 持续交付 |
| 热修复 | hotfix 分支 | feature 分支 | feature 分支 |
| 多版本维护 | 支持 | 不支持 | 有限支持 |

大厂实际做法多为**混合模型**：Google 用 Trunk-Based，阿里用简化 Git Flow，腾讯结合自身定制。

## 关联连接
- [[Git]] — 所属工具
- [[GitFlow]] / [[GitHubFlow]] — 其他主流分支模型
- [[FeatureToggle]] — 主干开发的关键支撑机制
- [[CI-CD]] — 持续部署前提
- [[摘要-一线大厂Git规范]] — 来源