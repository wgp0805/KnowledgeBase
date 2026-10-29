---
title: "摘要-cloudflare开源pingora"
type: source
tags: [来源, 反向代理, Rust, Cloudflare, Nginx, 开源]
sources: [raw/09-archive/2026-10-28 - Cloudflare正式开源Nginx替代品：Pingora.md]
last_updated: 2026-10-29
---

## 核心摘要
Cloudflare 于 2022 年就用 Rust 编写的内部代理 Pingora 替换了 Nginx，如今正式以 Apache License 开源（github.com/cloudflare/pingora）。Pingora 是一个 Rust 异步多线程框架，用于构建 HTTP 代理服务，据称每秒处理超过 4000 万个互联网请求，累计处理近千万亿请求。它提供零停机优雅重启、可定制的负载均衡与故障转移、gRPC/WebSocket 代理，以及 Prometheus/Sentry/OpenTelemetry 等可观测性集成。官方动机不止"更快"，而是用内存安全框架让原本被认为难以安全实现的功能变成可能。本文同时记录了 OpenResty 作者章亦春的反面观点：这更像是"搞不定 Nginx"后的重造轮子。

## 关键信息

### 时间线与规模
| 节点 | 内容 |
|------|------|
| 2022 年 | Cloudflare 宣布用 Rust 写的 Pingora 替换 Nginx |
| 开源时 | 正式开源框架本体，Apache License，托管于 GitHub |
| 吞吐 | 每秒处理超 4000 万个互联网请求 |
| 累计 | 已在全球网络处理近千万亿请求 |

### 核心特性
- **异步 Rust**：快速且可靠
- **协议支持**：HTTP/1 与 HTTP/2 端到端代理，gRPC、WebSocket；HTTP/3 在规划中
- **TLS**：基于 OpenSSL 或 BoringSSL（合规与安全考量）
- **优雅重载**：零停机自我升级，不丢弃任何传入请求
- **可定制负载均衡与故障转移策略**
- **可观测性**：Syslog、Prometheus、Sentry、OpenTelemetry 可轻松集成
- **可编程性**：除库与 API（可在 HTTP/1、HTTP/2、TLS、TCP/UDP 之上构建服务）外，还提供 filters 与 callbacks，允许完全自定义请求的处理、转换与转发

### 现状限制
- 尚处于 1.0 之前阶段，**不具备 API 稳定性**
- Cloudflare 目前**没有计划支持非 Unix 操作系统**（Windows 不可用）

### 官方动机：Rust 的价值不止于防 Bug
Cloudflare 工程师的说法值得单独记录：大多数人认为语言安全性主要用于预防 Bug，但对企业而言，语言的安全优势还能用来完成"被认为非常困难、或不可能安全实现"的功能需求，例如：

1. 提供类似 **Wireshark 的过滤语言**来编写防火墙规则
2. 允许 **数百万用户编写任意 JavaScript** 并直接在平台上运行
3. **即时重写 HTML 响应**

在实现这些功能的过程中，Rust 为服务提供了严格的执行边界，"让不可能变成可能"，并让内存安全问题日益成为过去。

### 反方观点（章亦春）
曾参与 Cloudflare 架构工作的 [[OpenResty]] 作者章亦春指出：这更像是 Cloudflare 的新工程师"搞不定" Nginx，所以用 Rust 重新造了轮子；并认为用 Rust 写解释型网关是一种**退步**。

> 这条批评与官方叙事构成一对张力：一边是"内存安全解锁新能力"，一边是"工程成熟度与抽象层次的倒退"。两者无法用跑分证伪，属于典型的技术路线分歧，参见 [[Pingora]] 的「争议」小节。

## 关联连接
- [[Pingora]] — 本文主角（Cloudflare 的 Rust 代理框架）
- [[Nginx]] — 被替代对象
- [[Cloudflare]] — 出品方
- [[Rust]] — 实现语言
- [[OpenResty]] — 反方观点的技术背景（Nginx + Lua 扩展路线）
- [[反向代理]] — 所属技术类别
- [[摘要-王者荣耀-为什么不用微服务]] — 同一公众号（终码一生）的另一篇转载
