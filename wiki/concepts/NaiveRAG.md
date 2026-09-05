---
title: "NaiveRAG"
type: concept
tags: [RAG, 向量检索, LangChain, ChromaDB]
sources: [raw/01-articles/2026-08-22-LangChain 实现NaiveRAG朴素向量检索生成 - lyshark.md]
last_updated: 2026-08-24
---

# Naive RAG（朴素RAG）

## 核心定义
最基础的 RAG（Retrieval-Augmented Generation）实现方式。通过文档加载→文本分割→向量化→存储→检索→生成的线性流程，将外部知识注入 LLM 生成过程。

## 实现流程
1. **文档加载**：DocumentLoader 加载文本文件
2. **文本分割**：TextSplitter 将文档切分为 chunk
3. **向量化**：Embedding 模型将 chunk 转为向量
4. **存储**：向量存入向量数据库（如 ChromaDB）
5. **检索**：用户提问 → 向量化 → 检索相似 chunk
6. **生成**：检索结果作为上下文，交给 LLM 生成回答

## 技术栈
- LangChain（框架）
- ChromaDB（向量数据库）
- OpenAI Embeddings / 本地 Embedding 模型

## 局限性
- 纯向量相似度检索，无重排序
- 无查询改写或扩展
- 无多轮检索
- 适合入门理解 RAG 原理，生产环境通常需要更复杂的 RAG 变体（如 [[AgenticRAG]]、[[GraphRAG]]）

## 关联连接
- [[RAG]]
- [[LangChain]]
- [[Chroma]]
- [[Embeddings]]
- [[VectorStore]]
- [[AgenticRAG]]
