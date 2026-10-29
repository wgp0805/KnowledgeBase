---
title: "ToolSearch"
type: concept
tags: [概念, AI, Agent, GPT-6, Astra, 工具加载]
sources: [raw/09-archive/2026-09-07-“GPT-6 Astra 正式登场”会怎样改变现有技术栈？.md]
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

### 在 code_mode_only 中的落地形态（2026-10-27）
沉默王二翻 Codex 源码发现 [[GPT-6.1-Terra]] 的 `tool_search` 是纯代码执行模式（[[code_mode_only]]）的配套：底层用 **BM25 实时检索**当前任务需要的工具并返回 TypeScript 签名，随后在同一段 JS 里用 `Promise.allSettled` 并发执行多个互不依赖的文件搜索/读取——"延迟加载"从概念落地为"检索签名 + 并发执行"的机制。详见 [[摘要-gpt6.1-terra-codex三招]]。

## 关联连接
- [[GPT-6]] — Tool Search 的支持模型
- [[GPT-6.1-Terra]] — tool_search 落地形态所在模型
- [[code_mode_only]] — 延迟加载机制的落地模式
- [[BM25]] — 工具签名检索算法
- [[Skills]] — 配合 Tool Search 的能力说明机制
- [[ResponsesApi]] — Tool Search 的接口载体
- [[RAG]] — Tool Search 推动 RAG 细分
- [[摘要-GPT-6-Astra改变技术栈]] — 来源
- [[摘要-gpt6.1-terra-codex三招]] — 来源（落地形态）
