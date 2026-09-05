---
title: "FST"
type: concept
tags: [数据结构, 倒排索引, Lucene, ElasticSearch]
sources: [raw/01-articles/2026-08-31 - 面试官：ElasticSearch 为什么快？.md]
last_updated: 2026-09-01
---

## 定义
FST（Finite State Transducer，有限状态转换器）是 Lucene 在 Term Index 层使用的前缀压缩数据结构，用于把海量词典的"目录页"装进内存，实现 O(查询词长度) 的词典定位。

## 关键信息
### 三大特点
- **前缀共享**：`cat`、`catalog`、`catalogue` 共用 `cat` 前缀，重复部分只存一份，压缩率极高
- **查询 O(len)**：时间复杂度只跟查询词长度有关，跟词典总量无关
- **内存占用小**：正是够小，Term Index 才能常驻堆内存

### 在 ES 词典查询中的位置
ES 词典查询拆三层：
1. **Term Index（内存）**：用 FST 只存 Term 前缀，定位目标 Term 所在磁盘块
2. **Term Dictionary（磁盘）**：真正有序的词典，通过 Term Index 直接定位，最少只需一次磁盘寻址
3. **Posting List**：拿到 Term 后获取对应文档 ID 列表

类比查字典：先翻目录（内存里的 FST）找页码，再翻到那一页（磁盘上的 Term Dictionary），最后看词条解释（Posting List）。

## 关联连接
- [[TermIndex]] — FST 所在的层
- [[InvertedIndex]] — 倒排索引整体结构
- [[Elasticsearch]] — 使用 FST 的搜索引擎
- [[Lucene]] — FST 的底层实现库
- [[摘要-es-为什么快-面试深度]] — 来源
