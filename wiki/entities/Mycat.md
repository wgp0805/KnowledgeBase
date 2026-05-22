---
title: "Mycat"
type: entity
tags: [数据库中间件, 分库分表, Java]
sources: [raw/02-papers/Java高级技术之Mycat.pdf]
last_updated: 2026-05-22
---

## 定义
Mycat 是一款开源的分布式数据库中间件，基于阿里巴巴 Cobar 演化而来，提供分库分表、读写分离、全局序列号等功能。

## 关键信息
- 支持 MySQL / Oracle / SQL Server 等多种数据库
- 提供水平分片（分库分表）能力
- 支持读写分离
- 全局序列号（数据库方式/时间戳方式/分布式 ZK 方式）
- 支持 ER 分片（关联表绑定）
- 支持 SQL 路由与结果聚合

## 关联连接
- [[MySQL]] — 后端数据库
- [[摘要-java-mycat]] — 来源摘要
