---
title: "MySQL"
type: entity
tags: [数据库, 关系型]
sources: [raw/01-articles/mysql查询时间段数据.md, raw/01-articles/mysql查询cpu占用过高的方法.md, raw/01-articles/mysql关键字explain解析.md, raw/01-articles/springboot整合mybatisPlus.md, raw/01-articles/使用Docker在Windows上部署独立MySQL.md]
last_updated: 2026-05-19
---

## 定义
MySQL 是最流行的开源关系型数据库管理系统之一，以高性能、高可靠性和易用性著称，广泛应用于 Web 应用开发。

## 关键信息
- EXPLAIN 执行计划分析：type（访问类型）、key（使用索引）、rows（扫描行数）、Extra（额外信息）
- SQL 优化：索引优化、覆盖索引、避免 SELECT *、避免隐式类型转换
- 时间段查询：CURDATE()、DATE_FORMAT()、YEAR()/MONTH() 等日期函数
- CPU 过高排查：通过 performance_schema 关联 SQL 语句
- Docker 容器化部署支持数据持久化

## 关联连接
- [[MyBatisPlus]] — ORM 框架
- [[Docker]] — 容器化部署
- [[Oracle]] — 竞品数据库
