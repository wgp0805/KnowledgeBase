---
title: "InMemoryStore"
type: entity
tags: [LangGraph, Store, 内存存储, 测试]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
LangGraph Store 的内存临时版本，内置简易向量检索能力，无需安装 [[pgvector]] 插件即可开箱即用。适合本地开发、功能演示、语义检索逻辑调试，但进程重启后所有数据丢失，禁止生产使用。

## 关键信息
- 与 [[PostgresStore]] API 一致：put/get/search/delete
- 内置语义向量检索：配合 `IndexConfig(embeddings=..., embed_path=[...])` 即可使用
- 无需 PostgreSQL 与 pgvector，纯 Python 内存实现
- 缺点：进程重启数据全部丢失，仅用于测试

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 所属框架
- [[PostgresStore]] — 生产版对应物
- [[pgvector]] — 生产版语义检索依赖
- [[AgentMemory]] — 记忆系统概念
