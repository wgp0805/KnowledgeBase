---
title: "OpenRouter"
type: entity
tags: [AI, 模型聚合, API网关]
sources: [raw/01-articles/“牛来”员工：你们可以在 OpenCode 爽用 Ox Alpha 模型了，1M上下文并支持视频输入（附Agent面试题）.md]
last_updated: 2026-08-24
---

## 定义
OpenRouter 是大模型聚合路由平台，通过统一 API 聚合多家厂商模型，用户配一个 Key 即可访问和切换数百个模型。

## 关键信息
- [[OxAlpha]] 在 OpenRouter 上以模型 ID `ox-alpha` 提供（2026-08）
- 知识库中多个工具将其作为 BYOK 中转渠道：[[Junie]] 的 BYOK 明确支持 OpenRouter，可曲线使用 DeepSeek/Qwen/GLM 等国产模型；AionUi、pi-agent、Hermes Agent 等亦内置其路由支持
- 同一模型经不同 Provider（如 OpenRouter vs OpenCode Zen）调用时，Agent 效果可能不同——Provider 会在 API 层做 system prompt 注入、参数覆盖、工具调用格式转换、限流超时策略等"加工"

## 关联连接
- [[摘要-ox-alpha模型与agent面试题]] — 来源
- [[OxAlpha]] — 托管的免费预览模型
- [[LLM网关]] — 同类概念（企业级自建网关）
- [[Junie]] — 通过 OpenRouter 中转国产模型的典型场景
