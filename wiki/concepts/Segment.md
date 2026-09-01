---
title: "Segment"
type: concept
tags: [数据结构, 存储结构, Lucene, ElasticSearch]
sources: [raw/01-articles/2026-08-31 - 面试官：ElasticSearch 为什么快？.md]
last_updated: 2026-09-01
---

## 定义
Segment 是 Lucene 底层的不可变存储单元，每个 Segment 生成后不再修改（删除只是打标记）。ES 的索引由多个 Segment 组成，是不可变设计的核心。

## 关键信息
### 不可变设计带来的三大性能红利
- **读取无锁**：不可变数据天生线程安全，并发查询不需要任何锁竞争
- **压缩率高**：内容不变就能放心用激进的压缩算法，省下来的空间全是 IO
- **吃满 Page Cache**：不可变文件可以被操作系统放心缓存，热数据几乎全部驻留内存，查询基本不打磁盘

### Segment 生命周期
1. **refresh**（默认 1s）：内存 Buffer 生成新 Segment，进文件系统缓存（可搜索，未落盘）
2. **flush**（默认 30 分钟或 Translog 512MB）：Segment 真正 fsync 到磁盘，清空 Translog
3. **force merge**：多个小 Segment 合并成大的（查询提速，但吃资源，建议低峰期做）

### 更新和删除如何处理
- Segment 不可变，无法物理修改
- 删除：在 `.del` 文件中打标记记录删除的文档号，查询时过滤掉
- 更新：等价于"标记删除旧文档 + 写入新文档"
- 真正的物理删除要等 Segment 合并时才发生

## 关联连接
- [[DocValues]] — 存储在 Segment 中的列式结构
- [[InvertedIndex]] — 存储在 Segment 中的倒排索引
- [[NearRealTime]] — Segment 的 refresh 机制是 NRT 的来源
- [[Elasticsearch]] — 使用 Segment 的搜索引擎
- [[Lucene]] — Segment 的实现库
- [[摘要-es-为什么快-面试深度]] — 来源
