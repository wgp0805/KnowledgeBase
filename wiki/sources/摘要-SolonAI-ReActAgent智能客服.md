---
title: "摘要-SolonAI-ReActAgent智能客服"
type: source
tags: [来源, AI Agent, Solon, 智能客服]
sources: ["raw/01-articles/2026-07-12-用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅.md"]
last_updated: 2026-07-13
---

## 核心摘要

本文介绍如何使用 Solon AI 框架的 ReActAgent 实现电商智能客服工单处理。通过定义订单查询、物流查询、补偿发放等工具，Agent 可自主完成"查单→定位问题→标准赔付"的全流程。

关键特性包括：业务 SOP 写进 system prompt + 工具描述、HITLInterceptor 实现大额赔付人工审批、InMemoryAgentSession 保持会话状态。该模式适用于保险理赔、物流投诉、物业报修等多种客服场景。

## 关联连接
- [[SolonAI]] — Solon AI 框架
- [[ReActAgent]] — ReAct Agent 模式
- [[HITL]] — Human-in-the-Loop
- [[ToolCalling]] — 工具调用机制
