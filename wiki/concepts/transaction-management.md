---
title: "transaction-management"
type: concept
tags: [Spring, 数据库]
sources: [raw/01-articles/spring框架中的事务管理.md]
last_updated: 2026-05-19
---

## 定义
事务管理是保证数据库操作原子性、一致性、隔离性和持久性（ACID）的机制，Spring 通过声明式事务（@Transactional）简化事务控制。

## 关键信息
- 传播行为：REQUIRED（默认，支持当前事务）、REQUIRES_NEW（新建事务）、NESTED（嵌套事务）、SUPPORTS、NOT_SUPPORTED、MANDATORY、NEVER
- 隔离级别：READ_UNCOMMITTED、READ_COMMITTED、REPEATABLE_READ、SERIALIZABLE
- 回滚规则：默认运行时异常回滚，编译时异常不回滚，可自定义 rollbackFor
- 常见失效场景：自调用（this.方法()）、多线程、非 public 方法、异常被 catch 吞掉
- 解决方案：注入自身代理调用、使用 AopContext.currentProxy()

## 关联连接
- [[Spring]] — 事务管理框架
- [[AOP]] — 事务底层实现
