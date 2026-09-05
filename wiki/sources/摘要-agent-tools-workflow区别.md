---
title: "Tools/Workflow/Agent 三者层级递进关系与选型"
type: source
tags: [AI, Agent, Workflow, Tools, 面试, Anthropic]
sources: [raw/01-articles/美团二面：Agent、Tools、Workflow 这三个的概念和区别介绍一下？我：没接触过.md]
last_updated: 2026-07-08
---

## 核心摘要

美团面试题解析文章，基于 Anthropic《Building Effective Agents》（2024 年 12 月）给出的业界公认定义，讲清 Tools、Workflow、Agent 三者的边界与选型。

**核心观点**：三者不是并列关系，而是层级递进——Tools 是积木，Workflow 是按图纸拼好的流水线，Agent 是会自己看图纸自己拼的工人。

| 维度 | Tools（工具） | Workflow（工作流） | Agent（智能体） |
| --- | --- | --- | --- |
| 本质 | LLM 可调用的离散函数 | 人预先编排的固定流程 | LLM 自主驱动的循环系统 |
| 决策方 | 调用者（人或 LLM） | 人（开发者写死路径） | LLM（动态决定下一步） |
| 可控性 | 单步可控 | 高（路径固定） | 低（路径不可预测） |
| 典型形态 | 查天气、算数、查 DB | RAG 管线、路由分发 | ReAct 循环、Plan-and-Execute |
| Java 框架落地 | @Tool 注解 | ChatClient 链式 API | Tool Calling + 自主循环 |

**关键区分**：Tools 本身不是 Agent，调用 Tools 的 LLM 也不一定是 Agent。只有"LLM 自主决策 + 循环执行"同时成立时才叫 Agent。Workflow 是"直线"，Agent 是"圆环"——从 Observe 回到 Think 的循环边是 Agent 的本质特征。

**选型原则**（Anthropic）："简单胜于复杂"。能用单个 Tool 就别编排一长串流程；能用 Workflow 解决就别上 Agent；能不调 LLM 就不调 LLM。Agent 的循环会带来不可控的 Token 消耗，对稳定性、成本、延迟敏感的场景优先用 Workflow。

**生产实践**：外层 Workflow 编排 + 关键决策点交给 Agent 的混合形态是 2025 年主流（Agent with Guardrails），必须加护栏：max_iterations、Token 预算、失败降级兜底。

## 关联连接
- [[Agent]] — 智能体概念
- [[AI工作流]] — Anthropic 定义的 Workflow 概念
- [[FunctionCalling]] — Tools 的底层机制
- [[SpringAI]] — Java 生态 @Tool 注解与 ChatClient
- [[LangChain4j]] — Java 生态 @Tool 注解
- [[ReAct_Agent]] — Agent 的经典循环模式
- [[RAG]] — Workflow 的典型应用场景
- [[dynamic-workflow]] — 区别于本文 Anthropic Workflow 概念
