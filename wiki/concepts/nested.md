---
title: "nested"
type: concept
tags: [Elasticsearch, 数据类型, 复杂对象]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
nested 是 Elasticsearch 中用于存储嵌套对象的特殊数据类型，能够保持嵌套对象之间的独立性，避免 object 类型的“拍平”问题。

## 关键信息
- **解决的问题**：`object` 类型会把嵌套数组“拍平”，丢失对象之间的边界，导致查询错乱（如“颜色=红 且 尺寸=XL”会误命中“红L + 蓝XL”）
- **工作原理**：给每个嵌套对象单独建索引文档，保住对象之间的边界
- **适用场景**：一对多关系，如商品的多个SKU（每个SKU有独立的颜色、尺寸、价格）
- **代价**：查询稍慢、更新麻烦（需要重建嵌套文档）
- **与 object 对比**：object 适合简单嵌套，nested 适合需要精确查询的复杂嵌套

## 关联连接
- [[Elasticsearch]] — 使用 nested 类型的搜索引擎
- [[object]] — ES 对象类型（简单嵌套）
- [[Mapping]] — 定义字段类型为 nested
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）