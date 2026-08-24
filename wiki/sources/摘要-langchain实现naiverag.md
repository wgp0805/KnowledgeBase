---
title: "摘要：LangChain实现NaiveRAG朴素向量检索生成"
type: source
tags: [RAG, LangChain, ChromaDB, 向量检索, 实战]
sources: [raw/01-articles/2026-08-22-LangChain 实现NaiveRAG朴素向量检索生成 - lyshark.md]
last_updated: 2026-08-24
---

# 摘要：LangChain实现NaiveRAG

## 核心主旨
使用 LangChain + ChromaDB 实现最朴素的 RAG（Retrieval-Augmented Generation）流程，作为理解 RAG 原理的入门教程。

## 关键实现步骤
1. **文档加载**：使用 LangChain DocumentLoader 加载文本文件
2. **文本分割**：使用 TextSplitter 将文档切分为 chunk
3. **向量化**：使用 Embedding 模型将 chunk 转为向量
4. **存储**：将向量存入 ChromaDB 向量数据库
5. **检索**：用户提问 → 向量化 → 在 ChromaDB 中检索相似 chunk
6. **生成**：将检索结果作为上下文，交给 LLM 生成回答

## 技术栈
- LangChain（框架）
- ChromaDB（向量数据库）
- OpenAI Embeddings / 本地 Embedding 模型

## 原始信息
- **来源**: SegmentFault / lyshark
- **抓取日期**: 2026-08-22

## 关联连接
- [[RAG]]
- [[LangChain]]
- [[Chroma]]
- [[Embeddings]]
- [[VectorStore]]
- [[NaiveRAG]]
