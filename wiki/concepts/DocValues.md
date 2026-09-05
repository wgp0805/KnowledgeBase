---
title: "DocValues"
type: concept
tags: [数据结构, 列式存储, Lucene, ElasticSearch]
sources: [raw/01-articles/2026-08-31 - 面试官：ElasticSearch 为什么快？.md]
last_updated: 2026-09-01
---

## 定义
Doc Values 是 Lucene/ES 在写入时额外存储的列式存储结构，用于加速排序、聚合等"按字段值"计算的操作，避免回源解析倒排索引原文。

## 关键信息
### 为什么需要 Doc Values
- 倒排索引擅长"找到文档"（Term → 文档 ID 列表）
- 但排序和聚合需要"按字段值"来算，用倒排索引就得把所有文档原文拉出来解析一遍，太浪费
- 所以 ES 写入时额外存一份列式存储的 Doc Values，排序聚合直接读它

### 与倒排索引的分工
| 操作 | 用哪个 |
|------|--------|
| 关键词搜索（找文档） | 倒排索引 |
| 排序、聚合（按字段值算） | Doc Values |
| 数值/地理位置范围查询 | BKD-Tree |

## 关联连接
- [[InvertedIndex]] — 互补关系
- [[Segment]] — Doc Values 存储在 Segment 中
- [[Elasticsearch]] — 使用 Doc Values 的搜索引擎
- [[Lucene]] — 实现库
- [[摘要-es-为什么快-面试深度]] — 来源
