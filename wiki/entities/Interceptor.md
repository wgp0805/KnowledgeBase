---
title: "Interceptor"
type: entity
tags: [SpringMVC, 责任链模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
Interceptor（拦截器）是 Spring MVC 中的组件，用于在请求处理的不同阶段进行拦截处理。通过责任链模式形成拦截器链，实现权限检查、日志记录等功能。

## 关键信息
- 责任链模式：请求沿着链条依次处理，每个 Interceptor 决定是否继续执行
- HandlerInterceptor 接口：preHandle()、postHandle()、afterCompletion()
- 执行时机：Controller 方法执行前、执行后、视图渲染后
- 应用场景：权限认证、日志记录、性能监控、国际化处理等
- 配置方式：WebMvcConfigurer.addInterceptors() 注册
- 与 Filter 区别：Interceptor 是 Spring MVC 特有，可以访问 Spring 上下文

## 关联连接
- [[SpringMVC]] — 所属模块
- [[Spring]] — 所属框架
- [[责任链模式]] — Interceptor 体现的设计模式
- [[Filter]] — Servlet 规范中的类似概念
- [[摘要-spring-design-patterns]] — 来源文章
- [[摘要-过滤器Filter与拦截器Interceptor的区别]] — 详细对比