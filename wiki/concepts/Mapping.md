---
title: "Mapping"
type: concept
tags: [Elasticsearch, 数据类型, 索引]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
Mapping 是 Elasticsearch 中定义索引字段名、数据类型及相关配置的过程，类似于关系型数据库中的 Schema 定义。它决定了字段如何被索引和存储。

## 关键信息
- **作用**：定义字段名、数据类型、分词器、是否索引等配置
- **与 MySQL Schema 对比**：MySQL 的 Schema 定义表结构，ES 的 Mapping 定义文档字段结构
- **类型不可变性**：Mapping 一旦创建，字段类型不能修改（底层 Lucene 段不可变），需要修改时只能重建索引（reindex）
- **动态映射**：如果未显式定义 Mapping，ES 会自动推断字段类型（Dynamic Mapping），但可能导致类型误判
- **生产建议**：显式定义 Mapping，关闭自动检测，避免类型推断错误

## 关联连接
- [[Elasticsearch]] — 使用 Mapping 的搜索引擎
- [[text]] — ES 分词字符串类型
- [[keyword]] — ES 不分词字符串类型
- [[动态映射]] — ES 自动类型推断
- [[Type]] — ES 历史概念（已废弃）
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）