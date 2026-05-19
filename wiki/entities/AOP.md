---
title: "AOP"
type: entity
tags: [Spring, 编程范式]
sources: [raw/01-articles/SpringBoot-Aop的使用.md, raw/01-articles/spring框架中的事务管理.md]
last_updated: 2026-05-19
---

## 定义
AOP（Aspect-Oriented Programming，面向切面编程）通过预编译方式和运行期动态代理实现程序功能的统一维护，将日志、事务、权限等横切关注点与业务逻辑分离。

## 关键信息
- 通知类型：@Before（前置）、@After（后置）、@Around（环绕）、@AfterReturning（返回后）、@AfterThrowing（异常后）
- 切入点表达式：execution（方法匹配）、@annotation（注解匹配）、within（类匹配）
- 自定义注解作为切点：结合 @Around 实现通用日志或权限校验
- Spring AOP 底层：JDK 动态代理（接口）和 CGLIB（类）
- AOP 是 Spring @Transactional 事务管理的底层实现基础

## 关联连接
- [[SpringBoot]] — 整合框架
- [[Spring]] — 基础框架
