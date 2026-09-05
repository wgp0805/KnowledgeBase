---
title: "摘要-为什么越来越多人用opensearch"
type: source
tags: [来源, 原始文件, OpenSearch, 搜索引擎, 向量搜索, 读写分离]
sources: [raw/01-articles/为什么越来越多人用OpenSearch？.md]
last_updated: 2026-09-01
---

## 核心摘要
苏三《为什么越来越多人用OpenSearch？》拆解 OpenSearch 从"Elasticsearch fork"成长为独立开源搜索分析平台的演进。**起源**：2021年 Elastic 把 ES/Kibana 许可证从 Apache 2.0 改为 SSPL+ELv2，AWS fork ES 7.10.2 改名 OpenSearch；2024年9月 AWS 把治理权完全移交给 Linux 基金会，创始成员含 AWS/SAP/Uber/Aiven/Canonical；2024年8月 Elastic 又加 AGPLv3 第三选项。**架构**：五层抽象（集群/节点/索引/分片/文档），节点分数据节点/主节点/协调节点，搜索能力基于 Apache Lucene 倒排索引。**三大架构革新**：①**Segment Replication（段复制，2.7）**——只有主分片执行索引操作，生成段文件后直接复制给副本，副本不需重新索引，吞吐量提升/CPU 大幅节省/网络带宽换计算资源；②**读写分离（3.0）**——三种分片角色（Primary 唯一写入入口/Write Replica 冗余备份可提升为 Primary/Search Replica 专门服务搜索不可提升），Search Replica 只能分配到带 search 角色的节点实现硬件级物理隔离；③**9.5倍性能飞跃（3.0，2025年5月）**——升级 Lucene 10 + JVM 21 + 原生 gRPC + GPU 加速向量索引（9.3倍），相比 1.3 搜索查询性能提升 9.5 倍。**向量搜索**：k-NN 支持 Faiss/NMSLIB/Lucene 三引擎，差异化优势是混合搜索（BM25 关键词 + k-NN 语义）同时进行；3.8版本 Base64 向量编码让网络传输减少 74%，批量摄取吞吐量提升 4.16 倍。**生态**：累计下载 20亿+，活跃贡献者 3000+，贡献组织 400+；OpenSearch Dashboards/Data Prepper/PPL/MCP 服务器。**vs Elasticsearch 核心差异**：OpenSearch 给"全栈免费"+"架构确定性（Apache 2.0 永不变）"+"治理中立（Linux 基金会）"；ES 优势在搜索相关性迭代更快/Kibana 生态/已有商业订阅。

## 关联连接
- [[OpenSearch]] — 被解析的核心实体
- [[Elasticsearch]] — 对标产品
- [[SegmentReplication]] — 段复制特性
- [[ReadWriteSeparation]] — 读写分离架构
- [[HybridSearch]] — 混合搜索（关键词+向量）
- [[Lucene]] — 底层引擎
- [[InvertedIndex]] — 倒排索引
- [[摘要-es-为什么快-面试深度]] — ES 性能原理对比
- [[elasticsearch-disadvantages]] — ES 缺点分析
