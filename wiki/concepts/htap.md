---
title: "htap"
type: concept
tags: [数据库, OLTP, OLAP, 架构]
sources: [raw/09-archive/2026-09-25 - 分库分表，可能真的要退出历史舞台了！.md]
last_updated: 2026-09-28
---

## 定义

HTAP（Hybrid Transactional and Analytical Processing，混合事务分析处理）指同时支持在线事务处理（OLTP）与在线分析处理（OLAP）的融合架构，目标是一份存储同时服务两类负载、免除传统繁琐的 ETL 过程。[[TiDB]] 是典型代表。

## 关键信息

### OLTP vs OLAP
| 维度 | OLTP | OLAP |
| --- | --- | --- |
| 实时性 | 高，单事务尽快处理 | 不高，常按天更新 |
| 数据量 | 读写数十条记录 | 聚合读取上百万条记录 |
| 面向 | 面向顾客，事务与查询 | 面向市场/决策，分析 |
| DB 设计 | 实体-联系 ER 模型、面向应用 | 星型/雪花模型、面向主题 |
| 工作单位 | 简单事务 | 复杂查询 |
| 评估指标 | 每秒 Transaction / SQL 数 | 磁盘子系统吞吐（MB/s） |
| 典型场景 | 银行存取款、电商交易 | 动态报表、时间序列分析 |

### HTAP 实现要点（TiDB 路线）
- 行存 TiKV 服务 OLTP、列存 TiFlash 服务 OLAP，两者可部署在不同机器实现资源隔离
- TiFlash 通过 Multi-Raft Learner 协议从 TiKV 实时复制，保证行/列存数据强一致
- 更复杂的分析交给 TiSpark（Spark SQL 直接跑在 TiDB 存储层）
- 设计目标：100% OLTP 场景 + 80% OLAP 场景

## 关联连接

- [[TiDB]] — HTAP 典型产品
- [[newsql]] — 所属数据库品类
- [[MySQL]] — 传统 OLTP 基线
- [[摘要-tidb-newsql入门]] — 来源
