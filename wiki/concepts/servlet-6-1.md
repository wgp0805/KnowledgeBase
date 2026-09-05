---
title: "servlet-6-1"
type: concept
tags: [Servlet, JakartaEE, Web, 规范]
sources: [raw/01-articles/Spring Boot 4.0官宣：弃用 Undertow.md]
last_updated: 2026-07-29
---

## 定义
Servlet 6.1 是 Jakarta EE 11 的核心子规范，于 2024 年 4 月发布。它是 Spring Boot 4.0（基于 Spring Framework 7）强制依赖的 Servlet 规范基线，也是 Undertow 被移除支持的根本原因。

## 关键信息
与前代 Servlet 6.0 相比，Servlet 6.1 带来以下重要改进：

**① ByteBuffer 支持**：在 ServletInputStream 和 ServletOutputStream 中新增 ByteBuffer 支持，显著改进非阻塞 I/O 能力。

**② HTTP/2 推送功能废弃**：正式废弃 HTTP/2 Server Push 支持，该功能在现代 Web 应用中使用率持续下降。

**③ 移除 SecurityManager 相关 API**：完全删除对已废弃的 Java SecurityManager 及关联 API 的引用。

**④ HTTP 会话增强机制**：提供新机制让应用程序能在标准 HTTP 请求处理之外与 HTTP 会话交互，特别是为 WebSocket 场景提供更好支持。

**⑤ HTTP 重定向控制增强**：开发者对发出 HTTP 重定向时的状态码和响应体拥有更精细的控制权。

**⑥ 敏感请求头安全处理**：新增 `HttpServlet.isSensitiveHeader` 方法，用于识别需要保护的敏感请求头。

## 关联连接
- [[Servlet]] — Servlet 规范
- [[JakartaEE]] — Jakarta EE 11 平台
- [[Undertow]] — 因未适配 Servlet 6.1 而被移除
- [[Tomcat]] — Tomcat 11 支持 Servlet 6.1
- [[Jetty]] — Jetty 12.1 支持 Servlet 6.1
- [[SpringBoot]] — Spring Boot 4.0 强制依赖 Servlet 6.1
- [[摘要-spring-boot-4-0-removes-undertow]] — 来源文章
