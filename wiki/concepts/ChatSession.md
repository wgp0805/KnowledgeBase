---
title: "ChatSession"
type: concept
tags: [AI, 对话记忆, 会话管理, LLM]
sources: [raw/01-articles/2026-07-04-用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅.md]
last_updated: 2026-07-06
---

## 定义
ChatSession 是 AI Agent 框架中管理多轮对话记忆的会话对象，自动维护 LLM 调用所需的历史上下文，无需开发者手动拼接消息列表。

## 关键信息

### Solon AI 实现
- `InMemoryChatSession` — 本地 Map 存储，适合开发与单节点部署
- `FileChatSession` — 文件系统持久化，适合 CLI 工具与桌面应用
- `RedisChatSession` — Redis 存储，适合生产环境分布式部署
- 支持会话 ID 隔离、最大消息数裁剪（maxMessages）

### 典型用法
通过 sessionId 隔离用户会话，对话前附加 session 对象即可自动注入历史上下文。

## 关联连接
- [[SolonAI]] — Solon AI 实现
- [[ChatMemory]] — 对话记忆管理概念
- [[ContextManagement]] — 上下文管理策略
- [[摘要-solon-chatmodel-java-llm]] — 来源
