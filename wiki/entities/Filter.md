---
title: "Filter"
type: entity
tags: [Java, Servlet, 责任链模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
Filter（过滤器）是 Java Servlet 规范中的组件，用于在请求到达 Servlet 之前和响应发送到客户端之前进行预处理和后处理。在 Spring 中，Filter 通过责任链模式形成过滤器链。

## 关键信息
- 责任链模式：请求沿着链条依次处理，每个 Filter 决定是否传递给下一个
- Servlet 规范：javax.servlet.Filter 接口
- 生命周期：init()、doFilter()、destroy()
- 应用场景：字符编码处理、安全认证、日志记录、跨域处理等
- Spring Boot 中的配置：FilterRegistrationBean 注册自定义 Filter
- 与 Interceptor 区别：Filter 是 Servlet 规范，Interceptor 是 Spring MVC 特有

## 关联连接
- [[Spring]] — Spring 框架中的应用
- [[责任链模式]] — Filter 体现的设计模式
- [[Interceptor]] — Spring MVC 中的类似概念
- [[摘要-spring-design-patterns]] — 来源文章
- [[摘要-过滤器Filter与拦截器Interceptor的区别]] — 详细对比