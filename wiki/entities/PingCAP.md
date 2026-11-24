---
title: "PingCAP"
type: entity
tags: [公司, 数据库, NewSQL, 开源]
sources: [raw/09-archive/2026-09-25 - 分库分表，可能真的要退出历史舞台了！.md, raw/09-archive/为什么越来越多人用 TiDB？.md]
last_updated: 2026-11-19
---

## 定义

PingCAP 是 [[TiDB]] 的自主设计与研发公司，由 [[黄东旭]] 等联合创始人创立，围绕 TiDB 提供开源社区版与收费企业版，并配套数据同步（Syncer）、迁移（分库分表 MySQL 实时迁移）、TiSpark 等工具链。

## 关键信息

- **核心产品**：TiDB（分布式 NewSQL 数据库），社区版免费、企业版提供服务与安全性支持
- **技术源流**：2012 年底受 Google F1/Spanner 论文启发立项，论文解决了关系型数据库 + 弹性扩展 + 全球分布的生产级难题
- **生态动作**：开源 TiSpark 补齐复杂 OLAP；提供 Syncer 把 TiDB 当作 MySQL Slave 接入现有主从架构
- **人物**：[[黄东旭]]（联合创始人 & CTO，开源分布式缓存 Codis 作者）
- **云服务与规模化验证（2026-11-19 补充）**：TiDB Cloud 已成为 AI Agent 的数据库基础设施——[[Kimi]]（Kimi.ai）用其为 Agent 提供 1 秒内创建隔离数据库的能力；Flipkart 用 TiDB on Kubernetes 做到每秒 100 万查询（详见 [[摘要-为什么越来越多人用tidb]]）；运维工具链有 TiUP 与 TiDB Operator（K8s Operator）

## 关联连接

- [[TiDB]] — 主力产品
- [[黄东旭]] — 联合创始人
- [[newsql]] — 所属品类
- [[摘要-tidb-newsql入门]] — 来源
- [[摘要-为什么越来越多人用tidb]] — 来源（TiDB Cloud AI Agent 基础设施案例与规模化验证）
