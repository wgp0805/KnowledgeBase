---
title: "摘要-tidb-newsql入门"
type: source
tags: [来源, 原始文件, TiDB, NewSQL, 分布式数据库]
sources: [raw/01-articles/2026-09-25 - 分库分表，可能真的要退出历史舞台了！.md]
last_updated: 2026-09-28
---

## 核心摘要

本文从数据库三代演进（SQL → NoSQL → NewSQL）切入，解释传统关系库在海量高并发下靠升级硬件有天花板、靠分片中间件又受跨库 join/事务困扰，而 NoSQL 放弃强一致性与 SQL 兼容，NewSQL 则把 NoSQL 的可扩展性与关系模型、ACID、标准 SQL 结合起来。主体是 TiDB 全景介绍：PingCAP 黄东旭受 Google F1/Spanner 论文启发于 2012 年底开始打造，架构由无状态的 TiDB Server、负责元信息/调度/全局事务 ID 的 PD、基于 Region + Multi-Raft 存储的 TiKV，以及面向 OLAP 的 TiFlash（列存）与 TiSpark 组成，提供水平弹性扩展、100% ACID、金融级高可用、实时 HTAP、云原生与 MySQL 5.7 高度兼容。文章列出四类应用场景（MySQL 分片合并、直接替换 MySQL、充当数据仓库、作为底层 KV 模块）以及 TiDB 相对 MySQL 的兼容差异清单（不支持存储过程/触发器/外键/临时表/XA 语法等，自增 ID 不保证多 server 连续，视图不可写）。另附 OLTP 与 OLAP 在实时性、数据量、面向对象、库设计上的对照表。

## 关联连接

- [[TiDB]] — 文章主体产品
- [[PingCAP]] — TiDB 的开发商
- [[黄东旭]] — TiDB 作者、PingCAP 联合创始人
- [[newsql]] — 概念背景与三代演进
- [[htap]] — TiDB 的混合负载定位
- [[Raft]] — Multi-Raft 多副本共识
- [[MySQL]] — TiDB 兼容与替换对象
- [[sharding]] — TiDB 试图替代的分库分表方案
- [[分布式事务]] — TiKV 两阶段提交
- [[摘要-分库分表vs-newsql对比]] — 同题文章的选型对比篇
