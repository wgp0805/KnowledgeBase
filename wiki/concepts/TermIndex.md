---
title: "TermIndex"
type: concept
tags: [Elasticsearch, 索引, 数据结构]
sources: [raw/01-articles/2026-09-05 - 面试官：倒排索引是什么？.md]
last_updated: 2026-09-05
---

## 定义
Term Index（词条索引）是倒排索引三层结构的顶层，使用 FST（Finite State Transducer，有限状态转换器）对词条做前缀索引，体积小到可以常驻内存，作用类似词典的"目录"，告诉你某个前缀在磁盘词典的哪个块里。

## 关键信息
- FST：前缀树（Trie）的极致压缩版，用极小内存共享前缀和后缀
- 能把"词→块地址"的映射直接编码在状态转移里
- 典型设计："内存放目录、磁盘放数据"
- 与 MySQL B+树三层结构思想相通，但实现完全不同

## 关联连接
- [[InvertedIndex]] — 倒排索引核心概念
- [[TermDictionary]] — 磁盘词条字典
- [[PostingList]] — 倒排列表
- [[FST]] — 有限状态转换器
- [[Elasticsearch]] — 全文检索引擎
- [[Lucene]] — 底层检索库
- [[摘要-倒排索引面试题]] — 来源
