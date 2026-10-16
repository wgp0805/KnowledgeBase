---
title: "摘要-mysql-9-7-lts"
type: source
tags: [来源, 原始文件, MySQL, LTS, 数据库]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 核心摘要

2026 年 4 月 21 日 Oracle 发布 MySQL 9.7.0 LTS（9.x 首个 LTS，5 年 Premier + 3 年 Extended Support），核心变化是**把一批企业版专属功能正式下放社区版**：Replication Applier Metrics（细粒度复制延迟指标）、Group Replication 流控统计/主选举/资源管理器、OpenTelemetry/OTLP 遥测、[[HypergraphOptimizer]]、[[JSONDualityViews]] DML、[[ProfileGuidedOptimization]]。三大收益：①复制可观测性——从粗糙的 `Seconds_Behind_Master` 升级到线程级指标，可直连 [[Prometheus]]；②超图优化器——用超图 + 动态规划替代传统左深树，改善多表 JOIN 执行计划（但 Percona 创始人 Peter Zaitsev 警告不保证更快，不要全局无脑开启）；③PGO——Percona 实测 32GB Buffer Pool 平均提速 12.2%，纯 CPU 层收益，不改配置不换硬件。**主要缺失**：`VECTOR` 类型有了，但相似度搜索函数 `DISTANCE()`/`VECTOR_DISTANCE()` 只在 Oracle 云的 HeatWave 中提供，社区版做 RAG 需用 [[Percona]] Server 9.7.2 的补丁实现或外接 [[向量数据库]]。作者结论：值得升级，但升级前先备份、跑兼容性测试、对比超图优化器开关前后的执行计划；写密集场景有退化风险，且 `innodb_log_file_size` 等旧变量已移除需调整配置。

## 关联连接

- [[MySQL]] — 主角数据库（+9.7 LTS 章节）
- [[Oracle]] — MySQL 出品方
- [[HypergraphOptimizer]] — 本文明细拆解的核心概念
- [[ProfileGuidedOptimization]] — 本文明细拆解的核心概念
- [[JSONDualityViews]] — 本文明细拆解的核心概念
- [[Percona]] — 第三方基准测试与补丁实现方
- [[HeatWave]] — 向量相似度函数的独占承载
- [[Prometheus]] — 复制指标的对接目标
- [[向量数据库]] — 社区版 RAG 的替代方案
- [[苏三]] — 作者
