---
title: "JDK动态代理"
type: concept
tags: [Java, 代理模式, 反射, AOP]
sources: []
last_updated: 2026-05-29
---

## 定义
JDK 动态代理是 Java 原生提供的代理机制，通过 `java.lang.reflect.Proxy` 在运行时动态创建实现指定接口的代理对象，是 Spring AOP 的底层实现之一。

## 关键信息
- 前提条件：目标类必须实现至少一个接口
- 核心类：`Proxy.newProxyInstance(ClassLoader, Class<?>[], InvocationHandler)`
- InvocationHandler：代理对象的方法调用会被转发到此接口的 invoke 方法
- 与 CGLIB 对比：JDK 代理基于接口（组合），CGLIB 基于继承
- 性能：JDK 代理在高版本 JDK 中性能已优化，与 CGLIB 差距缩小

## 关联连接
- [[代理模式]] — 设计模式基础
- [[CGLIB代理]] — 另一种代理实现
- [[Spring]] — AOP 代理实现
- [[AOP]] — 面向切面编程
