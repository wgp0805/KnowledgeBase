---
title: "DialectPattern"
type: concept
tags: [AI, 方言模式, 模型适配, Solon]
sources: [raw/01-articles/2026-07-04-用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅.md]
last_updated: 2026-07-06
---

## 定义
方言模式（Dialect Pattern）是 Solon AI 中统一多 LLM 服务商协议的适配策略，通过 standard/provider 字段自动切换协议适配器，屏蔽不同服务商的 API 差异。

## 关键信息
- 通过 `standard` 或 `provider` 字段选择方言标识
- 支持方言：openai（默认, 兼容 DeepSeek/Qwen/GLM/Kimi）、ollama、anthropic、gemini、dashscope
- 用户只需指向兼容的 LLM 端点 URL 并指定方言，即可自动完成协议适配
- 与面向对象中的"接口多态"理念相似，将不同实现统一到同一调用接口

## 关联连接
- [[SolonAI]] — 方言模式所属框架
- [[摘要-solon-chatmodel-java-llm]] — 来源
