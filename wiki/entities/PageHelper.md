---
title: "PageHelper"
type: entity
tags: [MyBatis, 分页, Java]
sources: []
last_updated: 2026-05-29
---

## 定义
PageHelper 是 MyBatis 的物理分页插件，通过拦截器机制自动改写 SQL 实现分页查询，支持多种数据库方言。

## 关键信息
- 物理分页：自动在 SQL 后追加 LIMIT 语句
- 使用方式：`PageHelper.startPage(pageNum, pageSize)` 开启分页
- 支持数据库：MySQL、Oracle、PostgreSQL、SQL Server 等
- PageInfo：封装分页结果（总条数、页数、是否有上下页等）
- 注意事项：startPage 必须紧跟在查询方法前，中间不能有其他 SQL

## 关联连接
- [[MyBatis]] — 所属框架
- [[MyBatisPlus]] — 内置分页功能，无需 PageHelper
- [[SpringBoot]] — 常用整合环境
