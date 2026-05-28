---
title: "PostgreSQL"
type: entity
tags: [数据库, 开源, 关系型数据库]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
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

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[MySQL]] — 对比数据库
- [[TDSQL]] — 腾讯云 PostgreSQL 分支
- [[PolarDB]] — 阿里云 PostgreSQL 分支
- [[GaussDB]] — 华为云 PostgreSQL 分支
- [[MVCC]] — 多版本并发控制
- [[WAL]] — 预写日志机制
- [[JSONB]] — 二进制 JSON 类型
- [[Sequence]] — 数据库序列对象
