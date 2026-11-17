---
title: "摘要-deepseek全家桶api开放"
type: source
tags: [来源, DeepSeek, API, 开源]
sources: [raw/09-archive/2026-11-14 - 重磅！DeepSeek放开全家桶API，直接帮开发者把桌子掀了！.md, raw/09-archive/突发！DeepSeek开放全家桶API：官方App功能均可自由组合调用.md]
last_updated: 2026-11-16
---

## 核心摘要
程序员追风（转新智元）2026-11-14 报道：DeepSeek 正式开放"全家桶应用 API"，把 App/网页端的深度思考搜索、上传文件、读链接、语音交互、文字识别等交互能力全部整合进原有 API——工具调用、上下文拼接由服务端完成，官方宣称开发者可 1:1 复刻完整 DeepSeek App。[[DeepSeek-V4.1-Flash]] 已在 Messages、Responses 与 Chat Completions 三协议下支持：联网搜索/深度思考搜索（deepseek_web_search 工具，思考模式可多步推理中自主搜索+读链接）、文件输入（PDF/Office/图片，服务端自动解析拼入上下文）、阅读链接（deepseek_read_url）、内置模型安全（输入输出审核+图片审核）。底层能力拆成独立接口：Search（联网搜索）、Fetch（网页抓取）、OCR（文字识别）、ASR（语音识别）、TTS（语音合成），可单独或组合调用。官方开源轻量前端演示 Demo（github.com/deepseek-ai/chat-demo，支持历史对话导入、密钥与对话存浏览器本地）。内容已并入 [[DeepSeek]] 与 [[DeepSeek-V4.1-Flash]]。

### 第二来源增补（2026-11-16 量子位版，码农学习联盟转载）
同一事件第二篇报道，增量信息为**定价明细与演进视角**：ASR 原价 0.78 元/小时现五折 **0.39 元**（约 0.0065 元/分钟），对比 OpenAI GPT-Transcribe（约 1.81 元/小时，1/4.6 价差）、GPT-4o mini Transcribe（约 1.21 元/小时，1/3.1）、Google Cloud 标准语音识别（约 6.43 元/小时，1/16.5）；TTS 原价 3 元/万字符现五折 **1.5 元/万字符**；OCR **1.5 元/千页**（0.0015 元/页）；Search/Fetch 维持 **5 元/千次成功调用**（与 [[DeepSeek-V4.1-Flash]] 页"2026-11-01 起计费"记录一致）。演进视角：联网搜索 2026-10-17 已开放 Search/Fetch 接口，但当时工具调用与衔接需开发者自己写代码串联；本次升级后"何时搜索/搜什么/读哪些网页/如何作答"全部由服务端自动完成。语音（ASR/TTS）为**首次开放官方独立接口**——此前 App 支持语音交互但公开 API 无完整语音能力，开发者需另接第三方 ASR/TTS 服务。

## 关联连接
- [[DeepSeek]] — 开放主体（增量更新）
- [[DeepSeek-V4.1-Flash]] — 承载能力的模型（增量更新）
- [[程序员追风]] — 来源作者
- [[AgenticSearch]] — Search/Fetch 接口同域概念
