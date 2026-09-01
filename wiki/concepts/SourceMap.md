---
title: "SourceMap"
type: concept
tags: [概念, 前端工程, 调试, 安全]
sources: [raw/01-articles/2026-08-26-Claude Code 与 Grok Bot 被拆开后：AI Agent 真正难复制的是什么？.md]
last_updated: 2026-08-27
---

## 定义
Source Map 是前端构建工具产出的源码映射文件，将压缩/打包后的代码映射回原始源码。在 2026 年两起 AI Agent 事件中成为技术载体：Claude Code 2.1.88 发布资产误带内部调试文件暴露约 2000 个文件、50 万行内部代码；Grok Bot 外部开发者依据 0.18.0 客户端 Source Map 重建运行层。Source Map 误发布会显著降低外界理解产品的成本。

## 关联连接
- [[ClaudeCode]] — 事件主角
- [[GrokBot]] — 事件主角
- [[TaskDelegationSystem]] — 事件引出的核心概念
