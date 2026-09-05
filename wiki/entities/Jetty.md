---
title: "Jetty"
type: entity
tags: [Web服务器, Java, Servlet, Eclipse]
sources: [raw/01-articles/Spring Boot 4.0官宣：弃用 Undertow.md]
last_updated: 2026-07-29
---

## 定义
Jetty 是 Eclipse 基金会出品的轻量嵌入式 Web 容器，以灵活轻量著称，在 I/O 密集型场景下表现优异，是 Spring Boot 4.0 仍支持的两种嵌入式 Web 容器之一。

## 关键信息
- 轻量灵活，支持 Servlet 6.1 规范（Jetty 12.1.x）
- 在 Spring Boot 4.0 中与 Tomcat 并列被支持（Undertow 已被移除）
- I/O 密集型场景下表现优异
- 需手动引入依赖并排除默认的 Tomcat

## 关联连接
- [[Tomcat]] — 对比 Servlet 容器
- [[Undertow]] — 已被 Spring Boot 4.0 移除的容器
- [[SpringBoot]] — Spring Boot 支持 Jetty
- [[Servlet]] — Servlet 规范
- [[摘要-spring-boot-4-0-removes-undertow]] — 来源文章
