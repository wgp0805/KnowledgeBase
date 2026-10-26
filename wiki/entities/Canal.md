---
title: "Canal"
type: entity
tags: [数据同步, MySQL, binlog, 中间件]
sources:
  - raw/09-archive/得物二面：分库分表后，怎么进行分页查询？我被问懵了.md
  - raw/09-archive/拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？.md
  - raw/09-archive/滴滴二面：怎么保证 ElasticSearch 和数据库的数据一致性？.md
last_updated: 2026-09-18
---

## 定义
Canal 是阿里巴巴开源的一款基于 MySQL binlog 的增量数据同步工具，能够实时捕获 MySQL 数据库的变更事件（插入、更新、删除），并将这些变更投递到下游系统（如 Elasticsearch、Kafka、HBase 等）。

## 关键信息
- **工作原理**：模拟 MySQL Slave 的交互协议，伪装自己为 Slave 向 Master 发送 dump 请求，接收 binlog 变更流
- **典型用途**：
  - 异构索引数据同步：MySQL → Canal → Kafka → Elasticsearch，构建 ES 查询层
  - 数据迁移与双写：数据库扩容时通过 Canal 实现灰度切换
- **在分库分表架构中的角色**：异构索引方案的关键链路组件，负责将 MySQL 分片的 binlog 变更实时同步到 ES，使 ES 成为查询层的"真实数据源"
- **生产标准架构**：MySQL（Source of Truth）→ Canal 监听 Binlog → MQ（削峰 + 失败重试）→ 消费写入 ES。业务代码与同步逻辑解耦，保证最终一致性。双写方案（业务代码同时写 MySQL 和 ES）耦合高、无事务保障，不推荐
- **版本号防乱序**：配合 ES 外部版本控制（`VersionType.EXTERNAL_GTE`），每条数据带单调递增版本号，旧版本消息到达时 ES 自动拒绝，实现"免疫"而非"预防"
- **与 Debezium 对比**：国外用 Debezium + Kafka 居多，思路相同，均为 CDC（Change Data Capture）工具

## 关联连接
- [[摘要-分库分表分页查询]] — 来源
- [[异构索引]] — Canal 是异构索引架构的核心组件
- [[Elasticsearch]] — 常见的下游数据同步目标
- [[Kafka]] — 常见的 Canal 投递中间件
- [[MySQL]] — 数据源
- [[sharding]] — 分库分表架构
- [[摘要-拼多多二面-es-vs-mysql]] — 来源（生产架构标准答案）
- [[摘要-滴滴二面-es数据一致性]] — 来源（ES 数据一致性方案演进）
- [[NearRealTime]] — ES 近实时机制（同步延迟考量）
