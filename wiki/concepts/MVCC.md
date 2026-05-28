---
title: "MVCC"
type: concept
tags: [数据库, 并发控制, 事务]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
---

## 定义

MVCC（Multi-Version Concurrency Control，多版本并发控制）是一种数据库并发控制机制，通过维护数据的多个版本来实现读写不阻塞，提高数据库并发性能。

## 关键信息

**PostgreSQL 与 MySQL 的 MVCC 实现差异：**

| 数据库 | 版本管理方式 | 优点 |
| --- | --- | --- |
| PostgreSQL | 每行存储多个版本，旧版本保留在堆中，直到被清理 | 读写完全隔离，支持可串行化快照隔离 |
| MySQL | 只保留当前版本，旧版本在 undo log 中暂存 | 读取更快，但长事务可能导致回滚段膨胀 |

**具体表现：**
- PostgreSQL：即使在写数据，别人也可以读取"之前的状态"
- MySQL：如果事务未提交，其他事务看到的是"脏读"或"不可重复读"（取决于隔离级别）

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[PostgreSQL]] — PostgreSQL 的 MVCC 实现
- [[MySQL]] — MySQL 的 MVCC 实现
- [[WAL]] — 预写日志，与 MVCC 配合保证数据一致性
