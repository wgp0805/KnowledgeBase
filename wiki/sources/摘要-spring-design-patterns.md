---
title: "摘要-spring-design-patterns"
type: source
tags: [Spring, 设计模式, 面试, 源码]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 核心摘要

本文详细介绍了Spring框架中使用的9种设计模式，包括工厂模式、单例模式、代理模式、模板方法模式、观察者模式、适配器模式、策略模式、责任链模式和装饰器模式。文章从面试考察点出发，强调设计模式认知广度、源码阅读深度和理论联系实际的重要性。通过核心答案表格和深度解析，深入讲解了每种设计模式在Spring中的具体实现组件和应用，如BeanFactory、ApplicationContext、AOP、JdbcTemplate、ApplicationEvent等。最后提供了面试高频追问和常见面试变体，帮助读者全面掌握Spring设计模式。

## 关联连接

- [[Spring]] — 文章核心讨论的框架
- [[BeanFactory]] — 工厂模式的核心实现
- [[ApplicationContext]] — 工厂模式的高级实现
- [[JdbcTemplate]] — 模板方法模式的典型应用
- [[ApplicationEvent]] — 观察者模式的实现基础
- [[HandlerAdapter]] — 适配器模式在Spring MVC中的应用
- [[Resource]] — 策略模式的资源加载接口
- [[设计模式]] — 文章讨论的核心概念
- [[工厂模式]] — Spring的基石设计模式
- [[单例模式]] — Bean的默认作用域
- [[代理模式]] — AOP的灵魂
- [[模板方法模式]] — JdbcTemplate等Template类的核心
- [[观察者模式]] — Spring事件机制的基础
- [[适配器模式]] — Spring MVC的核心
- [[策略模式]] — 资源加载等场景的应用
- [[责任链模式]] — Filter和Interceptor链
- [[装饰器模式]] — BeanWrapper等动态增强