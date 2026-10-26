---
title: "摘要-spring-ai-alibaba-文生图文生音向量化"
type: source
tags: [来源, 原始文件]
sources: ["raw/09-archive/2026-10-23-Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP.md"]
last_updated: 2026-10-26
---

## 核心摘要
Spring AI Alibaba 实战教程（NE_STOP 系列），基于 `spring-ai-alibaba-starter-dashscope` 演示四大能力。① ChatMemory 对话记忆：论断 LLM 无状态、服务重启记忆即丢必须持久化，用 `spring-ai-alibaba-starter-memory-redis` + Jedis 构建 `RedisChatMemoryRepository`，配 `MessageWindowChatMemory(maxMessages=10)` + `MessageChatMemoryAdvisor`，调用时以 `advisorSpec.param("conversationId", userId)` 按用户隔离会话，并在同一 api-key 下配 deepseek-v3 / qwen-max 双模型 Bean；② 文生图：`ImageModel` + `DashScopeImageOptions` 调 `wanx2.1-t2i-turbo`（通义万相 Wan 系列）返回图片 URL；③ 文生音：`SpeechSynthesisModel` 调 `cosyvoice-v2`（音色 longyingcui），返回 ByteBuffer 音频写入 mp3；④ 向量化：`EmbeddingModel` 调 `text-embedding-v3`，经 `spring-ai-starter-vector-store-redis` 把文档存入 Redis Stack 向量库并做 topK=10 相似度检索。文末论断：Redis Stack = 原生 Redis + 官方扩展模块（含 RediSearch），Redis 8.0 起模块内置原版、Redis Stack 独立包已弃用。

## 关联连接
- [[SpringAI_Alibaba]] — 主角框架（模型接入 + 记忆持久化 starter）
- [[SpringAI]] — ChatClient/ChatModel/ImageModel/SpeechSynthesisModel/EmbeddingModel 接口体系
- [[DashScope]] — 底层模型 API 平台（chat/文生图/文生音/向量化）
- [[ChatMemory]] — 对话记忆概念与 Redis 持久化
- [[ChatClient]] — ChatClient + Advisor 调用范式
- [[AdvisorChain]] — MessageChatMemoryAdvisor 顾问机制
- [[Redis]] — 记忆持久化 + Redis Stack/8.0 向量检索底座
- [[向量数据库]] — 概念定义与产品清单（PGvector/Elasticsearch 等）
- [[VectorStore]] — Spring AI 向量库接口
- [[Embeddings]] — 文本向量化（text-embedding-v3）
- [[RAG]] — 相似度检索支撑 RAG 应用
- [[pgvector]] — 文中列举的向量数据库之一
- [[摘要-spring-ai-2-对话记忆实战]] — 同主题 Spring AI 2.0 侧 Redis 记忆实战（含 Redis Stack 版本说法更新点）
- [[摘要-spring-ai-alibaba停更分析]] — SAA 系列背景（"养护模式"下的教程实践）
