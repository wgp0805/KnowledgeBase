---
title: "HeatWave"
type: entity
tags: [数据库, Oracle云, MySQL, 向量搜索]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 定义

HeatWave MySQL 是 Oracle 云上托管的 MySQL 版本，独占了 [[MySQL]] 9.7 的向量相似度搜索能力——关键的 `DISTANCE()` 和 `VECTOR_DISTANCE()` 函数**只在 HeatWave 中提供**，社区版和企业版本地部署均不包含。

## 关键信息

- MySQL 9.7 引入 `VECTOR` 数据类型与 `TO_VECTOR()`/`FROM_VECTOR()` 函数，本地部署版本可**存储向量**
- 但相似度搜索函数被锁定在 HeatWave，导致本地部署做 [[RAG]] 时"**可以在 MySQL 里存向量，但没法用 SQL 做向量相似度搜索**"
- 替代方案：①用 [[Percona]] Server for MySQL 9.7.2 的 `DISTANCE()` 实现（支持 COSINE/EUCLIDEAN/MANHATTAN/DOT）；②把向量数据同步到专门的 [[向量数据库]]
- 与"企业版功能下放社区版"（复制可观测性/超图优化器/PGO 等）形成对比，是 9.7 仍保留的云厂商护城河功能

## 关联连接

- [[MySQL]] — 对照的社区版
- [[Oracle]] — 出品方
- [[摘要-mysql-9-7-lts]] — 来源
- [[Percona]] — 本地部署的补位实现
- [[RAG]] — 受影响的应用场景
- [[向量数据库]] — 替代方案
