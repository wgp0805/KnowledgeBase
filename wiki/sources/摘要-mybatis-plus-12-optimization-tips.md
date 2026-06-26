---
title: "摘要-mybatis-plus-12-optimization-tips"
type: source
tags: [来源, 原始文件, MyBatis Plus, 优化]
sources: [raw/01-articles/MyBatis Plus 封神玩法：这12个骚操作让开发效率直接起飞！.md]
last_updated: 2026-06-26
---

## 核心摘要
本文介绍了 12 个 MyBatis Plus 性能优化技巧，旨在提升开发效率和查询性能。文章通过对比“不推荐”与“推荐”的写法，强调了使用具体默认值代替 isNull、明确 Select 字段、批量操作替代循环、EXISTS 代替 IN 子查询、使用 orderBy 代替 last、LambdaQuery 确保类型安全、between 代替 ge/le、注意排序字段索引、合理设置分页参数、优雅处理 Null 值、查询性能追踪、枚举类型映射、自动逻辑删除和乐观锁更新保护等最佳实践。这些技巧有助于减少数据库开销、提高代码可维护性和系统性能。

## 关联连接
- [[MyBatis Plus]] — 核心 ORM 框架
- [[ORM]] — 对象关系映射概念
- [[逻辑删除]] — 数据删除策略
- [[乐观锁]] — 并发控制机制
- [[分页查询]] — 数据查询优化
- [[批量操作]] — 性能提升方法
- [[子查询]] — SQL 查询优化
- [[类型安全]] — 代码健壮性
- [[性能追踪]] — 系统监控
- [[Java]] — 开发语言
- [[MySQL]] — 数据库
