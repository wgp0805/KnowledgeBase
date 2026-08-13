---
title: "transaction-management"
type: concept
tags: [Spring, 数据库]
sources: [raw/09-archive/spring框架中的事务管理.md, raw/01-articles/深度解析：Spring 事务与 MyBatis-Plus SqlSession 复用机制.md]
last_updated: 2026-06-10
---

## 定义
事务管理是保证数据库操作原子性、一致性、隔离性和持久性（ACID）的机制，Spring 通过声明式事务（@Transactional）简化事务控制。

## 关键信息
- 传播行为：REQUIRED（默认，支持当前事务）、REQUIRES_NEW（新建事务）、NESTED（嵌套事务）、SUPPORTS、NOT_SUPPORTED、MANDATORY、NEVER
- 隔离级别：READ_UNCOMMITTED、READ_COMMITTED、REPEATABLE_READ、SERIALIZABLE
- 回滚规则：默认运行时异常回滚，编译时异常不回滚，可自定义 rollbackFor
- 常见失效场景：自调用（this.方法()）、多线程、非 public 方法、异常被 catch 吞掉
- 解决方案：注入自身代理调用、使用 AopContext.currentProxy()

## 事务与 SqlSession 绑定
在 MyBatis/MyBatis-Plus 集成环境中，@Transactional 不仅管理数据库事务，还决定了 SqlSession 的生命周期：
- **SqlSessionTemplate**：Spring 提供的线程安全 SqlSession 代理，内部通过 ThreadLocal 管理会话。
- **ThreadLocal 绑定**：@Transactional 开启时，Spring 通过 TransactionSynchronizationManager 将 SqlSession 封装为 SqlSessionHolder 绑定到当前线程。
- **复用效果**：同一事务内的所有 Mapper 查询共享同一个 SqlSession，MyBatis 一级缓存生效；无事务时每次查询独立创建 SqlSession，一级缓存失效。
- **传播继承**：Propagation.REQUIRED（默认）使内层方法继承外层事务的 SqlSession 绑定。

## 关联连接
- [[Spring]] — 事务管理框架
- [[AOP]] — 事务底层实现
- [[MyBatisPlus]] — 事务内 SqlSession 复用
