---
title: "object"
type: concept
tags: [Elasticsearch, 数据类型, 复杂对象]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
object 是 Elasticsearch 中用于存储 JSON 对象的默认数据类型，支持嵌套结构，但会“拍平”嵌套数组，丢失对象之间的边界。

## 关键信息
- **拍平问题**：嵌套数组会被“拍平”成扁平结构，丢失对象之间的对应关系
- **示例**：商品对象包含多个SKU数组（每个SKU有颜色和尺寸），查询“颜色=红 且 尺寸=XL”会误命中“红L + 蓝XL”
- **适用场景**：简单嵌套结构，不需要精确查询嵌套对象之间的关系
- **与 nested 对比**：nested 保持对象边界，适合精确查询；object 更简单高效，适合简单结构
- **性能**：比 nested 更快，因为不需要单独建索引文档

## 关联连接
- [[Elasticsearch]] — 使用 object 类型的搜索引擎
- [[nested]] — ES 嵌套对象类型（保持对象边界）
- [[Mapping]] — 定义字段类型为 object
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）