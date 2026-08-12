---
title: "Nps"
type: entity
tags: [网络, 内网穿透, Go, 开源工具]
sources: [raw/01-articles/常见内网穿透工具，收好了！.md]
last_updated: 2026-08-12
---

## 定义
nps 是一款使用 Go 语言开发的轻量级内网穿透工具，由 ehang-io 开源。采用 C/S 架构（nps 服务端 + npc 客户端），提供 Web 管理面板，支持 TCP/UDP/HTTP/HTTPS/SOCKS5 多协议隧道。

## 关键信息
- **架构**：nps（公网服务端）+ npc（内网客户端）
- **管理**：内置 Web 可视化管理面板，支持多客户端、多隧道
- **协议**：TCP、UDP、HTTP、HTTPS、SOCKS5 代理
- **部署**：支持 Docker 一键部署，跨平台（Windows/Linux/Mac）
- **特性**：域名解析、内网穿透、P2P 穿透、流量统计

## 关联连接
- [[内网穿透]] — 核心概念
- [[Frp]] — 同类工具对比
- [[Ngrok]] — 同类工具对比
- [[EarthWorm]] — 同类工具对比
- [[Golang]] — 开发语言
- [[摘要-常见内网穿透工具]] — 来源文章
