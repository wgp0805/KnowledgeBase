---
title: "MyBatisPlus"
type: entity
tags: [ORM, MyBatis]
sources: [raw/01-articles/springboot整合mybatisPlus.md, raw/01-articles/若依项目使用mybatis切换mybatis-plus导致PageHelper失效的问题.md]
last_updated: 2026-05-19
---

## 定义
MyBatis-Plus（简称 MP）是 MyBatis 的增强工具，在 MyBatis 的基础上只做增强不做改变，为简化开发、提高效率而生。

## 关键信息
- 自动 CRUD：BaseMapper 提供 insert/update/delete/select 方法
- 条件构造器：QueryWrapper/LambdaQueryWrapper 支持链式条件查询
- 分页插件：PaginationInterceptor（PageHelper 可替代方案）
- 代码生成器：AutoGenerator 自动生成 Entity/Mapper/Service/Controller
- 多数据源：@DS 注解实现读写分离
- 逻辑删除：@TableLogic 自动处理删除标记
- 乐观锁插件：@Version 处理并发更新

## 关联连接
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 数据库
- [[MyBatis]] — 基础 ORM 框架
- [[PageHelper]] — 分页插件
