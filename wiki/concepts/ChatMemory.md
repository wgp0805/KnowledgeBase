---
title: "ChatMemory"
type: concept
tags: [AI, 对话记忆, 上下文]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md]
last_updated: 2026-05-19
---

## 定义
让无状态的 LLM 拥有"上下文"的机制，通过维护历史消息并在每次调用时重新注入，实现多轮对话的连贯性。

## 关键信息

### LangChain4j 实现
- `@MemoryId` 区分不同用户/会话，每个 ID 对应独立记忆
- `MessageWindowChatMemory`：滑动窗口策略，按消息数裁剪
- `TokenWindowChatMemory`：按 token 预算裁剪，更精准
- `ChatMemoryStore` 接口支持持久化到 Redis/MySQL/自建数据库

### 与 Agent 记忆的关系
ChatMemory 是对话级短期记忆（一次会话内），CLAUDE.md/Auto Memory 是跨会话的长期记忆。

## 关联连接
- [[LangChain4j]] — ChatMemory 框架
- [[RAG]] — 检索增强（长期知识）
- [[CLAUDEmd]] — 长期指令记忆
- [[ContextManagement]] — 上下文管理策略
