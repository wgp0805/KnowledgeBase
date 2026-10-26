---
title: "AI Registry"
type: concept
tags: [AI Agent, Nacos, MCP, 服务发现]
sources: [raw/09-archive/为什么越来越多人用Nacos？.md, raw/09-archive/2026-09-27-当 AI Agent 遇到 Nacos：OpenClaw.NET 集成入门 - 张善友.md]
last_updated: 2026-09-28
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

### 治理对象与工具开关（Nacos 3.2.4，来源：[[摘要-openclaw-net-nacos集成]]）
- 管理对象：**Skill、Agent、MCP Server、Prompt、AgentSpec** 的注册、治理、按版本发布与运行时发现
- 判定原则：**AI 资源不是配置，也不是普通服务**——配置管理关心内容发布与监听，服务发现关心实例健康；MCP Server 治理重点是协议类型、端点、版本与**工具开关**（`toolSpec.ToolsMeta`），管理员可在控制台关闭某工具，运行时必须遵守
- 消费方式之一：Nacos **MCP Router** 模式（如 `NacosMcpRouter`），对 Agent 暴露 search / add / use 三个工具，用本地向量检索完成发现，全程零 LLM 调用（见 [[OpenClawNET]]）

## 关联连接
- [[Nacos]] — 所属系统
- [[MCP]] — MCP Registry 的底层协议
- [[Agent]] — 面向对象
- [[OpenClawNET]] — 治理能力的消费方
- [[摘要-为什么越来越多人用Nacos]] — 来源
- [[摘要-openclaw-net-nacos集成]] — 治理对象与工具开关来源
