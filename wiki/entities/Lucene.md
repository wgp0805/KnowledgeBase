---
title: "Lucene"
type: entity
tags: [搜索引擎, 全文检索, Java, Apache]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

Lucene 是 Apache 软件基金会旗下的开放源代码全文检索引擎工具包，用 Java 开发。它不是一个完整的全文检索引擎，而是一个提供了完整查询引擎和索引引擎的架构，被认为是目前最先进、性能最好、功能最全的搜索引擎库。

## 关键信息

- 提供简单但强大的应用程序接口（API），用于全文索引和搜索
- 仅是一个库，需用 Java 直接集成到应用中，使用门槛较高
- Elasticsearch 使用 Lucene 作为核心实现索引和搜索功能，通过 RESTful API 隐藏其复杂性
- 一个 ES 分片就是一个 Lucene 索引（包含倒排索引的文件目录）

## 关联连接
- [[Elasticsearch]] — 基于 Lucene 的分布式搜索引擎
- [[Solr]] — 同样基于 Lucene 的搜索服务器
- [[inverted-index]] — Lucene 底层核心数据结构
- [[摘要-elasticsearch-quick-start]] — 来源
