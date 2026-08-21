---
title: "摘要-langgraph-postgresql-会话记忆持久化"
type: source
tags: [来源, 原始文件, LangGraph, PostgreSQL, 会话记忆, 持久化]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md]
last_updated: 2026-08-21
---

## 核心摘要
lyshark 撰写的 LangGraph 会话记忆持久化实战教程，拆解 Checkpointer（PostgresSaver）与 Store（PostgresStore）两大核心存储体系。PostgresSaver 是单 thread 会话短期记忆，保存 Graph 运行 state、消息历史、节点执行断点，以 thread_id 隔离，`graph.invoke()` 自动写入 checkpoint，支持中断恢复与历史回溯；PostgresStore 是跨 thread 长期记忆，以 namespace + key 隔离，需手动调用 put/get/search/delete，存储用户画像、偏好、事实记忆与业务知识库，多个 thread_id 可共享同一份记忆。

环境搭建使用 PostgreSQL 18.6 + psycopg 3.3.4 + langgraph-checkpoint-postgres 3.1.2。`checkpointer.setup()` 自动创建四张表：`checkpoints`（thread_id/checkpoint_id/parent_checkpoint_id/checkpoint jsonb/metadata jsonb）、`checkpoint_blobs`（channel/version/type/blob bytea）、`checkpoint_writes`（task_id/idx/channel/blob/task_path）、`checkpoint_migrations`（v integer）。数据表永久留存，程序重启自动延续历史会话。

PostgresSaver 实战：通过 `PostgresSaver.from_conn_string()` 绑定数据库，`graph.compile(checkpointer=checkpointer)` 注入持久化器，每轮对话自动写入。示例验证 user_001 记住"王瑞 28 岁"、user_002 隔离看不到、程序重启后同 thread_id 仍能续聊。

PostgresStore 实战：基础 put/get/search 读写命名空间记忆；语义向量检索依赖 pgvector 插件（生产）或 InMemoryStore（测试，内置简易向量检索）；delete 支持单条与批量删除；工具化调用通过 `@tool` 装饰器封装 get_user_info/save_user_info/delete_user_memory，配合 `ToolRuntime[Context]` 注入 store 与 user_id，实现智能体自主读写用户档案闭环。

两套机制相互独立、数据隔离、能力互补，共同构成 LangGraph 企业级记忆体系，实现「会话不断连、用户有记忆、多端多线程数据互通」。

## 关联连接
- [[LangGraph]] — 本文核心框架，Python AI Agent 编排
- [[PostgreSQL]] — 持久化载体，官方推荐数据库
- [[lyshark]] — 本文作者，博客园博主
- [[PostgresSaver]] — Checkpointer 检查点存储，单会话短期记忆
- [[PostgresStore]] — Store 通用外部存储，跨会话长期记忆
- [[Checkpointer]] — LangGraph 检查点存储概念
- [[AgentMemory]] — 智能体记忆系统概念
- [[pgvector]] — PostgreSQL 向量检索扩展，Store 语义检索依赖
- [[InMemoryStore]] — 内存版 Store，测试用语义检索
- [[InMemorySaver]] — 内存版 Checkpointer，仅本地临时测试
- [[LangChain]] — LangGraph 的母框架
- [[Qwen]] — 示例使用 qwen2.5-1.5b-instruct 本地模型
- [[Celery]] — 对比参考（异步任务队列）
