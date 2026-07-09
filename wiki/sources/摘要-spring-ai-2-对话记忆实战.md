---
title: "摘要-spring-ai-2-对话记忆实战"
type: source
tags: [来源, Spring AI, 实战教程, 对话记忆]
sources:
  - raw/01-articles/Spring AI 2.0真香！.md
last_updated: 2026-07-09
---

## 核心摘要

苏三（macrozheng 代码）带来的 [[SpringAI]] 2.0 实战教程：三步（引入 Starter 依赖、配置模型参数、注入 [[ChatClient]] 调用）即可搭建 AI 对话服务，支持同步 `call()` 与 SSE 流式 `stream()` 输出。通过引入 [[ChatMemory]] 并对接 [[Redis]]（需 redis-stack 而非普通版本，用 `MessageWindowChatMemory` + `RedisChatMemoryRepository`），实现多轮对话记忆，绑定 conversationId 管理会话历史。配置通过 OpenAI 兼容协议接入 [[DeepSeek]] V4 Pro 模型。

## 关键信息

- 依赖：spring-ai-bom 2.0.0、spring-ai-starter-model-openai、spring-boot-starter-webflux（SSE）
- 模型：通过 OpenAI 兼容接口访问 DeepSeek（base-url=api.deepseek.com，model=deepseek-v4-pro）
- 对话记忆存储后端：内存、JDBC、Neo4j、MongoDB、Redis 等；示例用 Redis（redis-stack:7.4.0-v8）
- ChatMemory API：add 添加记忆、get 获取历史、clear 清空，均绑定 conversationId
- 流式输出：`TEXT_EVENT_STREAM_VALUE`，用 `Flux<ChatEventDto>` 包装 SSE 事件

## 关联连接

- [[SpringAI]] - 所属框架
- [[苏三]] - 文章作者
- [[ChatClient]] - 聊天客户端
- [[ChatMemory]] - 对话记忆管理
- [[Redis]] - 记忆存储后端
- [[DeepSeek]] - 接入的模型
- [[AdvisorChain]] - Advisor 链模式
- [[摘要-spring-ai-2-agent-tips]] - 相关 Agent 实践
