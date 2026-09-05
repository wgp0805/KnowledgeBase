---
title: "FeatureToggle"
type: concept
tags: [软件工程, 分支策略, 持续交付, 功能开关]
sources: [raw/09-archive/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Feature Toggle（功能开关/特性开关）是一种用配置开关控制功能是否对外可见/可用的技术，允许未完成功能安全地合入主干而不上线，是 Trunk-Based Development 与渐进式重构（[[渐进式重构]]）的关键支撑机制。

## 关键信息
- **核心价值**：代码已合入主干但功能未发布——用开关控制，与"功能是否完成"解耦
- **支撑主干开发**：保持 `main` 始终可部署，未完成功能靠开关隔离（见 [[TrunkBasedDevelopment]]）
- **支撑渐进式重构**：新旧架构共存时用开关切换（见 [[渐进式重构]]，OpenCode v1.17.x 期间通过"temporary setting to switch between the old and new interface"实现）
- **落地形式**：配置中心（Nacos Config 等）、环境变量、代码标记
- **注意**：开关会累积技术债，需定期清理已稳定的开关

## 关联连接
- [[TrunkBasedDevelopment]] — 主干开发的核心支撑
- [[渐进式重构]] — 渐进式架构升级的支撑
- [[Nacos]] — 配置中心托管开关
- [[grayscale-release]] — 相关发布策略
- [[摘要-一线大厂Git规范]] — 来源