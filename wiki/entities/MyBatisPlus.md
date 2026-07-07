---
title: "MyBatisPlus"
type: entity
tags: [ORM, MyBatis]
sources: [raw/01-articles/springboot整合mybatisPlus.md, raw/01-articles/若依项目使用mybatis切换mybatis-plus导致PageHelper失效的问题.md, raw/01-articles/深度解析：Spring 事务与 MyBatis-Plus SqlSession 复用机制.md, raw/01-articles/MyBatis Plus 封神玩法：这12个骚操作让开发效率直接起飞！.md]
last_updated: 2026-06-10
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

## 最佳实践
- 避免使用 isNull 判断，改用具体默认值以利用索引
- 明确 Select 字段，避免全表查询开销
- 使用批量操作方法替代循环插入，减少网络往返
- 使用 EXISTS 代替 IN 子查询，提升查询性能
- 使用 orderBy 代替 last，避免 SQL 注入风险
- 使用 LambdaQuery 确保类型安全，便于重构
- 使用 between 代替 ge 和 le，简化范围查询
- 排序字段注意索引，避免文件排序
- 合理设置分页参数，控制单次查询数据量
- 优雅处理 Null 值，减少 if-else 判断
- 使用查询性能追踪工具监控慢查询
- 使用枚举类型映射，避免魔法值
- 自动处理逻辑删除，简化删除逻辑
- 使用乐观锁更新保护，并发控制

## 缓存机制
- **一级缓存（L1 Cache）**：默认开启，无法关闭。作用域为 SqlSession 级别（单次数据库会话）。在 Spring 集成环境中，SqlSession 与事务绑定，事务结束后缓存失效，分布式环境下无效。
- **二级缓存（L2 Cache）**：默认关闭，需手动配置（`cache-enabled: true` + Mapper 中声明 `<cache/>` 或实体类加注解）。作用域为 Mapper 级别（跨 SqlSession 共享）。推荐集成 Redis、Ehcache 等外部存储增强分布式缓存能力。
- **设计理念**：强调手动控制，开发者自行处理事务边界、缓存策略（LRU 淘汰、刷新间隔等），对 SQL 和缓存状态有 100% 控制权。

## SqlSession 复用机制
- **核心桥梁**：Spring 通过 SqlSessionTemplate（线程安全代理）和 ThreadLocal 管理 SqlSession 的获取与释放。
- **未开启事务**：每次 Mapper 查询独立创建 SqlSession，查询完毕立即关闭，一级缓存完全失效。
- **开启事务（@Transactional）**：Spring 事务拦截器新建 SqlSession，通过 TransactionSynchronizationManager 封装为 SqlSessionHolder 绑定到线程 ThreadLocal。整个事务生命周期内所有查询复用同一 SqlSession，一级缓存生效。
- **事务传播**：即使内层方法未加 @Transactional，默认 Propagation.REQUIRED 会加入外层事务，继续复用外层绑定的 SqlSession。

## 对比 JPA 缓存
- **MyBatis-Plus**：手动控制缓存，开发者自行配置 LRU 淘汰、刷新间隔，避免"黑魔法"行为。
- **JPA（Hibernate）**：自动化透明缓存，内置完善的一/二级缓存和延迟加载，但配置不当易出现 N+1 查询等性能陷阱。

## 关联连接
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 数据库
- [[MyBatis]] — 基础 ORM 框架
- [[PageHelper]] — 分页插件
- [[transaction-management]] — 事务管理与 SqlSession 绑定
- [[ORM]] — 对象关系映射概念
- [[逻辑删除]] — 数据删除策略
- [[乐观锁]] — 并发控制机制
- [[query-optimization]] — 查询优化
- [[摘要-用Qoder搭建PaiAgent项目脚手架]] — 使用 Qoder 的 Quest Mode 从零搭建 Pai…
