---
title: "Pingora"
type: entity
tags: [反向代理, Rust, Cloudflare, 开源, 网关]
sources: [raw/09-archive/2026-10-28 - Cloudflare正式开源Nginx替代品：Pingora.md]
last_updated: 2026-10-29
---

## 定义
Pingora 是 Cloudflare 用 Rust 编写的异步多线程 HTTP 代理框架，用于构建代理服务与其内部代理平台。它自 2022 年起在 Cloudflare 生产环境替代 [[Nginx]]，并已正式开源（Apache License，github.com/cloudflare/pingora）。它既是可复用的**框架/库**（在 HTTP/1、HTTP/2、TLS、TCP/UDP 之上构建服务），也是可直接运行的**代理**。

## 关键信息

### 定位
- **不是 Nginx 的配置兼容替代品**，而是一个用代码描述代理行为的 Rust 框架 —— 这对运维团队意味着"从写 nginx.conf 变成写 Rust 服务"
- 面向的场景：需要深度定制请求处理、负载均衡与故障转移策略的大型边缘网络

### 能力清单
| 维度 | 支持情况 |
|------|----------|
| 协议 | HTTP/1、HTTP/2 端到端；gRPC；WebSocket；HTTP/3 规划中 |
| 传输 | TLS（OpenSSL 或 BoringSSL）、TCP/UDP |
| 负载均衡 | 策略可定制，含故障转移 |
| 扩展能力 | filters + callbacks，完全自定义请求的处理、转换与转发 |
| 重载 | **零停机优雅重启**，自我升级不丢请求 |
| 可观测性 | Syslog、Prometheus、Sentry、OpenTelemetry 可集成 |

### 规模数据（官方口径）
- 每秒处理超过 **4000 万**个互联网请求
- 累计处理近 **千万亿**（10^15 量级）请求

### 采用边界
- 处于 **1.0 之前**，不具备 API 稳定性
- **仅支持 Unix 类系统**，官方暂不计划支持非 Unix 操作系统（Windows 不可用）

### 争议：路线之争而非跑分之争
- **官方叙事**：Rust 的内存安全不只是防 Bug，而是让"被认为不可能安全实现"的功能成为可能 —— 用类 Wireshark 的过滤语言写防火墙规则、让数百万用户跑任意 JavaScript、即时重写 HTML 响应
- **反方（[[章亦春]]）**：Cloudflare 的新工程师"搞不定" Nginx，才用 Rust 重新造轮子；且用 Rust 写**解释型网关**是退步（参见 [[OpenResty]] 的 Lua 扩展路线）
- 判断要点：这类分歧无法靠吞吐跑分裁决，取决于团队是否能长期维护 Rust 代码、以及是否需要 Pingora 那种"把代理逻辑写成程序"的定制深度

## 关联连接
- [[Cloudflare]] — 出品方，也是唯一的大规模生产验证方
- [[Nginx]] — 被替代对象（2022 年起）
- [[Rust]] — 实现语言（异步多线程）
- [[OpenResty]] — 竞争路线：Nginx + Lua 的扩展范式
- [[章亦春]] — 主要批评者
- [[反向代理]] — 所属技术类别
- [[摘要-cloudflare开源pingora]] — 来源
