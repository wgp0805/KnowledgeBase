---
title: "摘要-spring-boot-4-0-removes-undertow"
type: source
tags: [Spring Boot, Undertow, Servlet, Web容器]
sources: [raw/01-articles/Spring Boot 4.0官宣：弃用 Undertow.md]
last_updated: 2026-07-29
---

## 核心摘要
Spring Boot 4.0 基于 Spring Framework 7 构建，强制依赖 Servlet 6.1 规范，而 Undertow 尚未适配 Servlet 6.1，因此 Spring Boot 团队正式移除了对 Undertow 嵌入式 Web 容器的支持。文章详细解析了 Undertow 被弃用的前因后果：根本原因是 Servlet 6.1 不兼容，深层次原因是 Red Hat 对 Undertow 投入有限导致迭代缓慢。Servlet 6.1 带来了 ByteBuffer 支持、HTTP/2 推送废弃、SecurityManager 移除、HTTP 会话增强等多项重要改进。目前 Spring Boot 4.0 仅支持 Tomcat 11（Servlet 6.1）和 Jetty 12.1（Servlet 6.1）两种容器，使用 Undertow 的项目需要迁移到 Tomcat 或 Jetty。

## 关联连接
- [[Undertow]] — 被 Spring Boot 4.0 移除的嵌入式 Web 容器
- [[Jetty]] — Eclipse 基金会轻量嵌入式 Web 容器
- [[Tomcat]] — Apache Servlet 容器，Spring Boot 默认
- [[Servlet]] — Java Web 基础规范
- [[JakartaEE]] — Jakarta EE 11 平台
- [[SpringBoot]] — Spring 自动配置框架
