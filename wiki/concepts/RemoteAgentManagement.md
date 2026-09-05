---
title: "RemoteAgentManagement"
type: concept
tags: [Agent管理, 远程管理, SSH隧道, AgentBro]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

远程 Agent 管理是 AgentBro 通过 SSH 隧道统一管理远程开发机/服务器上 AI Agent 的能力。本地维护远程服务器列表，Agent 管理、诊断、Hooks 与事件接收共用同一条 SSH 连接。

## 核心原则

1. **统一管理入口**：本地与远程 Agent 在同一界面切换，不另开远程桌面
2. **SSH 单通道复用**：Agent 管理、Hooks、诊断共用一条 SSH 通道
3. **配置导入**：远程主机可手动添加，也可从 `~/.ssh/config` 自动导入

## 关键信息

**远程组件：** 远程服务器需安装 `agentbro-remote`
**TCP 隧道：** SSH 配置中建立，本地监听端口 7399，用于接收远程 Agent 事件

**当前限制（原文提及）：**
- 目前解决"从这台 Mac 管理远程 Agent"，不是跨设备/团队自动同步中心库
- 跨设备和团队同步尚未实现
- 项目级 Skill 管理、MCP 和 Plugins 的完整管理为后续版本规划

## 关联连接

- [[AgentBro]] — 核心工具
- [[AgentBroRemote]] — 远程组件实体