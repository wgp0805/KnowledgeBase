---
title: "ReAct Agent"
type: concept
tags: [AI, Agent, 推理, 行动循环]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
推理+行动循环（Reasoning + Acting）的 Agent 模式，模型自主进行"思考→行动→观察结果→再思考"的迭代循环，直到完成任务。

## 关键信息
- 多个 Java AI 框架实现了 ReAct Agent：Spring AI Alibaba（ReactAgent）、Solon AI（ReActAgent）、AgentScope-Java（HarnessAgent）
- ReAct 范式是 Agent 工程中最基础的自主推理模式
- 与 Pure Agent（模型完全自主决策）和 Workflow（预定义编排流程）并列为主流 Agent 模式

## 关联连接
- [[Agent]] — 所属核心概念
- [[SpringAI_Alibaba]] — ReactAgent 实现
- [[SolonAI]] — ReActAgent 实现
- [[AgentScope_Java]] — HarnessAgent 实现
- [[摘要-java-ai框架选型指南-2026]] — 来源
