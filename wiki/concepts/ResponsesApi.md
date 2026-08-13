---
title: "ResponsesApi"
type: concept
tags: [AI, API, Agent, DeepSeek, OpenAI]
sources: [raw/09-archive/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md]
last_updated: 2026-08-13
---

## 定义

Responses API 是一种**有状态**的大模型调用接口，相比传统无状态的 Chat Completions API，可通过引用前一轮的 response ID 避免重传完整对话历史，并将 tool_calls 作为独立结构化数据返回，更适合 Agent 场景且能显著降低 Token 成本。

## 关键信息

### 与 Chat Completions API 的核心差异

| 维度 | Chat Completions | Responses API |
|------|------------------|---------------|
| 状态 | 无状态，每轮重传完整对话历史 | 有状态，引用前一轮 response ID |
| 工具调用返回 | 混在文本输出里，需 Harness 解析提取 | 独立结构化数据，与推理内容/最终回复分开返回 |
| Token 计费 | 每轮重传 System Prompt 和工具定义，按未命中价格收费 | 首次请求后，后续轮次引用前一轮 ID，静态前缀走缓存命中价 |
| Agent 适配 | 需文本解析，易出错 | Harness 直接读取结构化字段 |

### 为什么更适合 Agent
1. **省 Token**：不用每轮重传历史上下文，静态前缀走缓存命中价
2. **工具调用更可靠**：结构化返回避免文本解析错误
3. **长程任务友好**：引用 response ID 而非重传，避免上下文膨胀

### 支持情况
- [[DeepSeek]] V4 Pro 正式版（0813）和 V4-Flash 正式版（0731）均支持
- 可完美适配 [[Codex]] 等 Agent 工具
- Preview 版本不支持

## 关联连接
- [[DeepSeek]] — V4 Pro/Flash 正式版支持方
- [[Codex]] — 被适配的 Agent 工具
- [[Harness]] — Responses API 是 Harness 调用模型的核心接口
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — 来源
- [[摘要-deepseek-v4-flash发布]] — Flash 正式版首次支持 Responses API
