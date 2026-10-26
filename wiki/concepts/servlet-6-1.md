---
title: "servlet-6-1"
type: concept
tags: [Servlet, JakartaEE, Web, 规范]
sources: [raw/09-archive/Spring Boot 4.0官宣：弃用 Undertow.md, "raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"]
last_updated: 2026-10-26
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

**落地 API 细节（2026-10，Tomcat 11.0.27 实测，详见 [[摘要-tomcat-11-new-features]]）**：
- `sendRedirect(String, int)`：直接指定 301/307/308 状态码；接口迁移推荐 308（历史浏览器遇 301/302 会把 POST 偷改成 GET，迁移时请求体易丢失；307/308 强制保持原请求方法）
- `setCharacterEncoding(Charset)`：支持直接传 `StandardCharsets` 对象，IDE 可自动补全
- `ServletOutputStream.write(ByteBuffer)`：与 NIO `FileChannel` 配合做文件下载，省去"先倒进 byte 数组再写出"的样板代码
- 新增状态码常量：308、421、422（`SC_UNPROCESSABLE_CONTENT`）、426
- `getParameter()` 等方法在请求参数解析出错时直接抛异常而非静默吞掉；Tomcat 11 因此删除了 `FailedRequestFilter`
- HTTP/2 Server Push 精确口径：规范将其降级为**可选功能**（允许容器不实现），主流浏览器（Chrome 等）已不支持，Tomcat 11 选择不实现，业界改用 `<link rel="preload">` 替代
- 注：上述 ④HTTP 会话增强、⑥isSensitiveHeader 两项 2026-10 源文未展开，原描述仍有效

## 关联连接
- [[Servlet]] — Servlet 规范
- [[JakartaEE]] — Jakarta EE 11 平台
- [[Undertow]] — 因未适配 Servlet 6.1 而被移除
- [[Tomcat]] — Tomcat 11 支持 Servlet 6.1
- [[Jetty]] — Jetty 12.1 支持 Servlet 6.1
- [[SpringBoot]] — Spring Boot 4.0 强制依赖 Servlet 6.1
- [[摘要-spring-boot-4-0-removes-undertow]] — 来源文章
- [[摘要-tomcat-11-new-features]] — 来源（Tomcat 11 视角的 6.1 落地细节）
- [[EL6.0]] — 同属 Jakarta EE 11 的 EL 规范
