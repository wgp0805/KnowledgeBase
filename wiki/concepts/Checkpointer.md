---
title: "Checkpointer"
type: concept
tags: [LangGraph, 记忆, 持久化, 概念]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
LangGraph 中的检查点存储机制，用于持久化单 thread 会话的运行状态（state）、消息历史与节点执行断点。核心特征是**自动写入**（`graph.invoke()` 执行过程自动保存）与**thread_id 隔离**（不同 thread 数据完全隔离），支持中断后恢复执行与历史快照回溯。

## 关键信息
- **与 Store 的区别**：Checkpointer 是会话级短期记忆（自动、thread_id 隔离），Store 是用户级长期记忆（手动、namespace+key 隔离、跨 thread 共享）
- **实现**：
  - [[InMemorySaver]] — 内存临时版，仅测试
  - [[PostgresSaver]] — PostgreSQL 持久化版，生产级
- **自动建表**：`checkpointer.setup()` 创建 checkpoints/checkpoint_blobs/checkpoint_writes/checkpoint_migrations 四张表
- **数据结构**：checkpoint 以 jsonb 存储 state 与 metadata，blob 以 bytea 存储序列化数据，支持 parent_checkpoint_id 链式回溯

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 所属框架
- [[PostgresSaver]] — PostgreSQL 实现
- [[InMemorySaver]] — 内存实现
- [[AgentMemory]] — 上位记忆概念
- [[PostgresStore]] — 互补的 Store 机制
