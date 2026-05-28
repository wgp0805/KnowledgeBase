---
title: "JSONB"
type: concept
tags: [数据库, JSON, 数据类型]
sources: [raw/01-articles/PostgreSQL这么多优势，为什么还要使用MySQL？？.md]
last_updated: 2026-05-28
---

## 定义

JSONB（JSON Binary）是 PostgreSQL 的二进制 JSON 数据类型，不仅支持 JSON 存储，还能建立索引、高效查询和更新，性能远超普通 JSON 字段。

## 关键信息

- **存储格式**：二进制格式，解析后存储
- **索引支持**：支持 GIN 索引，查询效率高
- **操作能力**：支持 JSON 路径查询、更新、合并等操作
- **性能优势**：比普通 JSON 文本类型性能更好

## 关联连接

- [[摘要-PostgreSQL-vs-MySQL]] — 来源
- [[PostgreSQL]] — PostgreSQL 的数据类型
- [[MySQL]] — MySQL 的 JSON 类型对比
