---
title: "KV缓存压缩"
type: concepts
tags:
  - 推理
  - 显存
sources: []
last_updated: 2026-09-15
---

## 定义
降低 Transformer 推理时 KV Cache 显存占用的技术族：量化、共享、驱逐、滑动窗口，是长上下文与高并发推理的关键。

## 关联连接
- [[长上下文]]

- [[混合注意力架构]]

- [[IndexPool]]

- [[HCA]]
