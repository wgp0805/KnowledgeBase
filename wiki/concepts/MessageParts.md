---
title: "MessageParts"
type: concept
tags: [概念, SpringAI, 消息模型, 多模态, 推理模型]
sources: ["raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md"]
last_updated: 2026-11-27
---

## 定义

Message Parts 是 [[SpringAI]] 2.1（M1 引入）对**消息模型的结构性重构**：一条消息从「带可选媒体附件的文本」变成**有序的 `MessagePart` 列表**。`Message` 内部由 Parts 组成，`getText()` / `getMedia()` / `getToolCalls()` / `getReasoning()` 全部降级为**视图**，不再是唯一入口。

本质上是把「消息」从**扁平文本容器**升级为**保真传输容器**——现代推理模型要求把结构化内容原样回传，而旧的「提取文本再重拼」路径会丢信息。

## 关键信息

### Part 类型

| Part | 承载内容 |
| --- | --- |
| `TextPart` | 普通文本 |
| `ReasoningPart` | 推理/思考内容，可带 **OpaquePayload**（如 [[Anthropic]] 的 thinking signature） |
| `ToolCallPart` | 工具调用（含流式 partial 标记） |
| `ToolResultPart` | 工具执行结果 |
| `MediaPart` | 图片等媒体 |
| `UnknownPart` | **保留原始 JSON 而不静默丢弃**——未知类型不丢数据 |

### 为什么必须有序且保真

消息构造方式不变，但顺序与不透明载荷变得**语义关键**：

1. **Anthropic**：要求 thinking blocks 原样、按原顺序回传。你改了一个字符，下一次请求就是 **HTTP 400**
2. **Google GenAI**：要求把 thought signature 放回原来那个 Part，否则 **Gemini 3+ 的函数调用直接 400**
3. **[[OpenAI]] Responses**：要求回放时带上 `encrypted_content`

旧模型（扁平文本 + 附件）在这三处都会「提取—重拼」中丢结构，于是要么报错、要么悄悄降级。`UnknownPart` 的存在正是为了守住「不静默丢数据」这条底线。

### 版本差异（容易踩坑）

- **M1**：只有 `OpenAiResponsesChatModel` **原生产出和消费** Parts，其它实现还在旧路径
- **RC1**：Ollama、Anthropic、Chat Completions 等才完成重构

也就是说 2.1.0 里不同 model 实现消费 Parts 的成熟度不一致——迁移时按具体 provider 核对，别按「2.1 都支持」假设。

### 与流式的关系

流式工具调用的参数增量也以带 **partial 标记**的 `ToolCallPart` 暴露。这些 partial Part 会被 `getToolCalls()` 和 `ToolCallingManager` **忽略**，随后同一个 index 的完整调用才到达。这既让 UI 能做「参数正在生成」的实时展示，又不破坏工具执行语义。

## 关联连接
- [[SpringAI]] — 所属框架（2.1 M1 引入）
- [[摘要-spring-ai-2-1-苏三解读]] — 来源（苏三视角完整展开）
- [[摘要-spring-ai-2-1发布]] — 来源（锋哥版特性清单）
- [[ResponsesApi]] — `encrypted_content` 回放要求的来源
- [[ChatCompletionsAPI]] — RC1 才完成 Parts 重构的路径之一
- [[ToolCalling]] — `ToolCallPart` / `ToolResultPart` 所属机制
- [[ChatMemory]] — 消息模型的消费者（历史消息保真度直接影响回放）
- [[Anthropic]] — thinking blocks 必须原样按序回传
- [[Gemini]] — thought signature 必须回到原 Part
- [[OpenAI]] — Responses 端点要求 `encrypted_content`
- [[上下文压缩]] — 压缩历史消息时 Parts 保真度是新风险点
- [[SSE流式输出]] — 流式 partial Part 的传输载体
- [[AgentRuntime]] — Parts 是「运行时」定位的消息层基础
