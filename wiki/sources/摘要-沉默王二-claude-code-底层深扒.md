---
title: "摘要-沉默王二-claude-code-底层深扒"
type: source
tags: [Claude Code, 架构, 沉默王二, 微信公众号]
sources: [raw/01-articles/老板：“刚刚，阿里全面禁用Claude，我们要不要跟风？”，我：“Claude Code的底层我刚严肃深扒，别上头。”.md]
last_updated: 2026-07-03
---

## 核心摘要
微信公众号沉默王二在阿里全面禁用 Claude 的背景下，从源码层面深度解析 Claude Code 的底层架构。文章详细介绍了 Query Loop 异步生成器模式、StreamingToolExecutor 推测执行、自声明工具系统（5 维度接口）、子 Agent 作为独立 Query Loop 实例的设计、7 级权限模式（含 auto 模式的 LLM 分类器）以及 Hook 优先级覆盖机制。

## 关联连接
- [[ClaudeCode]] — 核心剖析对象
- [[沉默王二]] — 作者
- [[Agent]] — Agent 循环核心概念
