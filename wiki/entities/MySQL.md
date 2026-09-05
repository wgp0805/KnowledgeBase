---
title: "MySQL"
type: entity
tags: [数据库, 关系型]
sources:
  - raw/09-archive/mysql查询时间段数据.md
  - raw/09-archive/mysql查询cpu占用过高的方法.md
  - raw/09-archive/mysql关键字explain解析.md
  - raw/09-archive/springboot整合mybatisPlus.md
  - raw/09-archive/使用Docker在Windows上部署独立MySQL.md
  - raw/09-archive/第00章_写在前面.pdf
  - raw/09-archive/第00章_写在最后.pdf
  - raw/09-archive/第01章_数据库概述.pdf
  - raw/09-archive/第02章_MySQL环境搭建.pdf
  - raw/09-archive/第02章_MySQL的数据目录.pdf
  - raw/09-archive/第03章_基本的SELECT语句.pdf
  - raw/09-archive/第03章_用户与权限管理.pdf
  - raw/09-archive/第04章_逻辑架构.pdf
  - raw/09-archive/第04章_运算符.pdf
  - raw/09-archive/第05章_存储引擎.pdf
  - raw/09-archive/第05章_排序与分页.pdf
  - raw/09-archive/第06章_多表查询.pdf
  - raw/09-archive/第06章_索引的数据结构.pdf
  - raw/09-archive/第07章_单行函数.pdf
  - raw/09-archive/第08章_聚合函数.pdf
  - raw/09-archive/第08章_索引的创建与设计原则.pdf
  - raw/09-archive/第09章_性能分析工具的使用.pdf
  - raw/09-archive/第09章_子查询.pdf
  - raw/09-archive/第10章_创建和管理表.pdf
  - raw/09-archive/第10章_索引优化与查询优化.pdf
  - raw/09-archive/第11章_数据处理之增删改.pdf
  - raw/09-archive/第11章_数据库的设计规范.pdf
  - raw/09-archive/第12章_数据库其它调优策略.pdf
  - raw/09-archive/第12章_MySQL数据类型精讲.pdf
  - raw/09-archive/第13章_事务基础知识.pdf
  - raw/09-archive/第13章_约束.pdf
  - raw/09-archive/第14章_视图.pdf
  - raw/09-archive/第14章_MySQL事务日志.pdf
  - raw/09-archive/第15章_存储过程与函数.pdf
  - raw/09-archive/第15章_锁.pdf
  - raw/09-archive/第16章_变量、流程控制与游标.pdf
  - raw/09-archive/第16章_多版本并发控制.pdf
  - raw/09-archive/第17章_触发器.pdf
  - raw/09-archive/第17章_其它数据库日志.pdf
  - raw/09-archive/第18章_主从复制.pdf
  - raw/09-archive/第18章_MySQL8其它新特性.pdf
  - raw/09-archive/第19章_数据库备份与恢复.pdf
  - raw/01-articles/拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？.md
last_updated: 2026-08-26
---

## 定义
MySQL 是最流行的开源关系型数据库管理系统之一，以高性能、高可靠性和易用性著称，广泛应用于 Web 应用开发。

## 关键信息
- EXPLAIN 执行计划分析：type（访问类型）、key（使用索引）、rows（扫描行数）、Extra（额外信息）
- SQL 优化：索引优化、覆盖索引、避免 SELECT *、避免隐式类型转换
- 时间段查询：CURDATE()、DATE_FORMAT()、YEAR()/MONTH() 等日期函数
- CPU 过高排查：通过 performance_schema 关联 SQL 语句
- Docker 容器化部署支持数据持久化
- **千万级大表 DDL**：6 种方案应对锁表风险——原生 Online DDL（<1亿行）、停机维护（<100GB）、PT-OSC（触发器）、双写迁移（金融级10亿+）、gh-ost（无触发器TB级）、分区滑动窗口（日志表）。加字段前优先用 JSON 字段预扩展，万亿级表应分库分表
- **B+Tree 索引的模糊搜索短板**：`LIKE '%xx%'` 前置通配符导致 B+Tree 有序性失效，优化器放弃索引走全表扫描；`LIKE 'xx%'` 前缀固定可走索引。覆盖索引可扫更小的二级索引树但本质仍全扫，数据量大照样慢。这是引入 ES 倒排索引解决全文检索的根本原因
- **与 ES 的分工**：MySQL 是"存"的专家（事务、关联、ACID），ES 是"搜"的专家（全文检索、分词、相关度排序）。生产标准架构为 MySQL 主存储 + ES 搜索引擎，通过 Canal 监听 Binlog + MQ 异步同步

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
- [[摘要-mysql查询时间段数据]] — 汇总 MySQL 中按不同时间段（今天、昨天、近7天、本月、…
- [[摘要-Orcale表锁解决方法]] — 介绍 Oracle 数据库中查询表锁和强制解锁的方法，通过 …
- [[摘要-Orcale创建用户和表空间授权过程]] — 记录 Oracle 数据库中创建表空间、创建用户及授权（CO…
- [[摘要-trunc函数用法]] — 介绍 Oracle 数据库中 TRUNC 函数的两种用法：截…
- [[摘要-mysql查询cpu占用过高的方法]] — 介绍定位 MySQL CPU 占用过高问题的排查方法，通过操…
- [[摘要-千万级大表新增字段方案]] — 千万级大表新增字段 6 种方案对比（Online DDL/停机/PT-OSC/双写/gh-ost/分区）
- [[OnlineDDL]] — MySQL 在线表结构变更机制
- [[PT-OSC]] — Percona 在线表结构变更工具
- [[GhOst]] — GitHub 无触发器在线表结构变更工具
- [[双写迁移]] — 金融级零停机数据迁移方案
- [[BPlusTree]] — MySQL 索引底层数据结构
- [[InvertedIndex]] — 对比数据结构（ES 倒排索引）
- [[Elasticsearch]] — 搜索场景搭档
- [[Canal]] — MySQL → ES 同步工具
- [[摘要-拼多多二面-es-vs-mysql]] — 来源（面试视角 ES vs MySQL）
