---
title: "摘要-spring-mybatis-plus-sqlsession-reuse"
type: source
tags: [来源, Spring, MyBatis-Plus, 事务, 缓存]
sources: [raw/01-articles/深度解析：Spring 事务与 MyBatis-Plus SqlSession 复用机制.md]
last_updated: 2026-06-10
---

## 核心摘要
本文深入剖析了 Spring 事务环境下 MyBatis-Plus SqlSession 的复用机制。核心原理是 Spring 通过 SqlSessionTemplate 和 ThreadLocal 将 SqlSession 与当前事务强绑定：未加 @Transactional 时每次查询独立创建 SqlSession，一级缓存失效；加 @Transactional 后整个事务生命周期内复用同一 SqlSession，一级缓存生效。文章还对比了 MyBatis-Plus 与 JPA 的缓存设计理念差异——MyBatis-Plus 强调手动控制，JPA 强调自动化透明。

## 关联连接
- [[MyBatisPlus]] — MyBatis 增强工具，缓存机制详解
- [[MyBatis]] — 基础 ORM 框架，SqlSession 生命周期
- [[transaction-management]] — Spring 事务管理，SqlSession 与事务绑定
- [[Spring]] — 企业级框架，提供 @Transactional 和 SqlSessionTemplate
