---
title: "JakartaEE"
type: entity
tags: [Java, 规范, 企业级]
sources: [raw/01-articles/Spring Boot 4.0官宣：弃用 Undertow.md, "raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"]
last_updated: 2026-10-26
---

## 定义
Jakarta EE（原名 Java EE）是由 Eclipse 基金会维护的企业级 Java 平台规范集合，定义了 Java 企业应用的标准 API，包括 Servlet、JPA、EJB、JMS 等核心规范。

## 关键信息
- Servlet 6.1 是 Jakarta EE 11 的核心子规范，于 2024 年 4 月发布
- 从 Java EE 迁移到 Jakarta EE 时，命名空间从 `javax.*` 迁移到 `jakarta.*`
- Spring Boot 4.0 全面升级至 Jakarta EE 11
- Tomcat 11 实现的 Jakarta EE 11 Web 子规范清单（2026-10，详见 [[摘要-tomcat-11-new-features]]）：Servlet 6.1、Pages（JSP）4.0、EL 6.0、WebSocket 2.2、Authentication 3.1、Annotations 3.0
- Tomcat 的取舍哲学：不做全规范实现，只挑 Web 开发最常用的一组（对比 WebLogic/WildFly 全家桶应用服务器），这是其启动快、占用小、上手简单的轻量优势来源

## 关联连接
- [[Servlet]] — Jakarta EE 核心子规范
- [[SpringBoot]] — Spring Boot 4.0 基于 Jakarta EE 11
- [[摘要-spring-boot-4-0-removes-undertow]] — 来源文章
- [[摘要-tomcat-11-new-features]] — 来源（Tomcat 11 落地规范清单）
- [[EL6.0]] — Jakarta EE 11 表达式语言规范
