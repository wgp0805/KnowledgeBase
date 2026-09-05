---
title: "CGLIB代理"
type: concept
tags: [Spring, AOP, 代理模式, 字节码]
sources: []
last_updated: 2026-05-29
---

## 定义
CGLIB（Code Generation Library）代理是通过运行时生成目标类的子类来实现的代理模式，无需目标类实现接口，Spring AOP 在目标类无接口时默认使用 CGLIB 代理。

## 关键信息
- 原理：运行时通过 ASM 字节码框架生成目标类的子类
- 限制：无法代理 final 类和 final 方法
- 与 JDK 动态代理对比：CGLIB 不需要接口，但通过继承实现
- Spring 5.x+：默认使用 CGLIB 代理（即使有接口）
- 代理创建时机：容器启动时或首次获取 Bean 时

## 关联连接
- [[代理模式]] — 设计模式基础
- [[JDK动态代理]] — 另一种代理实现
- [[Spring]] — AOP 代理实现
- [[AOP]] — 面向切面编程
- [[BeanFactory]] — 代理对象的创建时机
