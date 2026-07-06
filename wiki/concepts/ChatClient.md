---
title: "ChatClient"
type: concept
tags: [Spring AI, 聊天, API抽象]
sources: [raw/01-articles/SpringAI.md, raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md]
last_updated: 2026-07-06
---

## 定义
ChatClient 是 Spring AI 提供的高级聊天客户端接口，用于与 AI 聊天模型交互，封装了 prompt 构建、call/stream 调用等功能，提供更简洁的编程体验。

## 关键信息
- 通过 ChatClient.Builder 构建，支持自定义默认系统角色
- prompt().user(message).call().content() 链式调用
- 支持流式响应 stream().content() 返回 Flux
- tools(object) 注册 @Tool 注解的工具类，工具循环由 ToolCallingAdvisor 自动处理
- advisors 添加增强功能（如 MessageChatMemoryAdvisor 管理记忆、QuestionAnswerAdvisor 实现 RAG）
- 底层使用 ChatModel 作为属性，可指定不同的模型实现

### Spring AI 2.0 增强
- **ToolCallingAdvisor**：统一管理模型→调工具→再喂给模型的循环，框架自动注册
- **@Tool 注解**：定义工具最省心的方式，写在普通 Java 类的方法上
- **Advisor 链**：defaultAdvisors 可注册多个 Advisor（记忆/RAG/日志），每次调用自动生效
- **ChatMemory 集成**：MessageChatMemoryAdvisor 自动读写会话历史，无需手动拼 List

## 关联连接
- [[SpringAI]] — 所属框架
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 函数调用
- [[摘要-spring-ai]] — 来源
- [[摘要-spring-ai-2-agent-tips]] — 来源
- [[AdvisorChain]] — Advisor 链模式
