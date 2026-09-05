---
title: "AI工作流"
type: concept
tags: [AI, Workflow, Anthropic, 编排]
sources: [raw/01-articles/美团二面：Agent、Tools、Workflow 这三个的概念和区别介绍一下？我：没接触过.md]
last_updated: 2026-07-08
---

## 定义

开发者预先编排固定代码路径的多步流程，LLM 和 Tools 按写死的步骤一步步走，每一步做什么、结果往哪传都是确定的。LLM 只负责"执行单步任务"，不决定流程走向。与 Agent 的自主决策形成对比。

此概念源自 Anthropic《Building Effective Agents》（2024 年 12 月）给出的业界公认定义。注意不要与 [[dynamic-workflow]]（用代码替代自然语言编排 Agent 工作流）混淆——本文讲的是 Anthropic 定义的 Workflow 概念。

## 关键信息

### 核心特征
- **决策方是人**：开发者写死路径，LLM 不决定流程走向
- **可控性高**：路径固定，可调试、可监控
- **灵活性中**：适合任务路径明确、步骤固定的场景

### Workflow 是"直线"，Agent 是"圆环"
Workflow 按直线执行，没有从结果回到决策的循环边。Agent 的 ReAct 循环有从 Observe 回到 Think 的边，可以在中间结果基础上重新决策。这是两者最本质的区别。

### 典型应用场景
- RAG 问答（检索→重排→生成，固定流水线）
- 文档抽取（解析→分块→抽取字段→校验）
- 意图路由（LLM 分类→分发到对应处理分支）

### Anthropic 五种 Workflow 模式
Prompt Chaining、Routing、Parallelization、Orchestrator-Workers、Evaluator-Optimizer。

### Java 框架落地
Spring AI 中用 ChatClient 链式 API 编排 Workflow，开发者写死每一步的输入输出和调用顺序。

### 与 Tools/Agent 的层级关系
三者层级递进：Tools（积木，被动能力单元）→ Workflow（流水线，人写死路径）→ Agent（当家人，LLM 自己决定路径）。Workflow 把多个 Tools 按固定路径串起来，开发者是司机，LLM 是执行单元。

### 选型原则
Anthropic 强调"简单胜于复杂"：能用 Workflow 解决就别上 Agent；对稳定性、成本、延迟敏感的场景优先用 Workflow。Agent 的循环会带来不可控的 Token 消耗。

### 混合形态
生产环境主流：外层 Workflow 编排 + 关键决策点交给 Agent（Agent with Guardrails）。

## 关联连接
- [[Agent]] — 自主决策的智能体，与 Workflow 形成对比
- [[FunctionCalling]] — Tools 的底层机制
- [[dynamic-workflow]] — 不同的 Workflow 概念，需区分
- [[SpringAI]] — ChatClient 链式 API 编排
- [[LangChain4j]] — Java 生态 Workflow 编排
- [[RAG]] — Workflow 典型应用场景
- [[ReAct_Agent]] — Agent 的循环模式
- [[摘要-agent-tools-workflow区别]] — 来源
