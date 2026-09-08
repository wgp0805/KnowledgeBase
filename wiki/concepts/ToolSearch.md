---
title: "ToolSearch"
type: concept
tags: [概念, AI, Agent, GPT-6, Astra, 工具加载]
sources: [raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md]
last_updated: 2026-09-08
---

## 定义
Tool Search 是 GPT-6 Astra 支持的能力：让系统在需要时再加载工具定义与能力说明，避免把所有工具信息一次塞进上下文。与 Skills 配合，推动 RAG 从"检索更多内容"转向"装载正确证据和正确能力"。

## 关键信息
- Astra 支持 Tool Search 和 Skills
- 模型接到任务后，按需选择知识源、业务工具和处理方法
- 只把当前步骤需要的内容送入上下文
- 避免"一次塞进上下文"导致的窗口浪费和干扰
- 推动工具调用从"预注册全量"走向"按需加载"

## 关联连接
- [[GPT-6]] — Tool Search 的支持模型
- [[Skills]] — 配合 Tool Search 的能力说明机制
- [[ResponsesApi]] — Tool Search 的接口载体
- [[RAG]] — Tool Search 推动 RAG 细分
- [[摘要-GPT-6-Astra改变技术栈]] — 来源
