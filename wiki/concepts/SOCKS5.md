---
title: "SOCKS5"
type: concept
tags: [网络协议, 代理, Python, RFC1929]
sources: [raw/01-articles/2026-08-23-同一个SOCKS5代理，为什么requests能用，aiohttp却一直报407 Proxy Authentication Required？.md]
last_updated: 2026-08-24
---

# SOCKS5

## 核心定义
一种网络代理协议，在传输层（TCP/UDP）进行代理转发。与 HTTP 代理不同，SOCKS5 的认证发生在协议级别（RFC 1929 用户名/密码认证），而非通过 HTTP 头部。

## 认证方式
- **RFC 1929**：用户名/密码认证，发生在 SOCKS5 协议握手阶段
- 不是 HTTP Basic Auth（通过 HTTP 头部传递）

## Python 库兼容性问题
同一个 SOCKS5 代理（用户名/密码认证）在不同库中表现不同：
- `requests` + `urllib3`：正常工作
- `curl`：正常工作
- `aiohttp` + `aiohttp-socks`：报 407 Proxy Authentication Required
- `httpx`：报 407

### 可能原因
1. 底层实现差异：`urllib3` 与 `aiohttp-socks` 的认证握手实现不同
2. 代理服务商兼容性：某些服务商要求特定的握手顺序或编码方式

### Scheme 差异
- `socks5h://`：DNS 也通过代理解析（requests 使用）
- `socks5://`：DNS 本地解析（aiohttp/httpx 使用）

## 关联连接
- [[Python]]
- [[代理认证]]
