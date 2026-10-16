---
title: "Percona"
type: entity
tags: [数据库, 公司, 开源, MySQL]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 定义

Percona 是围绕 MySQL 生态的开源数据库软件公司与产品品牌，提供 MySQL 发行版、工具链与性能基准测试，是 MySQL 社区版能力边界的"补位者"与权威评测方。

## 关键信息

- **创始人**：Peter Zaitsev，对 [[MySQL]] 9.7 [[HypergraphOptimizer]] 给出清醒判断："新优化器并不意味着你的 workload 一定更快，有时候可能相反"
- **Percona Server for MySQL**：9.7.2 版本自行实现并补上了 `DISTANCE()` 向量相似度函数，支持 COSINE、EUCLIDEAN、MANHATTAN、DOT 等度量——弥补了社区版"能存 [[向量数据库]] 数据、不能做相似度搜索"的缺失（但非 Oracle 官方方案）
- **PGO 基准测试**：对 MySQL 9.7 的 [[ProfileGuidedOptimization]] 做了严谨对比（32GB Buffer Pool 平均提升 12.2%）
- **工具链**：PT-OSC（在线表结构变更工具，见 [[PT-OSC]]）

## 关联连接

- [[MySQL]] — 生态核心数据库
- [[摘要-mysql-9-7-lts]] — 来源
- [[HypergraphOptimizer]] — 创始人评论对象
- [[ProfileGuidedOptimization]] — 基准测试对象
- [[HeatWave]] — 向量函数缺失时的对照方案
- [[PT-OSC]] — 旗下在线 DDL 工具
