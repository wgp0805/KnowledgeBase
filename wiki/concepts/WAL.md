---
title: "WAL"
type: concept
tags: [数据库, 日志, 持久性]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
---

## 定义

WAL（Write-Ahead Logging，预写日志）是一种数据库持久性保证机制，要求在修改数据之前先将变更记录到日志中，确保数据库在崩溃后能够恢复到一致状态。

## 关键信息

- **核心原则**：数据变更前先写日志
- **作用**：确保数据持久性和一致性
- **应用**：PostgreSQL 的 WAL 机制成熟，是流复制和逻辑复制的基础

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[PostgreSQL]] — PostgreSQL 使用 WAL 机制
- [[MVCC]] — 与 WAL 配合保证数据一致性
- [[流复制]] — 基于 WAL 的复制机制
- [[逻辑复制]] — 基于 WAL 的逻辑复制
