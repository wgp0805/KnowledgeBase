---
title: "摘要-为什么越来越多人用tidb"
type: source
tags: [来源, 数据库, 分布式, TiDB, HTAP]
sources: [raw/09-archive/为什么越来越多人用 TiDB？.md]
last_updated: 2026-11-19
---

## 核心摘要
苏三 2026-11-19 文章，回答"数据量涨到几个亿、单表变慢，除了分库分表还能怎么办"——用 [[TiDB]]。核心论点：**分库分表是你在应用层"模拟"分布式，TiDB 是数据库本身"就是"分布式**——把分布式从应用层收回数据库层，不用管分片规则，加机器即扩容，跨库 JOIN 直接写，分析查询和交易查询跑在同一个入口（HTAP）。文章覆盖三层架构、Region 自动分片、Raft 强一致、从 MySQL 迁移的实操要点、用 AI 分析慢查询的工作流、优缺点与适用场景表。

## 关键要点
- **三层架构**：计算层 TiDB Server（无状态 SQL 引擎，加机器提升算力不停机）+ 存储层 TiKV（行存，OLTP）/TiFlash（列存，OLAP，经 Raft Learner 实时同步强一致）+ 调度层 PD（元数据、负载均衡、时间戳分配、Region 调度）
- **Region 自动分片**：数据按 Key 范围切 Region（默认约 96MB），变大变热由 PD 自动分裂并调度迁移，无需预判"该分几片"；扩容即加 TiKV 节点，数据自动均衡
- **Raft 强一致**：每 Region 3 副本，Leader 写 + Follower 同步，多数派（2 个）确认才算成功；Leader 挂自动重选，RTO 秒级，无需 MHA/主从切换脚本
- **HTAP 是拉开差距的关键**：分库分表后做实时分析要同步到 Hive/ClickHouse 走 T+1（链路越长一致性越难保证）；TiDB 优化器自动路由——OLTP 走 TiKV、OLAP 走 TiFlash；擎文集团案例：MySQL 分库分表 + Hive T+1 → 一套 TiDB 同时支撑在线业务与实时分析
- **迁移三要点**：① 连接串端口 3306→4000，JDBC 驱动/连接池/大部分 SQL 语法不变；② 建表注意 `AUTO_INCREMENT` 的坑——表无显式主键时 `_tidb_rowid` 与自增列共用分配器可能跳号，大写入量表建议显式主键 + `AUTO_RANDOM`（TiDB 特有，打散自增主键写入热点）；③ 跨库 JOIN 直接写，TiDB 自己决定怎么拆怎么算怎么合并
- **AI 辅助慢查询分析**：TiDB 慢查询日志是结构化的——把慢查询日志 + EXPLAIN 结果喂给 AI 分析"为什么没走索引、该加什么索引"（如联合索引 `(status, created_at)`）；AI 会提醒 TiDB DDL 在线不锁表但耗资源建议低峰执行、区分度低可用部分索引（partial index）；**AI 不能替你判断"索引到底该不该加"——AI 帮你理解执行计划，你来做权衡**
- **优点**：免分库分表、MySQL 兼容迁移成本低、HTAP 一套两负载、金融级高可用（Raft 多副本 RTO 秒级零丢失）、在线 DDL 不锁表、大厂验证（Kimi.ai 用 TiDB Cloud 为 AI Agent 提供 1 秒创建隔离库的基础设施；Flipkart 用 TiDB on Kubernetes 每秒 100 万查询）
- **缺点**：非 100% 兼容 MySQL（存储过程/触发器/事件/自定义函数/全文索引/空间数据类型不支持）；运维模型不同（需懂 PD/Region/Raft，有 TiUP 和 TiDB Operator 简化但学习成本在）；自增主键写入热点需 AUTO_RANDOM 处理；分布式最小部署资源消耗高——小数据量低并发不划算
- **适用场景**：数据量大分库分表运维痛苦 ✅✅✅ / 需要 HTAP ✅✅✅ / 金融级高可用 ✅✅✅ / AI Agent 数据库基础设施 ✅✅✅ / 依赖存储过程触发器全文索引 ⚠️ / 小数据量低并发 ❌

## 关联连接
- [[TiDB]] — 文章主角
- [[PingCAP]] — 开发商
- [[htap]] — 拉开差距的核心能力（行存列存双引擎）
- [[Raft]] — 强一致与高可用的基础协议
- [[sharding]] — 被替代的传统方案（分库分表）
- [[ShardingSphere]] — 文中引入的分库分表中间件（痛点来源）
- [[MySQL]] — 迁移来源与兼容对象
- [[苏三]] — 作者
