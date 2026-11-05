---
title: "PostgreSQL"
type: entity
tags: [数据库, 开源, 关系型数据库]
sources: [raw/09-archive/PostgreSQL这么多优势，为什么还要使用MySQL？？.md, raw/09-archive/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md, raw/09-archive/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义

PostgreSQL 是一个功能强大的开源对象-关系型数据库系统，以其可靠性、功能完整性和性能著称。它是国产数据库创新的首选技术底座，国内多家头部科技企业基于 PostgreSQL 构建分布式、云原生或 HTAP 数据库系统。

## 关键信息

**技术优势：**
- **数据类型丰富**：支持 ARRAY、范围类型、复合类型、JSONB 等高级数据类型
- **独立序列对象**：支持真正的 Sequence，可跨表共享，分布式环境下保证唯一性
- **扩展生态强大**：可编程数据库，支持 TimescaleDB、pg_trgm、Citus 等扩展
- **性能监控完善**：内置 pg_stat_activity、pg_stat_statements、pg_locks 等统计视图
- **复制机制成熟**：支持流复制（同步/异步）、逻辑复制、WAL 机制
- **MVCC 实现优秀**：每行存储多个版本，读写完全隔离，支持可串行化快照隔离
- **开源彻底**：BSD-like 许可证，完全自由，由基金会主导

**国产数据库基于 PostgreSQL 的产品：**
- 腾讯云 TDSQL PG 版（TBase）
- 阿里云 PolarDB for PostgreSQL
- 华为云 GaussDB（openGauss）
- 杭州易景数通 openHalo

**作为 AI Agent 记忆持久化载体：**
- LangGraph 官方推荐的会话记忆数据库，配合 [[PostgresSaver]]（Checkpointer）与 [[PostgresStore]]（Store）实现企业级记忆体系
- `checkpointer.setup()` 自动创建 checkpoints/checkpoint_blobs/checkpoint_writes/checkpoint_migrations 四张表
- 长期记忆存储在 langgraph_store 表，支持语义检索（依赖 [[pgvector]] 扩展）
- 在 [[RenoPit]] 项目中作为核心依赖，健康检查执行 `SELECT 1` + 连接池状态

### 云梯 SaaS 的 RLS 与多库实践（2026-11-05，详见 [[摘要-云梯saas智能客服]]）
[[云梯智能客服系统]]用 PostgreSQL 17 承载 6 个独立数据库（user_db/tenant_db/customer_db/billing_db/ops_db/ai_db）共 87 张表：
- **RLS 作为多租户第三道防线**：customer_db 对带 `tenant_code` 的表 `ENABLE/FORCE ROW LEVEL SECURITY`，连接借出时 `set_config('app.tenant_code', ...)`，SQL 忘写租户条件也不会越权（详见 [[RLS]]）
- **禁止跨库外键**，跨服务关联通过业务键与内部接口完成
- **原子序号**：`UPDATE session SET last_msg_seq = last_msg_seq + 1 ... RETURNING last_msg_seq` 保证并发下会话内消息序号唯一
- **幂等与并发控制**：大量使用唯一约束、条件更新（`export_time IS NULL`）、UPSERT 解决真实并发
- **类型选择**：金额用 NUMERIC 避免浮点误差、状态/类型用 SMALLINT + CHECK、业务 ID 用雪花算法、审计时间用服务端时间

## 关联连接
- [[摘要-云梯saas智能客服]] — 来源（RLS 与多库实践）
- [[云梯智能客服系统]] — 实践项目
- [[RLS]] — 行级安全

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源（LangGraph 记忆持久化）
- [[摘要-renopit-demo-healthcheck-docker]] — 来源（RenoPit 核心依赖）
- [[PostgresSaver]] — LangGraph Checkpointer 实现
- [[PostgresStore]] — LangGraph Store 实现
- [[pgvector]] — 向量检索扩展
- [[MySQL]] — 对比数据库
- [[TDSQL]] — 腾讯云 PostgreSQL 分支
- [[PolarDB]] — 阿里云 PostgreSQL 分支
- [[GaussDB]] — 华为云 PostgreSQL 分支
- [[MVCC]] — 多版本并发控制
- [[WAL]] — 预写日志机制
- [[JSONB]] — 二进制 JSON 类型
- [[Sequence]] — 数据库序列对象
