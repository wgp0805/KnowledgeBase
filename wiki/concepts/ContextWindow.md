---
title: "Context Window（上下文窗口）"
type: concept
tags: ["Context-Window", "LLM"]
last_updated: 2026-09-01
---

# Context Window（上下文窗口）

上下文窗口是 LLM 单次能处理的最大 token 数，不是聊天窗口。受限原因：注意力机制 O(n²) 复杂度、显存线性增长、长距离注意力衰减。窗口耗尽时需压缩（摘要/滑动窗口/分层记忆）。

## 关联连接
[[上下文爆炸]], [[短期记忆]], [[KVCache]], [[沉默王二]]
