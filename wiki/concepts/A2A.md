---
title: "A2A"
type: concept
tags: [AI, Agent, 协议, 通信]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
Agent-to-Agent 协议，实现分布式 Agent 间通信和编排，是 MCP 之外的另一种 Agent 互操作协议。

## 关键信息
- Spring AI Alibaba 通过 Nacos 实现 A2A 分布式 Agent 间通信
- AgentScope-Java 支持 A2A 实现跨进程 Agent 编排
- A2A 与 MCP 互补：MCP 解决 Agent 与外部工具/服务的连接，A2A 解决 Agent 与 Agent 之间的协作
- 支持跨服务、跨进程的 Agent 调用与编排

## 关联连接
- [[MCP]] — 互补协议（Agent-工具 vs Agent-Agent）
- [[SpringAI_Alibaba]] — A2A 实现框架
- [[AgentScope_Java]] — A2A 支持框架
- [[Agent]] — 所属核心概念
- [[摘要-java-ai框架选型指南-2026]] — 来源
