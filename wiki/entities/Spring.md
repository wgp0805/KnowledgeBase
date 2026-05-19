---
title: "Spring"
type: entity
tags: [框架, Java, IoC]
sources: [raw/01-articles/spring框架中的事务管理.md, raw/01-articles/理解Spring中的ApplicationListener与ApplicationRunner区别及使用场景.md, raw/01-articles/过滤器Filter与拦截器Interceptor的区别.md]
last_updated: 2026-05-19
---

## 定义
Spring 是一个轻量级的 Java 企业级应用开发框架，通过 IoC（控制反转）和 AOP（面向切面编程）两大核心特性简化企业级开发。

## 关键信息
- IoC 容器：管理 Bean 生命周期和依赖注入（DI）
- @Transactional 声明式事务：支持传播行为（REQUIRED/REQUIRES_NEW/NESTED）和隔离级别
- 事务失效场景：自调用（this.方法()）、多线程、非 public 方法、异常类型不匹配
- ApplicationListener：事件监听机制，观察者模式实现解耦
- AOP 底层：JDK 动态代理（接口）和 CGLIB 代理（类）

## 关联连接
- [[SpringBoot]] — 自动配置扩展
- [[SpringMVC]] — Web MVC 框架
- [[SpringSecurity]] — 安全框架
- [[AOP]] — 面向切面编程
