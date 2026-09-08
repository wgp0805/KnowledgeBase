---
title: "Responses API"
type: concept
tags: ["OpenAI", "API", "GPT-6", "Astra"]
sources:
  - raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md
last_updated: 2026-09-08
---

# Responses API

Responses API 是 OpenAI 新一代接口，支持内置工具、状态管理、多轮编排。与 Chat Completions API 的区别：后者是传统单轮接口。迁移建议：需要内置工具和多轮编排用 Responses API，简单调用保留 Chat Completions。

## GPT-6 Astra 时代的关键变化
- **GPT-6 Astra 只支持 Responses API**，Chat Completions API 不在支持范围
- Responses API 承载工具调用、远程 MCP、电脑操作、代码执行、文件检索、多轮状态
- Astra 还支持 [[ToolSearch]] 和 [[Skills]]：需要时再加载工具定义与能力说明
- 这会影响 Agent 框架：纯粹做工具转发的中间层价值下降，留下来的部分是企业连接器/流程规则/可观测性/权限控制/异常恢复

## 关联连接
[[ChatCompletionsAPI]], [[OpenAI]], [[沉默王二]], [[GPT-6]], [[ToolSearch]], [[Skills]], [[MCP]], [[AgentRuntime]], [[摘要-GPT-6-Astra改变技术栈]]
