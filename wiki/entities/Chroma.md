---
title: "Chroma"
type: entity
tags: [向量数据库, RAG, AI, 开源]
sources: [raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md]
last_updated: 2026-06-02
---

## 定义
Chroma（ChromaDB）是开源的向量数据库，专为 AI 应用设计，常与 LangChain 搭配使用，是 RAG 架构中向量存储层的典型代表。

## 关键信息
- 开源向量数据库，专注于 AI/ML 应用场景
- 支持 Embedding 向量的存储、检索和相似度搜索
- 与 LangChain 深度集成，是 RAG 管道的常用向量存储后端
- 轻量级，适合快速原型开发和小规模生产部署
- **LangChain 集成**：`Chroma(collection_name, embedding_function, persist_directory)` 支持磁盘持久化，提供 add_documents/delete/similarity_search 统一接口；search 支持 similarity / similarity_score_threshold / mmr 三种检索类型（见 [[VectorStore]]）
- **规模定位**：中小规模应用；大规模选 Milvus，开发调试可用内存实现

## 关联连接
- [[RAG]] — Chroma 是 RAG 架构中的向量存储组件
- [[LangChain4j]] — 常与 Chroma 搭配使用的框架
- [[VectorStore]] — 向量库统一接口抽象
- [[LangChain]] — 深度集成的框架
- [[Elasticsearch]] — 另一种支持向量检索的搜索引擎
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 来源
- [[摘要-langchain-rag构建知识库-理论]] — LangChain 集成来源
