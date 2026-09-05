---
title: "ReadWriteSeparation"
type: concept
tags: [OpenSearch, 搜索引擎, 读写分离, 架构]
sources: [raw/01-articles/为什么越来越多人用OpenSearch？.md]
last_updated: 2026-09-01
---

## 定义
读写分离是 OpenSearch 3.0 引入的架构变革：通过三种分片角色（Primary/Write Replica/Search Replica）实现索引写入与搜索服务的物理隔离，写入负载仅由 Primary 处理，搜索负载由 Search Replica 专责服务。

## 关键信息
### 三种分片角色
| 角色 | 功能 | 特点 |
|------|------|------|
| Primary | 处理索引写入 | 唯一的写入入口 |
| Write Replica | 冗余备份 | Primary 故障时可提升为 Primary |
| Search Replica | 专门服务搜索 | **不可提升为 Primary**，只能分配到带 search 角色的节点 |

### 完整读写分离流程（启用远程存储后）
1. Primary 将段文件和事务日志写入远程存储
2. Write Replica 从远程存储拉取段文件
3. Search Replica 持续轮询远程存储，发现新段立即加载

### 核心价值
| 维度 | 传统模式 | 读写分离模式 |
|------|---------|------------|
| 写入负载 | Primary + Replica 都处理 | 仅 Primary 处理 |
| 搜索负载 | Primary + Replica 都处理 | Search Replica 专责 |
| 资源隔离 | 混合，相互影响 | 硬件级物理隔离 |
| 扩展方式 | 整体扩展 | 按需独立扩展 |

## 关联连接
- [[OpenSearch]] — 引入此架构的项目
- [[SegmentReplication]] — 读写分离的基础
- [[Elasticsearch]] — 对比产品（无此能力）
- [[摘要-为什么越来越多人用opensearch]] — 来源
