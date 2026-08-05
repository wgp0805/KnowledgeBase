---
title: "AI Registry"
type: concept
tags: [AI Agent, Nacos, MCP, 服务发现]
sources: [raw/01-articles/为什么越来越多人用Nacos？.md]
last_updated: 2026-08-05
---

## 定义
AI Registry 是 Nacos 3.0 引入的全新模块，与传统的服务注册、配置管理并列成为 Nacos 三大核心能力之一，使 Nacos 从"云原生应用平台"定位升级为"AI Agent 应用平台"。它的核心思想：微服务时代 Nacos 是"人与服务之间的电话簿"，AI Agent 时代 Nacos 要变成"**Agent 与工具之间的电话簿**"。

## 关键信息
### 三层架构
1. **模型层**：管理 AI 模型的动态参数（Prompt 模板、学习率、连接配置等），复用 Nacos 配置管理的分发能力。典型场景：线上 Prompt 模板热更新、多模型切换、A/B 测试不同 Prompt 版本。
2. **工具层**（最核心）：即 **MCP Registry**。让 LLM 模型和 MCP 工具之间实现自动发现、自动注册、智能检索。关键能力是通过智能过滤，减少传给大模型的工具描述数量，从而**降低 Token 消耗**。
3. **智能体层**：管理 AI Agent 的生命周期和元数据。

### 解决的问题
Agent 如何知道有哪些工具可用？如何知道每个工具的调用方式？如何动态发现新上线的工具？

## 关联连接
- [[Nacos]] — 所属系统
- [[MCP]] — MCP Registry 的底层协议
- [[Agent]] — 面向对象
- [[摘要-为什么越来越多人用Nacos]] — 来源
