---
title: "AgentBroRemote"
type: entity
tags: [AgentBro组件, 远程管理, SSH隧道, agentbro-remote]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

AgentBro Remote 是 AgentBro 的远程管理组件，用于在本地 macOS 统一管理运行在远程开发机/服务器上的 AI Agent。它通过 SSH 隧道建立连接，复用同一条 SSH 通道进行 Agent 管理、Hooks 管理、诊断与事件接收。

## 关键信息

**部署要求：**
- 远程服务器需安装 `agentbro-remote`
- SSH 配置中建立 TCP 隧道，本地监听端口默认 7399，用于接收远程 Agent 事件

**管理能力：**
- 统一的远程服务器列表：主机可手动添加，也可从 `~/.ssh/config` 导入
- Agent 管理、诊断、Hooks 管理共用同一条 SSH 连接
- 本地可在本机与多台远程服务器之间切换当前管理环境
- 选中远程主机后，看到并管理的就是该机器上的 Agent，无需开远程桌面

**设计定位：**
- 解决"从这台 Mac 管理远程 Agent"，而非"跨设备/团队自动同步中心库"
- 跨设备和团队同步、项目级 Skill 管理、MCP 与 Plugins 完整管理均为后续版本规划

## 关联连接

- [[AgentBro]] — 核心产品
- [[RemoteAgentManagement]] — 远程管理概念
- [[SSHTunnel]] — SSH 隧道技术