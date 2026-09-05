---
title: "HandlerAdapter"
type: entity
tags: [SpringMVC, 适配器模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
HandlerAdapter 是 Spring MVC 中用于适配不同 Handler 类型的接口，通过适配器模式让 DispatcherServlet 能够统一调用不同类型的 Handler。

## 关键信息
- 适配器模式：让不兼容的接口能够协同工作
- Handler 类型：传统 Controller 接口、@RequestMapping 注解方法、HttpRequestHandler 等
- 工作流程：DispatcherServlet 拿到 Handler 后，找到对应的 HandlerAdapter，由适配器负责调用
- 统一接口：DispatcherServlet 只面向 HandlerAdapter 接口编程，不关心底层 Handler 差异
- 具体实现：RequestMappingHandlerAdapter、HttpRequestHandlerAdapter 等

## 关联连接
- [[SpringMVC]] — 所属模块
- [[Spring]] — 所属框架
- [[适配器模式]] — HandlerAdapter 体现的设计模式
- [[DispatcherServlet]] — 使用 HandlerAdapter 的前端控制器
- [[摘要-spring-design-patterns]] — 来源文章