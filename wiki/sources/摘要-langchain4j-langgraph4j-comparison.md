---
title: "摘要-langchain4j-langgraph4j-comparison"
type: source
tags: [来源, Java, AI框架, Agent]
sources: [raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md]
last_updated: 2026-06-30
---

## 核心摘要
这篇文章强调 [[LangChain4j]] 与 [[LangGraph4j]] 不是替代关系，而是“AI 能力接入层”和“Agent 工作流编排层”的互补关系。LangChain4j 负责模型调用、Embedding、RAG、Tool Calling、AiServices 等能力接入，适合单 Agent、RAG 问答和快速 AI 应用原型；LangGraph4j 负责状态图、条件分支、循环、多智能体协作、检查点和 Human-in-the-Loop，适合长流程、多步骤决策和生产级多 Agent 协作。文章的选型建议是：1-3 步轻量任务用 LangChain4j，多步分支/循环/断点恢复用 LangGraph4j，复杂企业项目常采用二者组合。

## 关联连接
- [[LangChain4j]] — Java LLM 应用能力接入框架
- [[LangGraph4j]] — Java Agent 状态图编排框架
- [[Agent工作流编排]] — 多智能体流程化、状态化方法论
- [[RAG]] — LangChain4j 重点能力之一
- [[FunctionCalling]] — LangChain4j Tool Calling 能力基础
