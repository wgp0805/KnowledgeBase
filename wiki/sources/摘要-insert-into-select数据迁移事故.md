---
title: "摘要-insert-into-select数据迁移事故"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/同事使用 insert into select 迁移数据，开开心心上线，上线后被公司开除！.md]
last_updated: 2026-09-18
---

## 核心摘要
某公司同事使用 `INSERT INTO SELECT` 迁移支付流水表历史数据时，因未对 WHERE 条件字段加索引导致全表扫描，引发锁表。在默认事务隔离级别下，INSERT INTO A SELECT B 操作会锁住 A 表并逐条锁定 B 表记录，导致正常业务写入超时失败，近 10 万元支付流水丢失。测试环境未复现是因为缺少并发写入的真实业务场景。解决方案是对 WHERE 条件字段建立索引避免全表扫描。

## 关联连接
- [[INSERT-INTO-SELECT锁表]] — 核心概念
- [[MySQL]] — 数据库
- [[数据迁移]] — 操作场景
