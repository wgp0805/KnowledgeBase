---
title: "pgvector"
type: entity
tags: [PostgreSQL, 向量检索, 扩展, 语义搜索]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
PostgreSQL 的开源向量相似度检索扩展，为 PostgreSQL 添加向量数据类型与索引（IVFFlat/HNSW），支持语义相似度查询。是 [[PostgresStore]] 原生 `store.search()` 向量检索的生产级依赖。

## 关键信息
- 为 PostgreSQL 添加 vector 数据类型，支持维度声明（如 vector(1536)）
- 索引方案：IVFFlat（倒排文件 + 扁平量化）与 HNSW（分层可导航小世界图）
- 距离度量：L2 距离、内积、余弦距离
- LangGraph PostgresStore 语义检索的生产依赖：Windows 环境部署配置复杂，适合 Linux 生产服务器
- 测试场景可用 [[InMemoryStore]] 替代，无需安装插件但重启丢失

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[PostgreSQL]] — 宿主数据库
- [[PostgresStore]] — 依赖 pgvector 的 LangGraph 存储
- [[InMemoryStore]] — 无需 pgvector 的测试替代
- [[AgentMemory]] — 语义检索应用场景
