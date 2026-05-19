---
title: "SpringMVC"
type: entity
tags: [Web框架, Spring]
sources: [raw/01-articles/过滤器Filter与拦截器Interceptor的区别.md, raw/01-articles/SpringBoot接收参数的几种常用方式.md]
last_updated: 2026-05-19
---

## 定义
Spring MVC 是 Spring 框架的 Web MVC 模块，基于 Servlet API 构建，实现了模型-视图-控制器设计模式。

## 关键信息
- 核心组件：DispatcherServlet（前端控制器）、HandlerMapping、HandlerAdapter、ViewResolver
- 参数接收：@PathVariable、@RequestParam、@RequestBody、@RequestHeader、@CookieValue
- 拦截器（Interceptor）：基于 Spring 容器，可访问 Spring 上下文
- 与 Filter 区别：Filter 基于 Servlet 容器，Interceptor 基于 Spring 容器

## 关联连接
- [[Spring]] — 基础框架
- [[SpringBoot]] — 自动配置框架
