---
title: "摘要-分库分表vs-newsql对比"
type: source
tags: [来源, 原始文件, 分库分表, NewSQL, 数据库架构]
sources: [raw/01-articles/2026-09-23 - 分库分表，可能真的要退出历史舞台了！.md]
last_updated: 2026-09-28
---

## 核心摘要

本文客观对比"中间件+传统关系数据库分库分表"与"新架构 NewSQL 分布式数据库"两条路线，反对脱离场景地贬低任一方：按 Pavlo 的 NewSQL 综述分类，Spanner/TiDB/OceanBase 属于新架构型，ShardingSphere/Mycat/DRDS 属于中间件型，后者虽在 SQL 解析执行重复、B+Tree 存储等方面被称"伪分布式"，但存储确实分布、可横向扩展。分布式事务是双刃剑——NewSQL 并未突破 CAP（Spanner 的"实际上是 CA"依赖私有全球网与高效运维），2PC 的 GID 获取、网络开销与 prepare 日志持久化仍显著拖累性能，Percolator（原子钟+MVCC+Snapshot Isolation）比 XA 强但仍有点锁与写倾斜问题，大规模高并发 OLTP 更建议 Saga/TCC/可靠消息等柔性事务。HA 上基于 Paxos/Raft 的多副本是 NewSQL 标配（MySQL Group Replication 也能补课），但异地多活受异地时延硬约束，蚂蚁的应用层 MQ 双写+黑名单方案更现实。文章给出两组各六七个自测问题作为选型清单，结论是：NewSQL 是方向但非银弹，分库分表"上限低、下限高"，对传统行业核心系统仍是稳妥选择。

## 关联连接

- [[sharding]] — 分库分表概念本体，本文为其选型对照的另一极
- [[newsql]] — 本文的核心讨论对象
- [[分布式事务]] — 2PC/XA 与柔性事务的详细展开
- [[CAP理论]] — NewSQL 并未突破 CAP 限制
- [[Paxos]] — 多副本高可用与异地多活前提
- [[Raft]] — 与 Paxos 同类的共识协议
- [[MVCC]] — Percolator 事务模型的组成部分
- [[ShardingSphere]] — 中间件型方案代表
- [[Mycat]] — 中间件型方案代表
- [[MySQL]] — 传统关系数据库基线
- [[TiDB]] — 新架构型 NewSQL 代表
- [[摘要-sharding-database-table]] — 分库分表实操篇来源
