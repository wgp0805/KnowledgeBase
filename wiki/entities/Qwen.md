---
title: "Qwen"
type: entity
tags: [AI模型, 阿里云, 通义千问]
sources: [raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md]
last_updated: 2026-06-30
---

## 定义
Qwen 是阿里通义千问大模型系列，文章中主要提到 Qwen3.6 Flash 在 Coding Agent 和源码解读任务中的表现。

## 关键信息
- Qwen3.6 Flash 被用于“源码解读并生成 HTML 架构分析报告”的多轮工具调用任务。
- 文章认为 Qwen3.6 Flash 能一次对话完成任务，源码总结质量可用，但执行过程中出现多次工具调用失败，需要模型自修复。
- 与 Step 3.7 Flash 对比时，Qwen3.6 Flash 的输出 token 更多、API 时间更长、估算成本略高。
- 在横向表中，Qwen3.6 Flash 的工具调用稳定性低于 Step 3.7 Flash、DeepSeek V4 Flash 和 Gemini 3.5 Flash，但错误自修复能力仍被评价为高。

## 关联连接
- [[摘要-step-3-7-flash-agent横评]] — 来源
- [[Step3Flash]] — 横评对比模型
- [[DeepSeek]] — 横评对比模型
- [[Gemini]] — 横评对比模型
- [[AICoding]] — Coding Agent 应用场景
