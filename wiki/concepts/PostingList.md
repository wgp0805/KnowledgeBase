---
title: "PostingList"
type: concept
tags: [Elasticsearch, 索引, 数据结构]
sources: [raw/01-articles/2026-09-05 - 面试官：倒排索引是什么？.md]
last_updated: 2026-09-05
---

## 定义
Posting List（倒排列表）是倒排索引三层结构的底层，存储每个词条对应的文档信息列表，包含文档ID、词频（TF）、位置（Position，用于短语匹配）、偏移（Offset，用于高亮）。

## 关键信息
- 压缩技术：
  - FOR压缩（Frame of Reference）：文档ID递增，存差值+位压缩
  - Roaring Bitmaps：跳跃数组+位图，用于filter查询缓存
- ES filter 查询特别快的原因：对多个有序文档ID列表做高效集合运算
- 动辄几百万个文档ID，压缩技术是性能关键

## 关联连接
- [[InvertedIndex]] — 倒排索引核心概念
- [[TermIndex]] — FST 前缀索引
- [[TermDictionary]] — 有序词条字典
- [[FOR压缩]] — Frame of Reference 压缩
- [[RoaringBitmaps]] — 位图压缩
- [[Elasticsearch]] — 全文检索引擎
- [[摘要-倒排索引面试题]] — 来源
