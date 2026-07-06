---
title: "摘要-solon-chatmodel-java-llm"
type: source
tags: [Solon, AI, Java, LLM]
sources: [raw/01-articles/2026-07-04-用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅.md]
last_updated: 2026-07-06
---

## 核心摘要
Solon 4.0 的 `ChatModel` 通过一套统一的 Builder API 封装了与不同 LLM 服务商交互的样板代码。文章从简单的同步调用到带记忆的流式聊天机器人，涵盖方言模式（Dialect Pattern）、ChatSession 对话记忆、ChatOptions 调优、多消息 Prompt 和 RAG 模式。支持 OpenAI、Ollama、Anthropic、Gemini、DashScope 等多模型提供商，并预告了工具调用、Talent 系统、ReActAgent/TeamAgent、RAG 流水线和 MCP 协议等高级能力。

## 关联连接
- [[SolonAI]] — 所属框架
- [[ChatSession]] — 对话记忆会话管理
- [[DialectPattern]] — 方言模式
- [[RAG]] — 检索增强生成
- [[ReAct_Agent]] — Agent 模式
- [[MCP]] — 模型上下文协议
- [[Ollama]] — 本地 LLM 部署
- [[DashScope]] — 阿里云通义大模型 API
