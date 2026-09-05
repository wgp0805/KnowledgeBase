---
title: "gateway-messaging"
type: concept
tags: [AI, Agent, 消息, 架构]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
消息网关（Gateway Messaging）是 AI Agent 的多平台消息接入层，支持将 Agent 的能力通过 Telegram、微信、邮箱、Discord、Slack 等多种即时通讯平台暴露给用户。

## 关键信息
- **核心功能**：消息路由、权限控制、多平台适配
- **代表系统**：Hermes Agent 支持 23+ 消息平台
- **架构特点**：平台适配层 + 统一消息路由 + 配对与权限管理

## 关联连接
- [[HermesAgent]] — 支持 Gateway Messaging 的 Agent
- [[摘要-hermes-agent-complete-guide]] — 来源
