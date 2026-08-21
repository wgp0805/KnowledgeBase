---
title: "PostgresSaver"
type: entity
tags: [LangGraph, 持久化, Checkpointer, PostgreSQL]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
LangGraph 的 Checkpointer 检查点存储实现，将单 thread 会话短期记忆持久化至 PostgreSQL。替代默认的 [[InMemorySaver]]（仅内存，重启丢失），实现同 thread_id 会话记忆永续、不同 thread_id 数据隔离、程序重启记忆不丢失的生产级能力。

## 关键信息
- **核心角色**：Checkpointer 检查点
- **核心用途**：单 thread 会话短期记忆，保存 Graph 运行 state、消息历史、节点执行断点，支持中断后恢复执行、回溯历史快照
- **数据隔离**：以 thread_id 为核心隔离，不同 thread 会话数据完全隔离
- **写入时机**：自动写入，`graph.invoke()` 执行过程自动保存 checkpoint，无需手动调用 API
- **生命周期**：跟随会话 thread，可配置过期清理会话快照
- **依赖**：`langgraph-checkpoint-postgres` 3.1.2 + `psycopg` 3.3.4
- **自动建表**：`checkpointer.setup()` 自动创建四张表：
  - `checkpoints`：thread_id/checkpoint_id/parent_checkpoint_id/checkpoint(jsonb)/metadata(jsonb)
  - `checkpoint_blobs`：thread_id/checkpoint_ns/channel/version/type/blob(bytea)
  - `checkpoint_writes`：thread_id/checkpoint_ns/checkpoint_id/task_id/idx/channel/type/blob/task_path
  - `checkpoint_migrations`：v(integer)
- **用法**：`PostgresSaver.from_conn_string(DB_URI)` 绑定数据库，`graph.compile(checkpointer=checkpointer)` 注入持久化器

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 所属框架
- [[PostgreSQL]] — 持久化载体
- [[PostgresStore]] — 互补的长期记忆存储
- [[InMemorySaver]] — 内存临时版，仅测试用
- [[Checkpointer]] — 所属概念
- [[AgentMemory]] — 记忆系统概念
