---
title: "摘要：SOCKS5代理在requests能用但aiohttp报407的问题"
type: source
tags: [Python, SOCKS5, 代理, aiohttp, httpx, requests, 网络编程]
sources: [raw/01-articles/2026-08-23-同一个SOCKS5代理，为什么requests能用，aiohttp却一直报407 Proxy Authentication Required？.md]
last_updated: 2026-08-24
---

# 摘要：SOCKS5代理认证的库兼容性问题

## 核心问题
同一个 SOCKS5 代理（用户名/密码认证），在 `requests` 和 `curl` 中正常工作，但在 `aiohttp` 和 `httpx` 中报 407 Proxy Authentication Required。

## 原因分析
1. **底层实现差异**：`requests` 底层依赖 `urllib3`，`aiohttp` 使用 `aiohttp-socks`，两者的 SOCKS5 认证握手实现可能有差异。
2. **认证层级**：SOCKS5 的用户名/密码认证发生在协议级别（RFC 1929），不是 HTTP Basic Auth（通过 HTTP 头部）。
3. **代理服务商兼容性**：某些代理服务商（如 9HTTP）的 SOCKS5 认证可能要求特定的握手顺序或编码方式，与 `aiohttp-socks`/`httpx` 的实现不完全兼容。

## 关键信息
- 代理协议：SOCKS5（RFC 1929 用户名/密码认证）
- 测试版本：aiohttp 3.8.0-3.10.0，httpx 多个版本，现象一致
- `requests` 使用 `socks5h://` scheme（h 表示 DNS 也通过代理解析）
- `aiohttp`/`httpx` 使用 `socks5://` scheme

## 原始信息
- **来源**: SegmentFault
- **链接**: https://segmentfault.com/q/1010000048194115
- **抓取日期**: 2026-08-23

## 关联连接
- [[SOCKS5]]
- [[Python]]
- [[aiohttp]]
- [[httpx]]
- [[requests]]
- [[代理认证]]
