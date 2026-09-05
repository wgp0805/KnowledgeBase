---
title: "HITL"
type: concept
tags: [AI, 人机协作, Agent]
sources: ["raw/01-articles/2026-07-12-用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅.md"]
last_updated: 2026-07-13
---

## 定义

HITL（Human-in-the-Loop，人机协同）是指在 AI Agent 执行过程中，关键决策点暂停执行，等待人工审批或确认后再继续的机制。

## 关键信息

- **核心价值**：确保高风险操作（如大额退款）由人工把关，降低 AI 误判风险
- **实现方式**：通过 HITLInterceptor 拦截特定工具调用，根据条件判断是否需要人工审批
- **审批流程**：Agent 暂停 → 管理员审批（批准/拒绝）→ Agent 续传执行
- **适用场景**：大额赔付、敏感操作、法律合规等需要人工确认的场景

## 关联连接
- [[摘要-SolonAI-ReActAgent智能客服]] — 来源
- [[ReActAgent]] — ReAct Agent 模式
- [[ToolCalling]] — 工具调用机制
