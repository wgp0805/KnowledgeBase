---
title: "DispatcherServlet"
type: entity
tags: [SpringMVC, 前端控制器]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
DispatcherServlet 是 Spring MVC 的前端控制器，负责接收所有 HTTP 请求并将其分派给相应的处理器（Handler）。它使用 HandlerAdapter 来适配不同类型的处理器。

## 关键信息
- 前端控制器模式：所有请求都经过 DispatcherServlet 处理
- 请求处理流程：接收请求 → 查找 Handler → 找到 HandlerAdapter → 执行 Handler → 返回 ModelAndView
- HandlerAdapter 使用：通过适配器模式支持不同类型的 Handler（Controller、@RequestMapping 方法等）
- 组件协调：协调 HandlerMapping、HandlerAdapter、ViewResolver 等组件
- 配置方式：在 web.xml 中配置或通过 Spring Boot 自动配置

## 关联连接
- [[SpringMVC]] — 所属模块
- [[Spring]] — 所属框架
- [[HandlerAdapter]] — DispatcherServlet 使用的适配器
- [[适配器模式]] — DispatcherServlet 中 HandlerAdapter 的应用
- [[摘要-spring-design-patterns]] — 来源文章