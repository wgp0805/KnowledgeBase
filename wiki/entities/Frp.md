---
title: "Frp"
type: entity
tags: [网络, 内网穿透, Go, 开源工具]
sources: [raw/01-articles/常见内网穿透工具，收好了！.md]
last_updated: 2026-08-12
---

## 定义
frp（Fast Reverse Proxy）是一个高性能的反向代理工具，使用 Go 语言开发，由 fatedier 开源。专注于内网穿透，配置极简（一个 ini 文件），支持 TCP/UDP/HTTP/HTTPS/STCP 协议和 P2P 穿透。

## 关键信息
- **架构**：frps（公网服务端）+ frpc（内网客户端）
- **配置**：单 ini 配置文件，极简上手
- **协议**：TCP、UDP、HTTP、HTTPS、STCP（安全 TCP）、XTCP（P2P）
- **部署**：二进制直接运行，支持 systemd 管理
- **社区**：GitHub 80k+ Stars，社区活跃度高

## 关联连接
- [[内网穿透]] — 核心概念
- [[Nps]] — 同类工具对比
- [[Ngrok]] — 同类工具对比
- [[EarthWorm]] — 同类工具对比
- [[Golang]] — 开发语言
- [[摘要-常见内网穿透工具]] — 来源文章
