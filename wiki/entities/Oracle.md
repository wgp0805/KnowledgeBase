---
title: "Oracle"
type: entity
tags: [数据库, 关系型]
sources: [raw/01-articles/Orcale表锁解决方法.md, raw/01-articles/orcale查看索引状态.md, raw/01-articles/orcale常用的查询资源的方法.md, raw/01-articles/Orcale创建用户和表空间授权过程.md, raw/01-articles/trunc函数用法.md]
last_updated: 2026-05-19
---

## 定义
Oracle Database 是甲骨文公司提供的企业级关系型数据库管理系统，以高性能、高安全性、高可用性著称，广泛用于大型企业应用。

## 关键信息
- TRUNC 函数：截取时间（年/月/日/时/分）和数值（指定小数位数）
- 表锁查询：v$session 和 v$locked_object 视图定位锁会话
- 索引状态检查：user_indexes、dba_indexes 视图
- DBA 运维：慢 SQL 定位、表空间监控、回滚段管理
- 用户和权限：CREATE TABLESPACE、CREATE USER、GRANT CONNECT/RESOURCE
- 角色权限体系：系统权限和对象权限分离

## 关联连接
- [[MySQL]] — 竞品数据库
- [[Linux]] — 运行环境
