---
title: "摘要-okhttp-5.5"
type: source
tags: [来源, OkHttp, Java, HTTP客户端, ECH, DoH, 锋哥]
sources: [raw/09-archive/2026-10-22 - 为什么越来越多人使用 OkHttp 5.5 ？.md]
last_updated: 2026-10-23
---

## 核心摘要
公众号 java1234 的锋哥（2026-10-22）解析 OkHttp 5.5 为什么正从「Android 的库」变成 JVM 通用 HTTP 客户端：Spring 服务调外部接口、定时任务拉数据、桌面工具发请求的 `pom.xml` 里越来越常出现 okhttp——很多人还是通过 Retrofit 间接用上它。三个重点：①**okhttp-jvm 坑**：5.0 起 JVM 与 Android 拆为两套产物，Gradle 写 `com.squareup.okhttp3:okhttp` 会自动选 JVM 包，Maven 认普通 POM，空的 `okhttp` 构件里没有 class，Java 项目必须显式依赖 `okhttp-jvm`（建议用 BOM 锁版本）；②**加密 DNS**：普通 HTTPS 不加密握手最初段的 SNI，5.5 选配 ECH（Encrypted Client Hello）把访问域名也加密，但系统 TLS 栈得支持（目前只有 Android 17/API 37 满足，JDK 的 TLS 还没接上）；为此 5.5 重做了 DNS 层——支持查 HTTPS 记录、结果异步流式返回、带内存缓存、返回 ECH 配置/ALPN/端口等服务元数据，Java 服务用 `DnsOverHttps`（DoH，如 Cloudflare 1.1.1.1）即可先享受加密解析，不在意隐私也建议优先 DoH；③JDK 自带 HttpClient 简单请求够用，但连接池、HTTP/2、拦截器、失败重试、同步 `execute()` 与异步 `enqueue()` 并存这些能力让 OkHttp 在后端、批处理和中间件里越来越常见。详见 [[OkHttp]] 实体页。

## 关联连接
- 作者：锋哥（公众号 java1234，未建实体页，纯文本记录）
- [[OkHttp]] — 项目本体
- [[SpringBoot]] — JVM 使用场景
- ECH/DoH/SNI 未单独立页（纯文本记录）
- [[幂等性]] — 失败重试语境的既有概念页
