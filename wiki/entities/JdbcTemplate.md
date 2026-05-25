---
title: "JdbcTemplate"
type: entity
tags: [Spring, JDBC, 模板方法模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
JdbcTemplate 是 Spring 框架中用于简化 JDBC 操作的模板类，通过模板方法模式封装了连接获取、Statement 创建、异常处理、资源关闭等繁琐流程。

## 关键信息
- 模板方法模式：定义算法骨架（固定流程），可变步骤留给调用方
- 简化 JDBC：封装了 try-catch-finally 流程，开发者只需关注 SQL 和结果映射
- 典型方法：`query()`、`update()`、`execute()` 等
- 回调接口：RowMapper、ResultSetExtractor 等用于结果映射
- 同类模板：RestTemplate、JmsTemplate、RedisTemplate 等都采用相同设计模式

## 关联连接
- [[Spring]] — 所属框架
- [[模板方法模式]] — JdbcTemplate 体现的设计模式
- [[Java]] — 编程语言
- [[MySQL]] — 常用数据库
- [[摘要-spring-design-patterns]] — 来源文章