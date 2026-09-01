---
title: "PlanMode"
type: concept
tags: [概念, AI工程, ClaudeCode, 工作模式]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
Plan Mode 是 [[ClaudeCode]] 的工作模式，是 [[AINativeSDLC]] 中工程师的默认起点。工程师在 plan mode 下给 Claude [[SpecMd]]，Claude 产出计划但不执行，工程师反复迭代计划直到满意，提交为 [[PlanMd]]。接受后 Claude 切换到实施。Plan Mode 把"想清楚"和"做出来"分离，降低返工成本。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[PlanMd]] — Plan Mode 的产物
- [[SpecMd]] — Plan Mode 的输入
- [[AutoMode]] — 对应的自动执行模式
- [[计划模式]] — 相关概念
