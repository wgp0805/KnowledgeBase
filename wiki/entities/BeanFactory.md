---
title: "BeanFactory"
type: entity
tags: [Spring, IoC, 工厂模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
BeanFactory 是 Spring 框架中最顶层的工厂接口，提供了 `getBean()` 等基本能力，属于"懒加载"模式，即用到 Bean 的时候才创建。

## 关键信息
- 核心方法：`getBean()` 用于获取 Bean 实例
- 懒加载：Bean 在第一次请求时才创建
- 工厂模式实现：封装了对象的创建过程，调用方无需关心对象如何创建
- 层次结构：BeanFactory 是 ApplicationContext 的父接口
- 具体实现：ClassPathXmlApplicationContext（XML配置）、AnnotationConfigApplicationContext（注解配置）

## 关联连接
- [[Spring]] — 所属框架
- [[ApplicationContext]] — BeanFactory 的超集，集成了更多企业级功能
- [[工厂模式]] — BeanFactory 体现的设计模式
- [[singleton-pattern]] — BeanFactory 管理的 Bean 默认为单例
- [[摘要-spring-design-patterns]] — 来源文章