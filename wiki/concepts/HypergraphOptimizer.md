---
title: "HypergraphOptimizer"
type: concept
tags: [数据库, 查询优化, MySQL, 执行计划]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 定义

Hypergraph Optimizer（超图优化器）是 [[MySQL]] 9.7 开放给社区版的查询优化器：把整个查询构建成一个**超图**，用动态规划搜索最优执行计划，替代传统优化器的"左深树"结构，用于改善多表关联、嵌套子查询场景下容易选错执行计划（全表扫描/错用索引）的问题。

## 关键信息

- 之前状态：仅企业版；MySQL 9.7 起社区版可用
- 开启方式：`SET optimizer_switch='hypergraph_optimizer=on';`
- **谨慎警告**：Percona 创始人 Peter Zaitsev 指出"新优化器不意味着你的 workload 一定更快，有时可能相反"；社区基准显示写密集场景可能退化
- 最佳实践：不要全局无脑开启，先在测试环境针对复杂 JOIN 场景做开启前后执行计划对比，确认提升再逐步铺开
- 升级提示：属于 MySQL 9.7 升级前三项必测内容之一（备份 → 兼容性测试 → 超图开关对比）

## 关联连接

- [[MySQL]] — 载体数据库
- [[摘要-mysql-9-7-lts]] — 来源
- [[Percona]] — 警告观点与基准测试提供方
- [[query-optimization]] — 上位概念：查询优化
