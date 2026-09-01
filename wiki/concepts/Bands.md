---
title: "Bands"
type: concept
tags: [概念, AI工程, SDLC, 监控, 运维]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
Bands 是 [[AINativeSDLC]] 运维阶段的监控响应分级机制，通过 bands.yaml 定义 1σ/2σ/3σ 三级响应。确定性脚本监控生产指标，控制带突破时按级别触发响应——轻度自动恢复，中度调用 [[ClaudeTag]]，重度人工介入。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[ClaudeTag]] — 由 bands 触发
- [[HealthCheck]] — 健康检查
