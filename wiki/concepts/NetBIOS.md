---
title: "NetBIOS"
type: concept
tags: [网络协议, Windows, 局域网]
sources: [raw/09-archive/2026-09-22 - ping 命令还能这么玩？.md]
last_updated: 2026-09-23
---

## 定义
NetBIOS（Network Basic Input/Output System）是一种网络协议，主要用于局域网内的计算机之间的通信和名称解析。

## 关键信息
1. **基本功能**：
   - 提供计算机名称解析服务
   - 支持局域网内的文件和打印机共享
   - 允许应用程序通过网络进行通信
2. **ping 命令中的应用**：
   - `ping -a` 参数可以解析计算机名与 NetBIOS 名
   - 通过 IP 地址反向解析出主机名
3. **工作原理**：
   - 使用 UDP 端口 137（名称服务）和 138（数据报服务）
   - 使用 TCP 端口 139（会话服务）
4. **安全考虑**：
   - NetBIOS 存在安全漏洞，可能被用于网络攻击
   - 在非必要情况下建议禁用 NetBIOS
   - 现代网络更多使用 DNS 进行名称解析

## 关联连接
- [[ping命令]] — 应用场景
- [[TCP-IP]] — 协议基础
- DNS — 替代协议
- Windows网络 — 应用环境
- 局域网 — 网络类型
