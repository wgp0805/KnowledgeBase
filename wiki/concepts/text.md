---
title: "text"
type: concept
tags: [Elasticsearch, 数据类型, 字符串]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
text 是 Elasticsearch 中用于全文检索的字符串类型，会被分词器处理，将文本拆分成多个词条（Term），并建立倒排索引。

## 关键信息
- **分词特性**：写入时会被分词器拆分成多个词条（如“小米折叠屏手机”拆成“小米”、“折叠屏”、“手机”）
- **适用场景**：全文检索（`match` 查询），需要搜索文本内容的场景
- **查询方式**：使用 `match` 查询时，查询文本也会被分词，然后匹配倒排索引中的词条
- **与 keyword 的区别**：text 用于搜索，keyword 用于精确匹配、排序、聚合
- **生产最佳实践**：主字段用 `text` 做搜索，子字段用 `keyword` 做排序聚合（使用 `fields` 子字段）
- **注意事项**：text 类型字段默认不支持排序和聚合，因为分词后无法直接用于精确比较

## 关联连接
- [[Elasticsearch]] — 使用 text 类型的搜索引擎
- [[keyword]] — ES 不分词字符串类型（常与 text 配合使用）
- [[倒排索引]] — text 类型建立的索引结构
- [[analyzer]] — 分词器，决定 text 如何被分词
- [[Mapping]] — 定义字段类型为 text
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）