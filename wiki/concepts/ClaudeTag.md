---
title: "ClaudeTag"
type: concept
tags: [概念, AI工程, SDLC, 运维, 事故响应]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 定义
Claude Tag 是 [[AINativeSDLC]] 闭合循环的实践：在 Slack/Teams 里 Claude 以自己身份成为频道成员，作为事故的第一响应者。确定性脚本监控生产，控制带突破时调用 Claude，Claude 在频道里响应并处理。

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[Bands]] — 触发 Claude Tag 的响应分级
- [[incident-severity-classification]] — 事故级别分类
