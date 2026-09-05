---
title: "PostgresStore"
type: entity
tags: [LangGraph, 持久化, Store, PostgreSQL, 长期记忆]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
LangGraph 的 Store 通用外部存储实现，专注用户级长期、跨线程全局记忆管理。不依赖、不绑定 thread_id，通过 namespace + key 全局维度管理记忆数据，支持用户偏好、个人档案、业务规则、知识库等长效数据的存储、查询、检索与删除，弥补 [[PostgresSaver]] 无法跨会话共享记忆的短板。

## 关键信息
- **核心角色**：Store 通用外部记忆存储
- **核心用途**：跨 thread 长期记忆，存储用户画像、用户偏好、事实记忆、业务知识库，多个会话 thread_id 可共享读取同一份记忆
- **数据隔离**：以 namespace + key 隔离，同一用户下全部 thread 可共享记忆
- **写入时机**：手动操作，需业务代码主动调用 put/get/search/delete，不会自动保存
- **生命周期**：用户级长期记忆，独立于会话，可持久保存用户事实
- **API**：
  - `store.put(namespace, key, value)` — 写入记忆
  - `store.get(namespace, key)` — 读取记忆
  - `store.search(namespace, query=..., limit=...)` — 搜索/语义检索
  - `store.delete(namespace, key)` — 删除记忆
- **语义向量检索**：原生 `store.search()` 向量检索依赖 [[pgvector]] 第三方插件（生产，Windows 部署复杂，适合 Linux）；[[InMemoryStore]] 内置简易内存向量检索（测试，开箱即用但重启丢失）
- **工具化**：通过 `@tool` 装饰器封装记忆操作，配合 `ToolRuntime[Context]` 注入 store 与 user_id，实现智能体自主读写用户档案闭环
- **数据表**：长期记忆统一存储在 PostgreSQL 的 `langgraph_store` 数据表中

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 所属框架
- [[PostgreSQL]] — 持久化载体
- [[PostgresSaver]] — 互补的短期会话记忆存储
- [[InMemoryStore]] — 内存测试版
- [[pgvector]] — 语义检索依赖的向量扩展
- [[AgentMemory]] — 记忆系统概念
