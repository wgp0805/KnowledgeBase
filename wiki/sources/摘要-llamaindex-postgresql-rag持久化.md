---
title: "摘要-llamaindex-postgresql-rag持久化"
type: source
tags: [来源, 原始文件, RAG, LlamaIndex, PostgreSQL, pgvector]
sources: [raw/09-archive/2026-09-18-基于 LlamaIndex+PostgreSQL 实现RAG持久化 - lyshark.md]
last_updated: 2026-09-20
---

## 核心摘要
在 CentOS Stream 10 上源码编译安装 PostgreSQL 18.6 + pgvector 向量插件，对接 LlamaIndex 实现 RAG 向量持久化。PGVector 作为 PostgreSQL 扩展可直接在关系型数据库中承载向量数据，对比 Qdrant、Milvus 等专用向量库，优势是无需额外维护独立向量服务，且原生支持元数据过滤，可基于部门/文档类型/权限标签实现企业多租户。文章给出最小化示例（自定义 Embedding 类 + OpenAILike 接入本地大模型 + PGVectorStore）和封装示例（RAGService 类，支持增量新增/按 doc_id 删除/元数据过滤检索/异常重试）。向量检索完整链路：文档分块 → Embedding 向量化 → 向量存入向量库 → 生成查询向量返回。

## 关联连接
- [[LlamaIndex]] — RAG 数据框架
- [[PostgreSQL]] — 关系型数据库
- [[pgvector]] — 向量检索扩展
- [[RAG]] — 检索增强生成
- [[VectorStoreRetriever]] — 持久化向量检索
- [[元数据过滤]] — 企业多租户权限隔离
- [[Rerank]] — 召回精度优化
- [[lyshark]] — 作者