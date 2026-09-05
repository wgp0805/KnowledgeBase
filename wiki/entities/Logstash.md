---
title: "Logstash"
type: entity
tags: [数据同步, 日志, ELK]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
Logstash 是 Elastic Stack（ELK）中的数据收集引擎，支持多种输入源，能够对数据进行转换处理，并输出到 Elasticsearch 等目标。

## 关键信息
- **在 MySQL → ES 同步中的应用**：通过 JDBC Input 插件定时拉取 MySQL 数据，并写入 Elasticsearch
- **特点**：适合全量同步或定时增量同步，但实时性不如 Canal 或 Flink CDC
- **局限性**：基于轮询机制，无法实现真正的实时同步，且频繁查询可能对 MySQL 造成压力

## 关联连接
- [[Elasticsearch]] — 常见的数据同步目标
- [[MySQL]] — 数据源
- [[Canal]] — 实时数据同步工具
- [[Flink]] — 流处理数据同步工具
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）