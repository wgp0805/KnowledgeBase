---
title: "ContextualRetrieval"
type: concept
tags: [RAG, 检索优化, 上下文增强]
sources: [raw/01-articles/一文讲透 RAG：原理、优化与落地.md]
last_updated: 2026-09-23
---

## 定义
Contextual Retrieval（上下文感知检索）是Anthropic提出的优化方法，在嵌入之前先让LLM给每个chunk补一段上下文说明，解决切块导致的指代关系切断问题。

## 关键信息
1. **核心问题**：
   - 切块会切断指代关系（如"该公司"指谁？答案在上一段）
   - 带着残缺文本去嵌入，向量自然也残缺
2. **解决方案**：
   - 嵌入之前，先让LLM给每个chunk补一段上下文说明
   - 原始chunk → LLM补上下文 → 带上下文的chunk → 再去嵌入
3. **效果**：
   - Anthropic实测：结合Contextual Embedding + BM25 + Rerank，检索失败率降低67%
   - 代价是建库时多一遍LLM调用
4. **价值**：
   - 提升长文档场景下的召回质量
   - 保留指代关系和上下文信息

## 关联连接
- [[RAG]] — 核心应用场景
- [[Chunk分块]] — 前置步骤
- [[Embedding向量化]] — 实现方式
- [[向量检索]] — 检索方式
