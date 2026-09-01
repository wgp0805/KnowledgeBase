---
title: "AutoMode"
type: concept
tags: [概念, AI工程, ClaudeCode, 工作模式]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
Auto Mode 是 [[ClaudeCode]] 的自动执行模式，与 [[PlanMode]] 相对。在 [[PlanMd]] 被接受后，Claude 切换到 Auto Mode 实施计划。Auto Mode 下 Claude 自主执行，但仍受 [[Hooks]] 护栏约束。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[PlanMode]] — 对应的规划模式
- [[PlanMd]] — Auto Mode 的触发条件
- [[Hooks]] — Auto Mode 的护栏
- [[auto-mode]] — 相关概念
- [[YOLO模式]] — 相关的自主执行模式
