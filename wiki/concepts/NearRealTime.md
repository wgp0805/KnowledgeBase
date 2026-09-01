---
title: "NearRealTime"
type: concept
tags: [实时性, 搜索引擎, Elasticsearch, 写入机制]
sources: [raw/01-articles/拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？.md]
last_updated: 2026-08-26
---

## 定义

近实时（Near Real-Time, NRT）是 Elasticsearch 的写入特性：数据写入后并非立即可搜索，默认约有 1 秒延迟。这与 MySQL 事务提交后数据立即可查的"实时"机制形成鲜明对比。

## 关键信息

### ES 写入三步流程
1. **写内存**：数据先进入 `index buffer`（内存缓冲区），同时把操作记录追加到 `translog`（类似 MySQL 的 redo log，用于宕机恢复）。此时数据 **搜不到**。
2. **refresh（默认 1 秒）**：缓冲区数据生成一个新的 segment（Lucene 最小索引单元），数据变成可搜索状态。这就是"近实时"的由来。
3. **flush**：segment 持久化到磁盘，`translog` 清空。

### 与 MySQL 实时性对比
| 维度 | MySQL | ES |
|------|-------|-----|
| 写入可见性 | 事务提交立即可查 | 默认 1 秒延迟后可搜索 |
| 事务 | ACID 强事务 | 无真正 ACID，跨文档无法回滚 |
| 持久性 | redo log 保证 | translog 保证 |

### 调优注意
`refresh_interval` 可调小以缩短延迟，但调太小会让 segment 过多，反而拖垮性能。

### translog 刷盘策略
通过 `index.translog.durability` 参数控制，是面试常见追问方向。

## 关联连接
- [[Elasticsearch]] — 近实时机制的载体
- [[Lucene]] — segment 是 Lucene 的最小索引单元
- [[MySQL]] — 实时性对比对象
- [[摘要-拼多多二面-es-vs-mysql]] — 来源
