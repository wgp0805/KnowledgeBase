---
title: "Servlet"
type: entity
tags: [Java, Web, 规范]
sources: []
last_updated: 2026-06-02
---

## 定义
Java Servlet 是 Java EE/Jakarta EE 规范中的服务器端组件，用于处理 HTTP 请求和生成动态 Web 内容，是 Java Web 应用的基础规范。

## 关键信息
- 定义了请求/响应处理模型：`HttpServletRequest` / `HttpServletResponse`
- 生命周期：init() → service() → destroy()
- 随 Java EE 演进到 Jakarta EE：`javax.servlet` → `jakarta.servlet`
- Tomcat 是最常用的 Servlet 容器实现
- Spring MVC 的 DispatcherServlet 基于 Servlet 规范构建

## 关联连接
- [[Tomcat]] — Servlet 容器实现
- [[SpringMVC]] — 基于 Servlet 的 Web 框架
- [[DispatcherServlet]] — Spring MVC 前端控制器
- [[Filter]] — Servlet 规范中的过滤器
- [[SpringBoot]] — 内嵌 Servlet 容器
