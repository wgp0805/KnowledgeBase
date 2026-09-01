---
title: "TermIndex"
type: concept
tags: [数据结构, 倒排索引, Lucene, ElasticSearch]
sources: [raw/01-articles/2026-08-31 - 面试官：ElasticSearch 为什么快？.md]
last_updated: 2026-09-01
---

## 定义
Term Index 是 Lucene 词典查询三层结构中的第一层，相当于字典的"目录页"，只存 Term 的前缀（用 [[FST]] 实现），体积极小可常驻内存，用于快速定位目标 Term 在磁盘上的位置。

## 关键信息
### 三层词典查询结构
| 层级 | 位置 | 作用 |
|------|------|------|
| Term Index | 内存 | 存 Term 前缀（FST），定位磁盘块 |
| Term Dictionary | 磁盘 | 有序词典，存完整 Term |
| Posting List | 磁盘 | Term 对应的文档 ID 列表 |

### 核心价值
- 通过内存里的 Term Index，直接定位到目标 Term 所在的磁盘块，**最少只需要一次磁盘寻址**
- 解决"Term 有上亿个时如何快速找到目标 Term"的问题

## 关联连接
- [[FST]] — Term Index 的底层实现
- [[InvertedIndex]] — 倒排索引整体结构
- [[Elasticsearch]] — 使用 Term Index 的搜索引擎
- [[Lucene]] — 实现库
- [[摘要-es-为什么快-面试深度]] — 来源
