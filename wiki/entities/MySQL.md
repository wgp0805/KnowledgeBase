---
title: "MySQL"
type: entity
tags: [数据库, 关系型]
sources:
  - raw/01-articles/mysql查询时间段数据.md
  - raw/01-articles/mysql查询cpu占用过高的方法.md
  - raw/01-articles/mysql关键字explain解析.md
  - raw/01-articles/springboot整合mybatisPlus.md
  - raw/01-articles/使用Docker在Windows上部署独立MySQL.md
  - raw/02-papers/第00章_写在前面.pdf
  - raw/02-papers/第00章_写在最后.pdf
  - raw/02-papers/第01章_数据库概述.pdf
  - raw/02-papers/第02章_MySQL环境搭建.pdf
  - raw/02-papers/第02章_MySQL的数据目录.pdf
  - raw/02-papers/第03章_基本的SELECT语句.pdf
  - raw/02-papers/第03章_用户与权限管理.pdf
  - raw/02-papers/第04章_逻辑架构.pdf
  - raw/02-papers/第04章_运算符.pdf
  - raw/02-papers/第05章_存储引擎.pdf
  - raw/02-papers/第05章_排序与分页.pdf
  - raw/02-papers/第06章_多表查询.pdf
  - raw/02-papers/第06章_索引的数据结构.pdf
  - raw/02-papers/第07章_单行函数.pdf
  - raw/02-papers/第08章_聚合函数.pdf
  - raw/02-papers/第08章_索引的创建与设计原则.pdf
  - raw/02-papers/第09章_性能分析工具的使用.pdf
  - raw/02-papers/第09章_子查询.pdf
  - raw/02-papers/第10章_创建和管理表.pdf
  - raw/02-papers/第10章_索引优化与查询优化.pdf
  - raw/02-papers/第11章_数据处理之增删改.pdf
  - raw/02-papers/第11章_数据库的设计规范.pdf
  - raw/02-papers/第12章_数据库其它调优策略.pdf
  - raw/02-papers/第12章_MySQL数据类型精讲.pdf
  - raw/02-papers/第13章_事务基础知识.pdf
  - raw/02-papers/第13章_约束.pdf
  - raw/02-papers/第14章_视图.pdf
  - raw/02-papers/第14章_MySQL事务日志.pdf
  - raw/02-papers/第15章_存储过程与函数.pdf
  - raw/02-papers/第15章_锁.pdf
  - raw/02-papers/第16章_变量、流程控制与游标.pdf
  - raw/02-papers/第16章_多版本并发控制.pdf
  - raw/02-papers/第17章_触发器.pdf
  - raw/02-papers/第17章_其它数据库日志.pdf
  - raw/02-papers/第18章_主从复制.pdf
  - raw/02-papers/第18章_MySQL8其它新特性.pdf
  - raw/02-papers/第19章_数据库备份与恢复.pdf
last_updated: 2026-05-22
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
- [[Mycat]] — 数据库中间件
- [[query-optimization]] — 查询优化
- [[transaction-management]] — 事务管理
- [[摘要-mysql-course]] — MySQL 完整课程
- [[sharding]] — 分库分表架构
- [[mysql-storage-engine-comparison]] — 存储引擎对比与底层架构
- [[MVCC]] — 多版本并发控制
