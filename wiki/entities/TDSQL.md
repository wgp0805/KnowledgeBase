---
title: "TDSQL"
type: entity
tags: [数据库, 腾讯云, 分布式, PostgreSQL]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
---

## 定义

TDSQL 是腾讯云基于 PostgreSQL 打造的分布式数据库（开源代号 TBase），通过引入 GTM 全局事务管理器和分布式协调，实现跨 shard 事务能力。

## 关键信息

- **开源代号**：TBase
- **GitHub**：https://github.com/Tencent/TBase
- **核心技术**：GTM 全局事务管理器 + 分布式协调
- **核心能力**：跨 shard 事务支持

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[PostgreSQL]] — 技术底座
- [[PolarDB]] — 同类竞品
- [[GaussDB]] — 同类竞品
