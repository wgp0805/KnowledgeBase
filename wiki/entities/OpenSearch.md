---
title: "OpenSearch"
type: entity
tags: [搜索引擎, 全文检索, 分布式, 开源, 向量搜索, Linux基金会]
sources: [raw/01-articles/为什么越来越多人用OpenSearch？.md]
last_updated: 2026-09-01
---

## 定义
OpenSearch 是一个由 Linux 基金会托管的、Apache 2.0 协议的开源搜索与分析平台，起源于 2021 年 AWS 从 Elasticsearch 7.10.2 fork 的分支，现已发展为独立项目。累计下载量突破 20 亿次，活跃贡献者超过 3000 人。

## 关键信息
### 起源与治理
- **2021年1月**：Elastic 把 ES/Kibana 许可证从 Apache 2.0 改为 SSPL + Elastic License v2 双重授权
- **2021年7月**：AWS fork ES 7.10.2（最后一个 Apache 2.0 版本），OpenSearch 1.0 发布
- **2024年9月**：AWS 把治理权完全移交给 Linux 基金会，成立 OpenSearch 软件基金会（创始成员：AWS/SAP/Uber/Aiven/Canonical）
- **2024年8月**：Elastic 在 SSPL/ELv2 基础上加 AGPLv3 第三选项（网络使用即分发条款）

### 架构（五层抽象）
- **集群（Cluster）→ 节点（Node）→ 索引（Index）→ 分片（Shard）→ 文档（Document）**
- 节点类型：数据节点（存储/摄取/搜索/聚合）、主节点（集群管理）、协调节点（路由）
- 搜索能力基于 [[Lucene]] [[InvertedIndex]]

### 三大架构革新
**① Segment Replication（段复制，2.7 引入）**
- 传统文档复制：每个副本分片都要重新执行完整索引操作，写入压力随副本数线性增长
- 段复制：只有主分片执行索引操作，生成 Lucene 段文件后直接复制给所有副本
- 收益：索引吞吐量提升、CPU 大幅节省、网络带宽换计算资源

**② 读写分离（3.0 引入）**
- 三种分片角色：Primary（唯一写入入口）/ Write Replica（冗余备份，可提升为 Primary）/ Search Replica（专门服务搜索，不可提升为 Primary）
- Search Replica 只能分配到带 search 角色的节点，实现硬件级物理隔离
- 启用远程存储后：Primary 写段文件和事务日志到远程存储 → Write Replica 拉取 → Search Replica 轮询加载

**③ 9.5 倍性能飞跃（3.0，2025年5月）**
- 升级 Apache Lucene 10（SIMD 向量化 + 改进 I/O）
- 升级 JVM 21
- 原生 gRPC 支持（HTTP/2 多路复用）
- GPU 加速向量索引（索引构建速度提升 9.3 倍）
- 相比 1.3：搜索查询性能提升 9.5 倍；相比 2.19：高影响操作平均提升 20%

### 向量搜索
- **k-NN（k-Nearest Neighbors）**：支持近似 k-NN（ANN，默认推荐）、精确搜索、Painless 扩展
- **三种引擎**：Faiss、NMSLIB、Lucene
- **[[HybridSearch]]（混合搜索）**：BM25 关键词 + k-NN 语义同时进行，需归一化后组合
- **3.8 版本优化（2026年8月）**：Base64 向量编码（768维 float 从 16KB→4KB，网络传输减少 74%），批量摄取吞吐量提升 4.16 倍，中位延迟降低 83%；径向搜索吞吐量提升 2.1 倍，召回率从 0.85→0.97

### 生态
| 指标 | 数据 |
|------|------|
| 累计下载量 | 20亿+ |
| Linux 基金会托管后增长 | 7亿→14亿→20亿 |
| 活跃贡献者 | 3000+ |
| 贡献组织 | 400+ |
| 公共仓库 | 140+ |

生态组件：OpenSearch Dashboards（可视化）、Data Prepper（数据摄取管道）、PPL（日志分析查询语言）、MCP 服务器（与 AI Agent 集成）

### vs Elasticsearch 核心差异
| 维度 | OpenSearch | Elasticsearch |
|------|-----------|--------------|
| 许可证 | Apache 2.0 | AGPLv3/ELv2/SSPL 三重 |
| 治理 | Linux 基金会 | Elastic N.V. |
| 安全功能 | 全部免费 | 基础免费，高级付费 |
| GPU 加速 | ✅ 索引加速 9.3 倍 | 有限支持 |
| gRPC | ✅ 原生 | ❌ |
| 读写分离 | ✅ 3.0 原生 | ❌ |
| MCP 协议 | ✅ 3.0 原生 | ❌ |
| 搜索相关性迭代 | 一般 | 更快 |
| Kibana 生态 | OpenSearch Dashboards 有学习成本 | 深度绑定 |

**核心差异三句话**：OpenSearch 给"全栈免费"+"架构确定性（Apache 2.0 永不变）"+"治理中立（不会被任何公司绑架）"

### 适用场景
- 对开源许可证敏感的企业（Apache 2.0 完全开源）
- 日志分析/可观测性（全栈免费，PPL 强大）
- SIEM/安全分析（安全/告警/异常检测全免费）
- RAG/向量检索（混合搜索+向量检索，GigaOm 领导者）
- AWS 云原生应用

## 关联连接
- [[Elasticsearch]] — 对标产品，同源分支
- [[Lucene]] — 底层引擎
- [[InvertedIndex]] — 倒排索引核心结构
- [[SegmentReplication]] — 段复制特性
- [[ReadWriteSeparation]] — 读写分离架构
- [[HybridSearch]] — 混合搜索
- [[Kibana]] — 对标的可视化工具（OpenSearch Dashboards）
- [[摘要-为什么越来越多人用opensearch]] — 来源
- [[摘要-es-为什么快-面试深度]] — ES 性能原理对比
- [[elasticsearch-disadvantages]] — ES 缺点分析
