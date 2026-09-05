---
title: "SSHTunnel"
type: concept
tags: [概念, SSH, 网络, 安全]
sources: []
last_updated: 2026-08-03
---

## 定义
SSH 隧道（SSH Tunneling / Port Forwarding）是利用 SSH 加密连接在本地与远程主机之间转发 TCP 流量的技术，可将远程服务安全地暴露到本地，或在受限网络间建立加密通道。

## 关键信息
- **三种类型**：本地转发（Local Forwarding，远程端口→本地）、远程转发（Remote Forwarding）、动态转发（SOCKS 代理）
- **典型用途**：远程服务器 Agent 管理（如 [[AgentBroRemote]] 通过 SSH 隧道统一管理远程 Agent）、数据库安全访问、绕过网络限制
- **安全性**：流量走 SSH 加密，规避明文暴露与中间人攻击
- **工具**：OpenSSH `-L/-R/-D` 参数、跳板机（Jump Host）

## 关联连接
- [[AgentBroRemote]] — 远程管理应用场景
- [[Linux]] — SSH 常用平台
- [[distributed-tracing]] — 相关网络架构概念（间接）
