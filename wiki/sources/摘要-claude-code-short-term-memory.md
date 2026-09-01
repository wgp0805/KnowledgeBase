---
title: "Claude Code 的短期记忆是怎么实现的"
type: source
tags: ["Claude-Code", "短期记忆", "沉默王二"]
sources: ["raw/01-articles/Claude Code 的短期记忆是怎么实现的？.md"]
last_updated: 2026-09-01
---

# Claude Code 的短期记忆是怎么实现的

沉默王二通过翻阅 Claude Code 源码和从零实现 PaiCLI，拆解 Claude Code 短期记忆三层机制：对话历史数组存储、上下文窗口耗尽时的摘要压缩、压缩后哪些信息保留哪些丢弃。

## 关联连接
[[Claude-Code]], [[短期记忆]], [[PaiCLI]], [[沉默王二]]
