---
title: "KV Cache"
type: concept
tags: ["KV-Cache", "LLM", "推理优化"]
last_updated: 2026-09-01
---

# KV Cache

KV Cache 是 LLM 推理时缓存 Key-Value 对以避免重复计算的机制。DeepSeek V4 通过 CSA/HCA 优化 KV Cache，降低缓存成本。上下文窗口不能无限大的原因之一就是 KV Cache 显存占用线性增长。

## 关联连接
[[DeepSeek-V4]], [[CSA]], [[HCA]], [[ContextWindow]], [[沉默王二]]
