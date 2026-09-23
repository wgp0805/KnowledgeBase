---
title: "Rerank"
type: concept
tags: ["Rerank", "RAG"]
sources:
  - raw/01-articles/一文讲透 RAG：原理、优化与落地.md
last_updated: 2026-09-23
---

# Rerank

Rerank 是 RAG 中的精排步骤：向量检索召回粗结果后，用 Rerank 模型对结果重新排序，提升相关性。Embedding 负责召回，Rerank 负责精排，两者配合让 LLM 听懂人话。

## 关联连接
[[Embedding]], [[RAG]], [[沉默王二]]
