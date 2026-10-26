---
title: "TTL"
type: concept
tags: [网络协议, TCP/IP, 数据包]
sources: [raw/09-archive/2026-09-22 - ping 命令还能这么玩？.md]
last_updated: 2026-09-23
---

## 定义
TTL（Time To Live）是 IP 协议包的一个值，表示 DNS 记录在 DNS 服务器上存在的时间，也表示数据包在网络中可以存活的最大跳数。

## 关键信息
1. **基本作用**：告诉路由器该数据包何时需要被丢弃，防止数据包在网络中无限循环
2. **TTL 值与操作系统对应关系**：
   - Linux 系统：TTL 值为 64 或 255
   - Windows NT/2000/XP 系统：TTL 值为 128
   - Windows 98 系统：TTL 值为 32
   - UNIX 主机：TTL 值为 255
3. **判断范围**：
   - 100~130ms 之间：Windows 系统
   - 240~255ms 之间：UNIX/Linux 系统
4. **实际应用**：
   - 通过 ping 返回的 TTL 值粗略判断目标系统类型
   - 估算数据包经过的路由器数量
   - 诊断网络路由问题

## 关联连接
- [[ping命令]] — 主要应用工具
- [[网络连通性测试]] — 应用场景
- [[TCP-IP]] — 协议基础
- IP协议 — 相关协议
- 路由追踪 — 相关技术
