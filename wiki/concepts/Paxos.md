---
title: "Paxos"
type: concept
tags:
  - 分布式
  - 共识算法
sources: [raw/01-articles/2026-09-23 - 分库分表，可能真的要退出历史舞台了！.md]
last_updated: 2026-09-28
---

## 定义
经典分布式共识算法（Lamport 1990）：通过 Prepare/Promise/Accept 两阶段协议，在多数派存活时选出唯一值，是 Raft 等后续算法的前身。

## 关键信息
### 工程化要点（来自 [[摘要-分库分表vs-newsql对比]]）
- 算法本身不难，但生产级实现要考虑大量异常并做很多优化，实际必须转化为 `multi-paxos` / `multi-raft`
- 需要 batch、异步等方式减少网络与磁盘 IO 开销
- 采用过半写原则、支持自动选主：缩短 failover 时间、减少运维工作量，已成 NewSQL 数据库底层标配（Spanner、TiDB、CockroachDB、OceanBase）
- 传统关系库也能改造：阿里、微信团队改造 MySQL 存储支持 Paxos 多副本，MySQL 官方推出 Group Replication，主从模式可能逐渐成为历史

### 异地多活的前提
基于 Paxos/Raft 宣称的"异地多活"有硬前提：**异地间网络延迟不能太高**。银行"两地三中心"相隔数千里、时延达数十毫秒，若异地副本参与日志过半确认，几乎没有 OLTP 系统能接受。更现实的是应用层方案（如蚂蚁：MQ 同步双写交易信息 + 缓存 + 切换后黑名单管理，追平后再解除）。

## 关联连接
- [[Raft]]
- [[分布式]]
- [[高可用]]
- [[冷备暖备热备]]
- [[newsql]] — 多副本共识是其高可用底座
- [[分布式事务]] — 事务与共识的协同
- [[摘要-分库分表vs-newsql对比]] — 来源
