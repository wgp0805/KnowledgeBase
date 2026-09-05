---
title: "为什么 LLM 的上下文窗口不能无限大？"
type: source
tags: ["Context-Window", "LLM-原理", "面试题"]
sources: ["raw/01-articles/为什么 LLM 的上下文窗口不能无限大？.md"]
last_updated: 2026-09-01
---

# 为什么 LLM 的上下文窗口不能无限大？

面试题讲解上下文窗口受限的原因：注意力机制的计算复杂度 O(n²)、显存占用线性增长、长距离注意力衰减。沉默王二分析为什么不能简单「无限扩窗口」，以及 KV Cache、滑动窗口等工程解法。

## 关联连接
[[ContextWindow]], [[KVCache]], [[沉默王二]]
