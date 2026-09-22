---
title: "摘要-insert-into-select迁移数据事故"
type: source
tags: [来源, MySQL, 数据迁移, 事故]
sources: [raw/01-articles/2026-09-20 - 同事使用 insert into select 迁移数据，开开心心上线，上线后被公司开除！.md]
last_updated: 2026-09-22
---

## 核心摘要
同事使用INSERT INTO SELECT迁移MySQL百万级支付流水数据，因WHERE条件未加索引导致全表扫描，执行期间锁住目标表，新写入的支付流水因拿不到锁而超时失败，最终丢失约10万元流水。测试环境无法复现是因为缺少并发写入场景。根因：INSERT INTO SELECT对目标表直接锁表、对源表逐条加锁，全表扫描放大锁持有时间。解决：对WHERE字段加索引避免全表扫描。

## 关联连接
- [[INSERT-INTO-SELECT锁表]] — 已有概念页面，增量更新
- [[MySQL]] — 数据库
- [[全表扫描]] — SQL执行计划
- [[索引优化]] — 避免全表扫描
- [[事务隔离级别]] — 锁机制
