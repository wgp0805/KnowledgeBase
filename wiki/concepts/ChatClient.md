---
title: "ChatClient"
type: concept
tags: [Spring AI, 聊天, API抽象]
sources: [raw/01-articles/SpringAI.md]
last_updated: 2026-05-22
---

## 定义
ChatClient 是 Spring AI 提供的高级聊天客户端接口，用于与 AI 聊天模型交互，封装了 prompt 构建、call/stream 调用等功能，提供更简洁的编程体验。

## 关键信息
- 通过 ChatClient.Builder 构建，支持自定义默认系统角色
- prompt().user(message).call().content() 链式调用
- 支持流式响应 stream().content() 返回 Flux
- functions("funcName") 注册可调用的自定义函数
- advisors 添加增强功能（如 QuestionAnswerAdvisor 实现 RAG）
- 底层使用 ChatModel 作为属性，可指定不同的模型实现

## 关联连接
- [[SpringAI]] — 所属框架
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 函数调用
- [[摘要-spring-ai]] — 来源
