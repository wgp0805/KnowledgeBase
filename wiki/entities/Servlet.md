---
title: "Servlet"
type: entity
tags: [Java, Web, 规范]
sources:
  - "raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"
last_updated: 2026-10-26
---

## 定义
Java Servlet 是 Java EE/Jakarta EE 规范中的服务器端组件，用于处理 HTTP 请求和生成动态 Web 内容，是 Java Web 应用的基础规范。

## 关键信息
- 定义了请求/响应处理模型：`HttpServletRequest` / `HttpServletResponse`
- 生命周期：init() → service() → destroy()
- 随 Java EE 演进到 Jakarta EE：`javax.servlet` → `jakarta.servlet`
- Tomcat 是最常用的 Servlet 容器实现
- Spring MVC 的 DispatcherServlet 基于 Servlet 规范构建

### Servlet 6.1（Jakarta EE 11）
- 于 2024 年 4 月作为 Jakarta EE 11 核心子规范发布
- Spring Boot 4.0 强制依赖 Servlet 6.1，导致 Undertow 被移除
- 主要改进：ByteBuffer 非阻塞 I/O、HTTP/2 推送废弃、SecurityManager 移除、HTTP 会话增强、重定向控制增强、敏感请求头识别

**Servlet 6.1 实用 API（2026-10，详见 [[摘要-tomcat-11-new-features]]）**：
- `resp.sendRedirect(path, statusCode)`：直接指定 301/307/308；接口迁移推荐 308（历史浏览器遇 301/302 会把 POST 偷改成 GET 致请求体丢失，307/308 强制保持原请求方法）
- `setCharacterEncoding(StandardCharsets.UTF_8)`：Charset 对象重载，IDE 可补全、不怕字符串拼错
- `ServletOutputStream.write(ByteBuffer)`：配合 NIO `FileChannel` 做文件下载，省去 byte 数组中转
- 新增状态码常量：308、421、422（`SC_UNPROCESSABLE_CONTENT`）、426
- 请求参数解析出错时 `getParameter()` 直接抛异常而非静默吞掉，Tomcat 11 据此删除了 `FailedRequestFilter`
- HTTP/2 Server Push 口径：Servlet 6.1 将其降级为可选功能，Tomcat 11 不再实现

## 关联连接
- [[Tomcat]] — Servlet 容器实现
- [[SpringMVC]] — 基于 Servlet 的 Web 框架
- [[DispatcherServlet]] — Spring MVC 前端控制器
- [[Filter]] — Servlet 规范中的过滤器
- [[SpringBoot]] — 内嵌 Servlet 容器
- [[摘要-tomcat-11-new-features]] — 来源（Servlet 6.1 API 实测细节）
- [[servlet-6-1]] — Servlet 6.1 概念页
