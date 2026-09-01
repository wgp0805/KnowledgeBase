---
title: "Lucene"
type: entity
tags: [搜索引擎, 全文检索, Java, Apache]
sources:
  - raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md
  - raw/01-articles/拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？.md
last_updated: 2026-08-26
---

## 定义

Lucene 是 Apache 软件基金会旗下的开放源代码全文检索引擎工具包，用 Java 开发。它不是一个完整的全文检索引擎，而是一个提供了完整查询引擎和索引引擎的架构，被认为是目前最先进、性能最好、功能最全的搜索引擎库。

## 关键信息

- 提供简单但强大的应用程序接口（API），用于全文索引和搜索
- 仅是一个库，需用 Java 直接集成到应用中，使用门槛较高
- Elasticsearch 使用 Lucene 作为核心实现索引和搜索功能，通过 RESTful API 隐藏其复杂性
- 一个 ES 分片就是一个 Lucene 索引（包含倒排索引的文件目录）
- **segment 是 Lucene 最小索引单元**，不可变。ES refresh（默认 1s）将内存 buffer 生成新 segment 使数据可搜索；flush 将 segment 持久化到磁盘
- **FST（Finite State Transducer）压缩**：Lucene 在词条字典之上使用 FST 压缩存储，海量词条能常驻内存，查询极快
- **更新代价**：segment 不可变导致更新实际是"标记删除 + 新写入"，写放大严重，不适合频繁更新场景

## 关联连接
- [[Elasticsearch]] — 基于 Lucene 的分布式搜索引擎
- [[Solr]] — 同样基于 Lucene 的搜索服务器
- [[inverted-index]] — Lucene 底层核心数据结构
- [[摘要-elasticsearch-quick-start]] — 来源
- [[摘要-拼多多二面-es-vs-mysql]] — 来源（segment/FST/倒排索引原理）
- [[InvertedIndex]] — 倒排索引概念页
- [[NearRealTime]] — 近实时机制（segment 生成流程）
