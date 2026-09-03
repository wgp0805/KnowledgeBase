---
title: "scaled_float"
type: concept
tags: [Elasticsearch, 数据类型, 数值]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
scaled_float 是 Elasticsearch 中用于存储精确数值的浮点类型，通过指定缩放因子（scaling_factor），将浮点数转换为整数存储，既省空间又精确。

## 关键信息
- **原理**：指定 `scaling_factor`（如 100），底层实际存 `long`（价格 19.99 存成 1999），展示时再除回去
- **解决的问题**：ES 没有真正的十进制精确类型，`double` 存金额会有精度问题（0.1 + 0.2 ≠ 0.3）
- **适用场景**：订单金额、价格等需要精确计算的字段
- **与 MySQL DECIMAL 对比**：MySQL 的 DECIMAL 是精确十进制类型，ES 用 scaled_float 模拟类似效果
- **注意事项**：scaling_factor 需根据业务精度需求设置，如金额保留两位小数则设为 100

## 关联连接
- [[Elasticsearch]] — 使用 scaled_float 类型的搜索引擎
- [[MySQL]] — 关系型数据库（DECIMAL 类型对比）
- [[Mapping]] — 定义字段类型为 scaled_float
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）