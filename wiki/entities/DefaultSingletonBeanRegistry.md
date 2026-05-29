---
title: "DefaultSingletonBeanRegistry"
type: entity
tags: [Spring, 单例模式, 缓存]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
DefaultSingletonBeanRegistry 是 Spring 框架中管理单例 Bean 的核心类，通过三级缓存机制解决单例 Bean 的循环依赖问题。

## 关键信息
- 单例模式：容器级别单例，保证同一个 id 的 Bean 只创建一次
- 三级缓存：
  1. singletonObjects（一级缓存）：完全初始化好的单例 Bean
  2. earlySingletonObjects（二级缓存）：早期暴露的 Bean（解决循环依赖）
  3. singletonFactories（三级缓存）：Bean 工厂（用于创建代理对象）
- 循环依赖：三级缓存主要解决代理对象的循环依赖问题
- 线程安全：Spring 单例是非线程安全的，Bean 应设计为无状态

## 关联连接
- [[Spring]] — 所属框架
- [[singleton-pattern]] — DefaultSingletonBeanRegistry 体现的设计模式
- [[BeanFactory]] — 单例 Bean 的管理容器
- [[摘要-spring-design-patterns]] — 来源文章