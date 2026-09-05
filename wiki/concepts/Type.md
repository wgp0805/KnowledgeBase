---
title: "Type"
type: concept
tags: [Elasticsearch, 历史概念, 已废弃]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
Type 是 Elasticsearch 7.0 之前用于在索引内逻辑分组文档的概念，类似于关系型数据库中的表。但在 ES 7.0 中已被废弃，8.0 中彻底移除。

## 关键信息
- **历史角色**：在 ES 7.0 之前，一个索引可以包含多个 Type，每个 Type 类似一张表
- **废弃原因**：不同 Type 共用同一份底层 Lucene 索引，字段会互相干扰（A Type 里字段是 date，B Type 里同名字段就得是 date），设计上不合理
- **当前状态**：ES 7.0 开始废弃 Type，ES 8.0 彻底移除。现在一个索引直接对应一个文档类型
- **与 MySQL 类比**：旧教程中“Table 对应 Type”的说法已过时，现在 Database→Index、Row→Document

## 关联连接
- [[Elasticsearch]] — 使用 Type 的搜索引擎（已废弃）
- [[Mapping]] — ES 字段定义（替代 Type 的逻辑分组）
- [[MySQL]] — 关系型数据库（Table 对应 Index）
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）