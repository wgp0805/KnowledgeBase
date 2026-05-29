---
title: "MyBatis"
type: entity
tags: [ORM, Java, 数据库]
sources: []
last_updated: 2026-05-29
---

## 定义
MyBatis 是一款优秀的半自动 ORM（对象关系映射）持久层框架，支持自定义 SQL、存储过程和高级映射，避免了几乎所有的 JDBC 代码和手动设置参数。

## 关键信息
- 半自动 ORM：SQL 由开发者编写，框架负责映射
- XML 映射：通过 XML 或注解配置 SQL 映射
- 动态 SQL：支持 if/choose/foreach 等动态 SQL 标签
- 与 MyBatis-Plus 关系：MyBatis-Plus 是 MyBatis 的增强工具，保留 MyBatis 所有特性
- PageHelper：MyBatis 分页插件
- 整合 Spring Boot：通过 mybatis-spring-boot-starter 自动配置

## 关联连接
- [[MyBatisPlus]] — 增强工具
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 常配合使用
- [[PageHelper]] — 分页插件
