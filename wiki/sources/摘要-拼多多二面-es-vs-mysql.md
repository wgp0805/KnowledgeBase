---
title: "摘要-拼多多二面-es-vs-mysql"
type: source
tags: [来源, 原始文件, 面试题, Java, Elasticsearch, MySQL]
sources: [raw/01-articles/ƴ�����棺ΪʲôҪʹ�� ElasticSearch���ʹ�ͳ��ϵ���ݿ� MySQL ��ʲô��ͬ��.md]
last_updated: 2026-08-28
---

## 核心摘要
本文以拼多多二面题目"为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？"为切入点，系统对比 MySQL B+Tree 与 ES 倒排索引的核心差异，深度解析全文检索、多条件组合查询、相关性打分、聚合分析、近实时写入等场景下 ES 的优势，并详细阐述 MySQL + ES 双库架构的生产落地方案：MySQL 作为源头主存储，通过 Canal 监听 Binlog 同步至 ES，实现事务数据与检索数据的最终一致性。文章还涵盖 ES 写入流程、refresh/flush/merge 机制、分页深度限制、ES 不适用场景（事务、Join、频繁更新、小数据量）等工程实战要点。

## 关联连接
- [[Elasticsearch]] — 分布式全文检索引擎
- [[MySQL]] — 关系型数据库
- [[Lucene]] — ES 底层搜索库
- [[Canal]] — MySQL Binlog 同步工具
- [[BM25]] — ES 5.0+ 默认相关性算法
- [[FST]] — Lucene 词典压缩结构
- [[InvertedIndex]] — 倒排索引核心数据结构
- [[BPlusTree]] — MySQL 索引底层结构
- [[NearRealTime]] — 近实时写入特性
- [[SegmentMerge]] — ES 段合并机制
- [[DualWriteArchitecture]] — MySQL+ES 双写架构
- [[FullTextSearch]] — 全文检索能力