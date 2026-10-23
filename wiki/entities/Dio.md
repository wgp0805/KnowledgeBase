---
title: "Dio"
type: entity
tags: [HTTP客户端, Dart, Flutter, 网络请求]
sources: [raw/09-archive/2026-10-22-纯原生Flutter3 + Dio 实战 DeepSeek V4.1 SSE流式对话 - yxybox.md]
last_updated: 2026-10-23
---

## 定义
Dio 是 Dart/Flutter 生态最流行的 HTTP 客户端库（当前 ^5.11.1），支持请求拦截、FormData、断点续传、超时与 **SSE 流式响应**处理。

## 关键信息
- 在 Flutter AI 对话应用中，Dio 承担对 DeepSeek 等 LLM API 的流式请求，把字节流交给上层状态管理逐字渲染
- 常与 flutter_dotenv 组合管理 `DEEPSEEK_BASE_URL` / API Key 等敏感配置
- 在 AI 客户端场景下的替代方案：直接使用模型的 OpenAI 兼容端点 + `stream: true`（详见 [[DeepSeek-V4.1-Flash]] 的接入实证）
- 与 Java 生态的 [[OkHttp]] 定位类似：都是"应用与网站之间的交通调度"，处理连接、TLS、重试与流式读取

## 关联连接
- [[Flutter]] — 主要使用场景
- [[SSE流式输出]] — 流式请求的核心机制
- [[DeepSeek-V4.1-Flash]] — 实战对接的模型
- [[摘要-flutter-dio-deepseek-sse]] — 来源
- [[OkHttp]] — Java 生态里的同类角色
