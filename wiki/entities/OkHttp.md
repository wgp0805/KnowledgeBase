---
title: "OkHttp"
type: entity
tags: [HTTP客户端, Java, Kotlin, Square, 网络请求]
sources: [raw/09-archive/2026-10-22 - 为什么越来越多人使用 OkHttp 5.5 ？.md]
last_updated: 2026-10-23
---

## 定义
OkHttp 是 Square 出品的 HTTP 客户端库，Android 与 JVM 上的 Java/Kotlin 通用（Java 调用方式与 4.x 几乎一样：`OkHttpClient.Builder` + `Request.Builder`；库本身 Kotlin 编写会带 `kotlin-stdlib`）。Rising用法多经 Retrofit 间接引入，因此"Retrofit 一升版本，OkHttp 行为跟着变"——它早已躺在很多 Java 服务的调用链上。

（注：Retrofit 在本库未建页，纯文本记录）

## 关键信息
- **职责画像**：找地址（DNS）→ 建连接（连接池复用）→ 做 TLS → 收发响应；HTTP/2 单连接并发多请求、响应默认 gzip、失败按策略重试；5.0 起 IPv6/IPv4 一起试（Happy Eyeballs），还有 GraalVM 原生镜像与 JPMS module-info 支持
- **5.x 分包坑**：Gradle 写 `com.squareup.okhttp3:okhttp` 会自动选 JVM 包；**Maven 必须显式依赖 `okhttp-jvm`**（空 okhttp 构件没有 class）——Java 用户最常踩；用 BOM 锁版本
- **性能要点**：客户端必须进程内共享一份；每个请求 `new OkHttpClient()` 会连连接池/线程池都新建，是 Java 服务最常见的性能问题
- **5.5 新特性**：
  - **ECH（Encrypted Client Hello）**：握手段 SNI 里的域名也加密，路人更多时候只能看到 IP；前提是系统 TLS 栈支持（目前 Android 17/API 37），JDK 进程要等 JDK TLS 跟进——5.5 只是"把门打开"，同一套配置，平台支持后自动生效
  - **DNS API 重做**：可查 HTTPS 记录，结果异步/流式返回并带内存缓存；除 IP 外能拿到 ECH 配置、ALPN、端口提示；JVM 上就能用
  - **DnsOverHttps（DoH）**：DNS 查询本身走 HTTPS（如 Cloudflare 1.1.1.1/dns-query），公司网络/公共 DNS 看不到解析结果，无论 Java/Android 都建议优先 DoH；DoH 全局 shared 引导 client + `newBuilder()` 沿用连接池
  - **拦截器扩展**：仍是最好用的扩展点；5.4 起拦截器还能改缓存、连接池、DNS
  - **杂项修复**：multipart 某段 sink 关闭不再带崩整个请求体；HTTP/1 先刷请求体再摘超时；系统代理选择器抛异常改为不走代理不崩溃；默认主机名校验拒绝规范化失败的 IP；MockWebServer `@StartStop` 配合 JUnit5 `@Nested`
- **治理归属**：OkHttp 与 Retrofit、Okio、SQLDelight 一起加入 Commonhaus 基金会，换新签名密钥——依赖仍在被认真维护

## 关联连接
- [[摘要-okhttp-5.5]] — 来源（锋哥详解与三段 Java 实例）
- [[Dio]] — Dart/Flutter 生态的同类定位
- [[SSE]] — AI 客户端里同常见的流式 HTTP 形态
- Retrofit（上层封装，未建页，纯文本记录；OkHttp 与其、Okio、SQLDelight 同属 Commonhaus 基金会治理）
