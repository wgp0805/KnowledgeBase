---
title: "Undertow"
type: entity
tags: [Web服务器, Java, Servlet, Red Hat]
sources: [raw/01-articles/Spring Boot 4.0官宣：弃用 Undertow.md]
last_updated: 2026-07-29
---

## 定义
Undertow 是 Red Hat 出品的开源嵌入式 Web 容器，以低内存占用、高并发吞吐和原生支持持久连接为特点，曾被 Spring Boot 支持为三种嵌入式 Web 容器之一（与 Tomcat、Jetty 并列）。

## 关键信息
- 以性能优势著称：高并发场景下内存占用比 Tomcat 低、吞吐量更高
- 曾被 Spring Boot 支持为可选嵌入式 Web 容器（spring-boot-starter-undertow）
- **Spring Boot 4.0 正式移除对 Undertow 的支持**，因为 Undertow 尚未适配 Servlet 6.1
- Red Hat 对 Undertow 的投入相对有限，导致无法及时跟进新规范
- Undertow 团队已在 2025 年 10 月发布 2.4.0.Alpha1 开始实现 Jakarta Servlet 6.1，但正式支持时间表未知

## 关联连接
- [[RedHat]] — Undertow 的主要维护方
- [[Tomcat]] — 另一 Servlet 容器，Spring Boot 默认
- [[Jetty]] — 另一轻量 Servlet 容器
- [[Servlet]] — Servlet 规范
- [[SpringBoot]] — Spring Boot 4.0 移除 Undertow
- [[摘要-spring-boot-4-0-removes-undertow]] — 来源文章
