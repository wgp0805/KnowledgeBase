---
title: "BeanWrapper"
type: entity
tags: [Spring, 装饰器模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
BeanWrapper 是 Spring 框架中用于封装 Bean 属性访问的接口，通过装饰器模式动态增强对象功能，提供属性读写、类型转换、验证等功能。

## 关键信息
- 装饰器模式：动态增强对象功能，不修改原有代码
- 属性操作：getPropertyType()、setPropertyValue()、getPropertyValue()
- 类型转换：内置 PropertyEditor 和 ConversionService 支持
- 验证功能：支持 Bean Validation 集成
- 应用场景：Spring 容器创建 Bean 时的属性注入和绑定

## 关联连接
- [[Spring]] — 所属框架
- [[装饰器模式]] — BeanWrapper 体现的设计模式
- [[IoC]] — Spring 控制反转容器的核心组件
- [[摘要-spring-design-patterns]] — 来源文章