---
title: "Tomcat"
type: entity
tags: [Web服务器, Java, Servlet]
sources: []
last_updated: 2026-05-29
---

## 定义
Apache Tomcat 是 Apache 软件基金会的开源 Servlet 容器和 Web 服务器，实现了 Java Servlet、JavaServer Pages（JSP）和 WebSocket 规范，是 Java Web 应用最常用的运行环境。

## 关键信息
- Servlet 容器：实现 Java Servlet 和 JSP 规范
- 嵌入式支持：Spring Boot 内嵌 Tomcat 作为默认 Web 服务器
- 连接器：Coyote（HTTP/HTTPS/AJP）
- 部署方式：WAR 包部署或嵌入式运行
- 版本与 Servlet 规范对应：Tomcat 10 → Servlet 6.0（Jakarta EE）

## 关联连接
- [[SpringBoot]] — 内嵌 Tomcat
- [[Nginx]] — 常作为反向代理
- [[Filter]] — Servlet 规范中的责任链实现
- [[Servlet]] — Java Web 基础规范
