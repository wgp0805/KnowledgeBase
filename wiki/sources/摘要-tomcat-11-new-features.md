---
title: "摘要-tomcat-11-new-features"
type: source
tags: [来源, 原始文件]
sources: ["raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"]
last_updated: 2026-10-26
---

## 核心摘要
文章系统梳理了 Tomcat 11（当前最新 11.0.27，Spring Boot 4.x 默认内嵌容器）的新特性。底座方面：最低要求 Java 17，对齐 Jakarta EE 11，完整实现 Servlet 6.1、Pages(JSP) 4.0、EL 6.0、WebSocket 2.2、Authentication 3.1、Annotations 3.0 这组 Web 规范。最亮点是 Connector 层支持虚拟线程——`useVirtualThreads="true"` 一行配置（Spring Boot 则是 `spring.threads.virtual.enabled=true`），让"一请求一线程"的同步代码扛住高并发，但仅解决 IO 等待、不解决 CPU 密集，且 `synchronized` pinning 问题到 Java 24（JEP 491）才解决，生产推荐 Java 25 LTS。Servlet 6.1 落地了几个实用 API：`sendRedirect()` 可指定状态码（308 保持请求方法）、`setCharacterEncoding(Charset)` 重载、`ServletOutputStream.write(ByteBuffer)`；EL 6.0 终于支持读取 record 组件和数组 `.length`。同时文章强调"做减法"：移除 SecurityManager（Java 24 JEP 486 永久禁用）、HTTP/2 Server Push（浏览器已不支持）、全部废弃 API；默认更安全（`maxParameterCount` 10000→1000 防 DoS、Cookie 严格 RFC 6265），并新增 FFM API 直调系统 OpenSSL，免装 tomcat-native JNI 库。文末附 Docker 一键部署（镜像 webapps 默认为空的坑）与内嵌 Tomcat 11 完整可运行示例（JDK 25 + 11.0.27 实测）。

**版本线速查**：

| Tomcat 版本 | 对应平台 | Servlet 版本 | 包名 | 最低 Java |
| --- | --- | --- | --- | --- |
| 9.0.x | Java EE 8 | 4.0 | `javax.*` | 8 |
| 10.1.x | Jakarta EE 10 | 6.0 | `jakarta.*` | 11 |
| 11.0.x | Jakarta EE 11 | 6.1 | `jakarta.*` | 17 |

## 关联连接
- [[Tomcat]] — 文章主角，实体页增量合并
- [[Servlet]] — Servlet 6.1 API 落地细节
- [[servlet-6-1]] — Servlet 6.1 概念页（增量细节并入此页）
- [[JakartaEE]] — Jakarta EE 11 平台与 Web 规范组清单
- [[EL6.0]] — EL 6.0 支持 record 与数组 length
- [[虚拟线程]] — Connector 虚拟线程开启方式与坑
- [[HTTP2]] — Server Push 移除涉及
- [[Java]] — Java 17 起步 / JEP 486、JEP 491 / Java 25 LTS 推荐
- [[SpringBoot]] — Spring Boot 4.x 默认内嵌 Tomcat 11，一行配置开虚拟线程
- [[Docker]] — `tomcat:11.0-jdk21` 一键部署与 webapps 空目录坑
- [[摘要-spring-boot-4-0-removes-undertow]] — Servlet 6.1 / Spring Boot 4 强相关来源
