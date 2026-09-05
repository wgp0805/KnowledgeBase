---
title: "InMemorySaver"
type: entity
tags: [LangGraph, Checkpointer, 内存存储, 测试]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
LangGraph Checkpointer 的内存临时版本，将会话数据存储在内存中。程序重启、线程销毁后数据直接丢失，仅适合本地临时测试。生产环境应使用 [[PostgresSaver]] 替代。

## 关键信息
- LangGraph 默认的 Checkpointer 实现
- 与 [[PostgresSaver]] API 一致，可无缝切换
- 仅内存存储，重启即丢失
- 适用场景：本地开发、单元测试、功能验证

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 所属框架
- [[PostgresSaver]] — 生产版对应物
- [[InMemoryStore]] — Store 的内存测试版
- [[Checkpointer]] — 所属概念
