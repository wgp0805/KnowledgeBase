---
title: "摘要-es-data-types-mysql-mapping"
type: source
tags: [Elasticsearch, MySQL, 数据类型, 映射]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 核心摘要
本文介绍了 Elasticsearch 支持的数据类型及其与 MySQL 的映射关系。重点讲解了 ES 的五大数据类型（核心、数字、时间、布尔、复杂），特别是 text 和 keyword 的区别与使用场景。文章详细对比了 MySQL 与 ES 的概念映射（Database→Index、Row→Document、Column→Field、Schema→Mapping），并提供了字段类型映射表。最后指出了动态映射的潜在陷阱，建议生产环境显式定义 Mapping。

## 关联连接
- [[Elasticsearch]] — 数据存储和搜索引擎
- [[MySQL]] — 关系型数据库
- [[text]] — ES 分词字符串类型
- [[keyword]] — ES 不分词字符串类型
- [[scaled_float]] — ES 精确数值类型
- [[动态映射]] — ES 自动类型推断
- [[倒排索引]] — ES 核心索引结构
- [[nested]] — ES 嵌套对象类型
- [[object]] — ES 对象类型
- [[Mapping]] — ES 字段定义
- [[Type]] — ES 历史概念（已废弃）