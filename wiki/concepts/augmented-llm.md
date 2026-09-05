---
title: "augmented-llm"
type: concept
tags: [AI, LLM, Agent, 架构]
sources: [raw/01-articles/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md]
last_updated: 2026-07-22
---

## 定义
增强型 LLM（Augmented LLM）是在原生 LLM 基础上叠加检索、工具、记忆三大核心能力所形成的基础 Agent 构建单元。它让 LLM 不再局限于训练数据中的知识，能够从外部检索信息、调用工具执行操作、记住跨会话的上下文。

## 关键信息
- **三大增强支柱**：检索（RAG/搜索）、工具（Function Calling/MCP）、记忆（会话/持久）
- **检索增强**：从外部知识库检索相关信息
- **工具增强**：通过 Function Calling 调用外部 API
- **记忆增强**：跨会话持久化关键信息
- **定位**：构建 Agent 系统的基础单元，所有高级工作流和编排模式的基石

## 关联连接
- [[Agent]] — AI Agent 核心概念
- [[RAG]] — 检索增强
- [[FunctionCalling]] — 工具调用
- [[MCP]] — 模型上下文协议
- [[摘要-agent-engineering]] — 来源
