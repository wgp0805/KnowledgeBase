---
title: "OnlineDDL"
type: concept
tags: [MySQL, DDL, 在线变更, 数据库运维]
sources: [raw/01-articles/千万级的大表如何新增字段？.md]
last_updated: 2026-08-14
---

## 定义
Online DDL（Online Data Definition Language）是 MySQL 5.6+ 引入的在线表结构变更机制，允许在执行 DDL 操作（如 ADD COLUMN、ADD INDEX）期间不阻塞或仅短暂阻塞 DML 操作，从而减少对线上业务的影响。

## 关键信息
- **语法**：`ALTER TABLE ... ALGORITHM=INPLACE, LOCK=NONE`
- **ALGORITHM 三档**：
  - `INSTANT`（MySQL 8.0.12+）：仅修改元数据，秒级完成，不锁表
  - `INPLACE`：在存储引擎内部完成，不复制全表
  - `COPY`：创建临时表复制数据，最慢
- **LOCK 三档**：`NONE`（不锁）→ `SHARED`（读锁）→ `EXCLUSIVE`（写锁）

## 致命缺陷
1. 仍可能触发表锁（如添加全文索引）
2. 磁盘空间需双倍（500GB 表需 1TB 空闲）
3. 主从延迟风险（从库单线程回放）

## 适用场景
- <1 亿行的小表变更
- MySQL 8.0+ 优先用 `ALGORITHM=INSTANT` 秒级加字段

## 关联连接
- [[MySQL]] — 所属数据库
- [[摘要-千万级大表新增字段方案]] — 来源
- [[PT-OSC]] — 替代方案（低版本 MySQL）
- [[GhOst]] — 替代方案（高并发大表）
