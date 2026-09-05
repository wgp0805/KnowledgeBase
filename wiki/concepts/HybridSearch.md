---
title: "HybridSearch"
type: concept
tags: [搜索引擎, 向量搜索, 混合搜索, OpenSearch]
sources: [raw/01-articles/为什么越来越多人用OpenSearch？.md]
last_updated: 2026-09-01
---

## 定义
混合搜索（Hybrid Search）是 OpenSearch 的差异化优势：关键词搜索（BM25）+ 语义搜索（向量 k-NN）同时进行，BM25 捕捉精确关键词匹配，k-NN 捕捉语义相似性，两者互补，需归一化后组合。

## 关键信息
### 为什么需要混合搜索
- BM25 返回的分数是无界的
- k-NN 返回 [0,1] 区间
- 需要归一化后才能组合

### 适用场景
需要同时兼顾关键词匹配和语义理解的复杂查询中特别有效：
- BM25 捕捉精确关键词匹配
- k-NN 捕捉语义相似性
- 两者互补

### OpenSearch 向量搜索能力
- **k-NN（k-Nearest Neighbors）**：支持近似 k-NN（ANN，牺牲少量精度换大幅性能，默认推荐）、精确搜索（暴力全量比对，适合小数据集）、Painless 扩展
- **三种引擎**：Faiss、NMSLIB、Lucene
- **3.8 优化**：Base64 向量编码（768维 float 从 16KB→4KB，网络传输减少 74%），批量摄取吞吐量提升 4.16 倍

## 关联连接
- [[OpenSearch]] — 提供混合搜索的项目
- [[Elasticsearch]] — 也支持混合搜索
- [[BM25]] — 关键词搜索评分算法
- [[RAG]] — 混合搜索是 RAG 检索的重要能力
- [[摘要-为什么越来越多人用opensearch]] — 来源
