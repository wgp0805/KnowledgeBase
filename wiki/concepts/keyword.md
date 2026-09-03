---
title: "keyword"
type: concept
tags: [Elasticsearch, 数据类型, 字符串]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
keyword 是 Elasticsearch 中用于精确匹配、排序和聚合的字符串类型，不会被分词，整条字符串原样存入索引。

## 关键信息
- **不分词特性**：整条字符串原样存入索引，不会被分词器处理
- **适用场景**：精确匹配（`term` 查询）、排序、聚合（如统计、分组）
- **查询方式**：使用 `term` 查询进行精确匹配，适合状态码、标签、ID 等字段
- **与 text 的区别**：keyword 用于精确操作，text 用于全文检索
- **ignore_above 参数**：默认 256，超过 256 字符的内容不会被索引，这是个经典坑
- **生产最佳实践**：作为 text 字段的子字段（`fields`），实现一次定义两种玩法：text 搜索 + keyword 排序聚合

## 关联连接
- [[Elasticsearch]] — 使用 keyword 类型的搜索引擎
- [[text]] — ES 分词字符串类型（常与 keyword 配合使用）
- [[Mapping]] — 定义字段类型为 keyword
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）