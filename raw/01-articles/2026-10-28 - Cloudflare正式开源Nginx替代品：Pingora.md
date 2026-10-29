---
source_url: "https://mp.weixin.qq.com/s/zrYQqItmuOTqOmPbbOAxZQ"
title: "Cloudflare正式开源Nginx替代品：Pingora"
account: "终码一生"
published_at: "2026-10-28 23:00:58"
saved_at: "2026-10-29 07:21:33"
sync_id: "art_982e76fd3d094645928a38660b56dcf9"
parse_status: "ok"
---

# Cloudflare正式开源Nginx替代品：Pingora

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

早在 2022 年，Cloudflare 就宣布已将 Nginx 替换为内部采用 Rust 编写的 Pingora，目标是构建一个更快、更高效、更通用的内部代理，用作 Cloudflare 当前和未来产品的平台。

![图片](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/eaf7ba49d27aaf63f23c2c74843d9974_MD5.png)

现在，Cloudflare 正式开源了 Pingora 框架，源代码采用 Apache License，托管在 GitHub (https://github.com/cloudflare/pingora)。

![图片](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/02f325d14afc6e24692b20db5cb370e7_MD5.png)

Pingora 是一个 Rust 异步多线程框架，用于构建 HTTP 代理服务，已在 Cloudflare 内部使用多年，**据称每秒处理超过 4000 万个互联网请求**。

截至目前，Pingora 已在 Cloudflare 的全球网络中处理了近千万亿的互联网请求。

![](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/e3415148a9018e581714e7cf7e6c0289_MD5.png)

01

Pingora 主要特性

![](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/ea730ad34a93d53950aeb779339a74ef_MD5.png)

- 异步 Rust：快速且可靠
- HTTP 1/2 端到端代理
- 基于 OpenSSL 或 BoringSSL 的 TLS
- gRPC 和 websocket 代理
- 优雅的重新加载方式
- 可定制的负载均衡和故障转移策略
- 支持多种可观测性工具

![](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/881a8aea14790a031a3796c51f9cae68_MD5.png)

Cloudflare 团队写道：“我们正在开源 Pingora，以帮助在我们自己的基础设施之外构建一个更好、更安全的互联网。我们希望为我们的客户、用户和其他人提供工具、想法和灵感，以使用内存安全框架构建自己的互联网基础设施。”

![图片](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/499d64123b0ada3664299164c6c1ea7f_MD5.png)

根据介绍，Pingora 提供库和 API 来在 HTTP/1 和 HTTP/2、TLS 或 TCP/UDP 之上构建服务。

作为代理，它支持 HTTP/1 和 HTTP/2 端到端、gRPC 和 websocket 代理，**HTTP/3 支持也在规划当中**。它还具有可定制的负载平衡和故障转移策略。为了合规性和安全性，它支持常用的 OpenSSL 和 BoringSSL 库。

除了提供这些功能之外，Pingora 还提供 filters 和 callbacks，以允许用户完全自定义服务应如何处理、转换和转发请求。

在运行方面，Pingora 提供**零停机优雅重启**，可在不丢弃任何传入请求的情况下进行自我升级。Syslog、Prometheus、Sentry、OpenTelemetry 和其他必备的可观测工具也可以轻松与 Pingora 集成。

值得注意的是，Pingora 尚处于 1.0 之前的阶段，不具备 API 稳定性，且 Cloudflare 目前没有计划支持非 Unix 操作系统。

Cloudflare 工程师看起来非常热爱 Rust 语言，去年他们使用 Rust 重写 Nginx C 模块，谈到了 Rust 带来的好处：

“大多数人认为编程语言的安全性主要是用于预防出现 bug，但对于一家公司来说，我们发现编程语言的安全优势还可以用来完成一些被认为非常困难、或不可能安全实现的功能需求。比如提供类似 Wireshark 的过滤语言来编写防火墙规则、允许数百万用户编写任意 JavaScript 代码并直接在我们的平台上运行它，以及即时重写 HTML 响应。

在实现上述功能过程中，Rust 为这些服务提供了严格的执行边界，让不可能变成可能。与此同时，Rust 让过去困扰行业的内存安全问题日益成为过去。”

不过曾参与 Cloudflare 架构工作的 OpenResty 作者章亦春则指出是因为 Cloudflare 的新工程师“搞不定” Nginx——所以用 Rust 重新造了轮子，并表示他们用 Rust 写解释型网关是退步了。

![图片](assets/2026-10-28%20-%20Cloudflare%E6%AD%A3%E5%BC%8F%E5%BC%80%E6%BA%90Nginx%E6%9B%BF%E4%BB%A3%E5%93%81%EF%BC%9APingora/02fc277ae628802e6b6477db55bf173a_MD5.jpg)

02

相关链接

- https://blog.cloudflare.com/pingora-open-source
- https://www.zhihu.com/question/554595029/answer/2683793513

---
原文链接：https://mp.weixin.qq.com/s/zrYQqItmuOTqOmPbbOAxZQ
