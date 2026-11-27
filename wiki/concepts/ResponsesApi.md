---
title: "Responses API"
type: concept
tags: ["OpenAI", "API", "GPT-6", "Astra"]
sources:
  - raw/09-archive/2026-09-07-“GPT-6 Astra 正式登场”会怎样改变现有技术栈？.md
  - raw/09-archive/2026-11-22 - 夯爆了，Spring AI 2.1 正式发布 ！.md
  - raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md
last_updated: 2026-11-27
---

# Responses API

Responses API 是 OpenAI 新一代接口，支持内置工具、状态管理、多轮编排。与 Chat Completions API 的区别：后者是传统单轮接口。迁移建议：需要内置工具和多轮编排用 Responses API，简单调用保留 Chat Completions。

## GPT-6 Astra 时代的关键变化
- **GPT-6 Astra 只支持 Responses API**，Chat Completions API 不在支持范围
- Responses API 承载工具调用、远程 MCP、电脑操作、代码执行、文件检索、多轮状态
- Astra 还支持 [[ToolSearch]] 和 [[Skills]]：需要时再加载工具定义与能力说明
- 这会影响 Agent 框架：纯粹做工具转发的中间层价值下降，留下来的部分是企业连接器/流程规则/可观测性/权限控制/异常恢复

## Spring AI 侧的接入方式（来源：[[摘要-spring-ai-2-1-苏三解读]]、[[摘要-spring-ai-2-1发布]]）

[[SpringAI]] 2.1 新增 `OpenAiResponsesChatModel` 对接 `/v1/responses`，**切一行配置即启用**：

```properties
spring.ai.openai.chat.api=responses
```

几点必须知道的语义：

- **为什么非切不可**：GPT-5.4 起，Chat Completions **不支持「工具调用 + 非 none 推理强度」这个组合**。想在 Agent 场景里既用工具又保留推理强度，只能走 Responses API
- **它是无状态的**：`OpenAiResponsesChatModel` 每次把**完整 Prompt** 发过去，不依赖服务端会话状态。因此 [[ChatMemory]] / Advisor / [[RAG]] 的行为和 Chat Completions 路径**完全一致**——这是 Spring AI 刻意选的设计（不引入第二套状态模型）
- **两个端点互斥**：默认只装配一个 ChatModel。若要在同一应用里同时保留两个端点，需在 Builder 里**显式声明**，不能靠自动配置并存
- **消息保真要求**：Responses 要求回放时带上 `encrypted_content`，这正是 [[MessageParts]] 里 `ReasoningPart` 携带 **OpaquePayload** 的动因；旧扁平消息模型在这条路径上会丢结构

## 关联连接
[[ChatCompletionsAPI]], [[OpenAI]], [[沉默王二]], [[GPT-6]], [[ToolSearch]], [[Skills]], [[MCP]], [[AgentRuntime]], [[摘要-GPT-6-Astra改变技术栈]], [[SpringAI]], [[MessageParts]], [[ChatMemory]], [[RAG]], [[摘要-spring-ai-2-1-苏三解读]], [[摘要-spring-ai-2-1发布]]
