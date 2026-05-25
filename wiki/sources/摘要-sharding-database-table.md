---
title: "摘要-sharding-database-table"
type: source
tags: [分库分表, 数据库优化, Sharding-JDBC, 面试]
sources: [raw/01-articles/从40分钟到1秒：我用分库分表彻底解决了上亿数据的大表性能问题！！.md]
last_updated: 2026-05-25
---

## 核心摘要

本文讲解大数据量场景下分库分表的原理、三大坑点和落地实践。分库分表的核心思想是"分而治之"：水平分表按行拆（如按时间）、垂直分表按列拆、分库将压力分散到多个数据库实例。三大坑点：分片键选错导致数据倾斜、跨分片查询性能差、分布式事务一致性问题。落地实践推荐Sharding-JDBC中间件，采用双写+灰度切换的平滑迁移方案。启动红线：单表>1000万且查询>500ms、QPS>2000且连接数打满、预计6个月内数据翻倍。

## 关联连接
- [[ShardingSphere]] — 分布式数据库中间件
- [[MySQL]] — 关系型数据库
- [[consistent-hashing]] — 一致性哈希算法
- [[distributed-lock]] — 分布式锁机制
