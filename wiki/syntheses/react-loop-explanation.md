---
title: "react-loop-explanation"
type: synthesis
tags: [AI, Agent, ReAct, 推理循环]
sources:
  - wiki/concepts/ReAct_Agent.md
  - wiki/concepts/ReActAgent.md
  - wiki/concepts/Agent.md
  - wiki/concepts/ToolPipeline.md
  - wiki/concepts/HarnessAgent.md
last_updated: 2026-07-06
---

# ReAct 循环详解

## 定义

ReAct（Reasoning + Acting，推理+行动循环）是 AI Agent 最基础的自主推理模式。核心流程：

> 思考（Reason）→ 行动（Act）→ 观察（Observe）→ 再思考 → 循环直到完成任务

相当于给 LLM 装了一个"能动手"的循环：模型不只是"想"（输出文字），还可以"做"（调用工具查天气、读文件、执行代码），然后把工具返回的结果"看"到，再决定下一步。

## 典型执行路径

1. LLM 收到用户问题 → **思考**需要什么工具
2. 输出工具调用指令（tool_call）→ **行动**：框架执行工具
3. 工具结果回填到消息历史 → **观察**结果
4. 如果还没完成 → 回到步骤 1
5. 如果任务完成 → 输出最终回答

在 [[ReActAgent]]（AgentScope Java 实现）中，这个过程被比作"发动机"——它解决的是"一次请求→推理→工具→回复"这个最基础的智能体能力。

## 关键设计点

### 单轮单工具局限
ReAct 每轮只能调用一个工具。多步骤任务需要多次 LLM 调用，Token 消耗大，响应延迟高。

### 适用范围
- **适合**：无固定流程的开放式问题（如"帮我研究一下这个主题"）
- **不适合**：流程固定的标准化多步骤任务（这类场景更适合 [[ToolPipeline]]）

### 各框架实现
| 框架 | 实现类 | 特点 |
|------|--------|------|
| [[SolonAI]] | ReActAgent | 与 SimpleAgent、TeamAgent 并列 |
| [[SpringAI_Alibaba]] | ReactAgent | 阿里多智能体编排框架 |
| [[AgentScope_Java]] | HarnessAgent | ReActAgent 的工程化包装 |

## 工程化升级

纯 ReAct 循环在生产中不够用，各框架在其上叠加工程能力：

- [[HarnessAgent]] 在 ReActAgent 上加了工作区、Session、记忆、压缩、子 Agent、沙箱等——类比"发动机变整车"
- [[Agent]] 概念中的 Harness 工程决定了同样的大模型在不同 Agent 上的效果差异
- [[ToolPipeline]] 在流程固定场景下替代 ReAct 多轮循环，大幅降低 Token 消耗

## 与 ToolPipeline 对比

| 维度 | ReAct | ToolPipeline |
|------|-------|-------------|
| 工具执行 | 单轮单工具 | 批量串行/并行 |
| LLM 思考次数 | 每步骤一次 | 仅规划一次 |
| Token 消耗 | 大 | 小 |
| 适用场景 | 无固定流程的开放问题 | 流程固定的标准化任务 |

## 关联连接
- [[ReAct_Agent]] — 核心概念页面
- [[ReActAgent]] — AgentScope Java 实现
- [[Agent]] — Agent 核心概念
- [[ToolPipeline]] — 工具流水线编排（对比）
- [[HarnessAgent]] — ReActAgent 的工程化包装
- [[SpringAI_Alibaba]] — ReactAgent 实现
- [[SolonAI]] — ReActAgent 实现
- [[AgentScope_Java]] — HarnessAgent 实现
