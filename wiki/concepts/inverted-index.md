---
title: "inverted-index"
type: concept
tags: [搜索引擎, 数据结构, 全文检索, Lucene]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

倒排索引（Inverted Index）是全文搜索引擎的核心数据结构。它将文档中的每个不重复的词条（Term）映射到包含该词条的文档列表，从而实现无需扫描全部文档即可快速定位包含特定关键词的文档。

## 关键信息

### 工作原理
1. 将每个文档拆分成独立的词条（Token）
2. 创建一个包含所有不重复词条的排序列表
3. 列出每个词条出现在哪些文档中

### 示例
文档1：`Study every day, good good up to forever`
文档2：`To forever, study every day, good good up`

倒排索引结构：
| 词条 | 文档列表 |
|------|---------|
| day | 1, 2 |
| every | 1, 2 |
| forever | 1, 2 |
| good | 1, 2 |
| study | 1, 2 |
| to | 1, 2 |
| up | 1, 2 |

搜索 `to forever` 时，通过倒排索引直接定位包含这些词条的文档。

### 在 ES 中的实现
- 一个 ES 分片就是一个 Lucene 索引
- 每个分片都包含独立的倒排索引文件目录
- Elasticsearch 使用 Lucene 倒排索引作为底层实现

## 关联连接
- [[Elasticsearch]] — 使用倒排索引的搜索引擎
- [[Lucene]] — 底层倒排索引实现
- [[full-text-search]] — 全文搜索引擎概念
- [[摘要-elasticsearch-quick-start]] — 来源
