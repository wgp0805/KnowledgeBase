---
title: "AgentMemory"
type: concept
tags: [AI, Agent, 记忆系统, 概念]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 定义
智能体（Agent）的记忆系统，指 Agent 跨轮次、跨会话、跨用户保持与检索信息的能力。生产级 Agent 记忆通常划分为**短期会话记忆**（上下文续接）与**长期用户记忆**（个性化画像）两层，二者独立存储、能力互补。

## 关键信息
- **两层划分**（以 LangGraph 为典型）：
  - 短期会话记忆 → [[Checkpointer]]（如 [[PostgresSaver]]）：自动写入、thread_id 隔离、支持中断恢复
  - 长期用户记忆 → Store（如 [[PostgresStore]]）：手动写入、namespace+key 隔离、跨会话共享
- **常见误区**：混淆「会话运行状态记忆」与「用户业务长期记忆」，导致会话无法续连、用户记忆错乱、多线程数据互通异常
- **语义检索**：长期记忆可配合向量嵌入实现语义相似度匹配（非精准匹配），是个性化应答与知识库智能召回的核心能力，依赖 [[pgvector]]（生产）或 [[InMemoryStore]]（测试）
- **工具化**：记忆操作可封装为 Agent 工具（`@tool`），让智能体自主识别用户意图、读写用户档案、清理记忆，实现闭环

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[LangGraph]] — 典型实现框架
- [[Checkpointer]] — 短期会话记忆概念
- [[PostgresSaver]] — 短期记忆实现
- [[PostgresStore]] — 长期记忆实现
- [[pgvector]] — 语义检索依赖
- [[AgentEngineering]] — 相关工程化概念
