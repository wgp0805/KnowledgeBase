---
title: "Claude Code 如何检索长期记忆"
type: source
tags: ["Claude-Code", "长期记忆", "沉默王二"]
sources: ["raw/01-articles/Claude Code 如何检索长期记忆？.md"]
last_updated: 2026-09-01
---

# Claude Code 如何检索长期记忆

沉默王二翻阅 Claude Code 和 OpenClaw 源码后发现：Claude Code 检索长期记忆没有用向量搜索或语义匹配，而是用简单直接的方式（全文注入/关键词匹配）。分析这种设计的取舍。

## 关联连接
[[Claude-Code]], [[长期记忆]], [[OpenClaw]], [[沉默王二]]
