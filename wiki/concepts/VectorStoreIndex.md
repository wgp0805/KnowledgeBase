---
title: "VectorStoreIndex"
type: concept
tags: [LlamaIndex, 向量索引, RAG]
sources: [raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 定义
VectorStoreIndex 是 LlamaIndex 的核心索引类型，将文档切分为 Node，通过 Embedding 模型向量化存入向量数据库，构建支持语义检索的索引结构。

## 关键信息
- **构建流程**：Document → Node Parser（切分） → Embedding（向量化） → VectorStore（存储）
- **查询引擎**：`index.as_query_engine()` 一键生成问答引擎，支持流式、重排序、混合检索
- **检索器**：`index.as_retriever()` 固化检索参数，返回相关 Node 列表
- **多索引支持**：支持向量索引、关键词索引、知识图谱索引等多种索引类型组合

## 关联连接
- [[摘要-langchain-langgraph-llamaindex对比]] — 来源
- [[LlamaIndex]] — 所属框架
- [[RAG]] — 核心应用场景
- [[LlamaParse]] — 复杂文档解析器
- [[Embeddings]] — 向量化组件