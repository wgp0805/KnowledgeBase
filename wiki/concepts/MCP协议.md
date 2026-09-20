---
title: "MCP协议"
type: concept
tags: [概念, 协议, Agent, 工具接入]
sources: [raw/01-articles/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md]
last_updated: 2026-09-20
---

## 定义
MCP（Model Context Protocol，模型上下文协议）是 Anthropic 提出的开放协议，用于标准化 Agent 与外部工具/数据源的连接方式，解决"每个 Agent 都要为每个工具写适配器"的碎片化问题。

## 关键信息
- **核心思想**：把工具接入标准化，一次实现到处复用
- **与 Function Calling 关系**：正交关系，工具形态/接入协议/路由策略是三个独立维度
  - Function Calling 是模型调用工具的方式（工具形态）
  - MCP 是工具接入的协议（接入协议）
  - 路由策略决定用哪个工具（路由策略）
- **应用**：Claude Code、Codex 等主流 Agent 均支持 MCP 连接外部服务

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[MCP]] — 相关实体
- [[FunctionCalling]] — 正交关系
- [[工具路由]] — 独立维度
- [[Agent]] — 应用场景