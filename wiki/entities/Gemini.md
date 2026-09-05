---
title: "Gemini"
type: entity
tags: [Google, AI, 大模型, 长上下文]
sources: [raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md, raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md]
last_updated: 2026-06-30
---

## 定义
Gemini 是 Google 推出的大语言模型系列，以超长上下文窗口著称（1M+ Token），是长上下文方案的代表产品。

## 关键信息
- Google 旗舰大模型系列
- 支持 100 万+ Token 的超长上下文窗口，是当前上下文窗口最长的模型之一
- 在 RAG vs 长上下文的讨论中，Gemini 常被引用为"长上下文能否替代 RAG"的论据
- 长上下文的优势：无需检索，全文直接输入
- 长上下文的局限：成本高（按 Token 计费）、延迟随输入长度增加、无法精确溯源
- [[摘要-step-3-7-flash-agent横评]] 中提到 Gemini 3.5 Flash 在 GitHub 项目雷达任务中能一次性完成脚本和页面，但页面组织较松散，信息密度和视觉层级不如 [[Step3Flash]]。

## 关联连接
- [[RAG]] — 与长上下文的对比选型
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 来源
- [[摘要-step-3-7-flash-agent横评]] — 来源（Gemini 3.5 Flash Agent 任务体验）
- [[Step3Flash]] — 横评对比模型
- [[Qwen]] — 横评对比模型
