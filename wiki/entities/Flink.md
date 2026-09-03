---
title: "Flink"
type: entity
tags: [流处理, 大数据, 数据同步]
sources: ["raw/01-articles/ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？.md"]
last_updated: 2026-09-02
---

## 定义
Apache Flink 是一个面向分布式数据流处理和批处理的开源计算框架，提供高吞吐、低延迟的流处理能力，支持事件时间处理和状态管理。

## 关键信息
- **Flink CDC**：基于数据库日志（如 MySQL binlog）的增量数据捕获技术，能够实时捕获数据库变更并同步到下游系统
- **在 MySQL → ES 同步中的应用**：作为 Canal 的替代方案，Flink CDC 可直接读取 MySQL binlog 并写入 Elasticsearch，实现近实时数据同步
- **优势**：相比 Canal，Flink CDC 提供更强大的状态管理和精确一次语义，适合复杂数据管道

## 关联连接
- [[Elasticsearch]] — 常见的数据同步目标
- [[MySQL]] — 数据源
- [[Canal]] — 同类数据同步工具
- [[摘要-es-data-types-mysql-mapping]] — 来源（ES 数据类型与 MySQL 映射）