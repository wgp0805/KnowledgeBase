---
title: "HttpRequestDecorator"
type: entity
tags: [Spring, 装饰器模式, HTTP]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
HttpRequestDecorator 是 Spring 框架中用于装饰 HTTP 请求的抽象类，通过装饰器模式在不修改原始请求对象的情况下增强其功能。

## 关键信息
- 装饰器模式：动态增强对象功能，保持接口一致性
- HttpServletRequestWrapper：Java Servlet 规范中的装饰器基类
- 应用场景：修改请求参数、添加请求头、包装请求体等
- 典型使用：ContentCachingRequestWrapper（缓存请求体）、CharacterEncodingWrapper（字符编码处理）
- Spring 中的实现：Spring 提供了多种 HttpRequestDecorator 的实现类

## 关联连接
- [[Spring]] — 所属框架
- [[装饰器模式]] — HttpRequestDecorator 体现的设计模式
- [[Filter]] — 常与 HttpRequestDecorator 配合使用
- [[摘要-spring-design-patterns]] — 来源文章