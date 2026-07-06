---
title: "ReAct Agent"
type: concept
tags: [AI, Agent, 推理, 行动循环]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/2026-07-05-AI Agent 30天速成｜Day10 笔记 - 云淡风轻YangG.md]
last_updated: 2026-07-06
---

## 定义
推理+行动循环（Reasoning + Acting）的 Agent 模式，模型自主进行"思考→行动→观察结果→再思考"的迭代循环，直到完成任务。

## 关键信息
- 多个 Java AI 框架实现了 ReAct Agent：Spring AI Alibaba（ReactAgent）、Solon AI（ReActAgent）、AgentScope-Java（HarnessAgent）
- ReAct 范式是 Agent 工程中最基础的自主推理模式
- 与 Pure Agent（模型完全自主决策）和 Workflow（预定义编排流程）并列为主流 Agent 模式

### 与 ToolPipeline 对比
- ReAct 单次只能调用一个工具，多步骤需多轮 LLM 思考，Token 消耗大
- ToolPipeline 一次性定义串行/并行多工具步骤，模型仅一次规划，网关批量调度
- **选型建议**：无固定流程开放问题 → ReAct；流程固定标准化任务 → ToolPipeline

## 关联连接
- [[Agent]] — 所属核心概念
- [[SpringAI_Alibaba]] — ReactAgent 实现
- [[SolonAI]] — ReActAgent 实现
- [[AgentScope_Java]] — HarnessAgent 实现
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-ai-agent-day10-tool-pipeline]] — 来源
- [[ToolPipeline]] — 工具流水线编排对比
