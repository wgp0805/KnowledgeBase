---
title: "Sequence"
type: concept
tags: [数据库, 序列, ID生成]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
---

## 定义

Sequence（序列）是数据库中的独立对象，用于生成唯一的数字序列，常用于主键 ID 生成。PostgreSQL 支持真正的独立序列对象，可脱离表单独使用，支持跨表共享。

## 关键信息

**PostgreSQL 的 Sequence：**
```sql
-- 创建独立序列
CREATE SEQUENCE order_seq START WITH 1 INCREMENT BY 1;
-- 使用序列生成 ID
INSERT INTO orders (id, name) VALUES (nextval('order_seq'), 'test');
```

**MySQL 的限制：**
- MySQL 5.7+ 通过 AUTO_INCREMENT 模拟序列
- 缺少真正的独立序列对象
- 不能跨表共享序列
- 分布式环境下难以保证唯一性（需配合 Redis 等中间件）

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[PostgreSQL]] — PostgreSQL 支持独立序列
- [[MySQL]] — MySQL 的 AUTO_INCREMENT 机制
