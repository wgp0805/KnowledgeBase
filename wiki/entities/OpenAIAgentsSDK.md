---
title: "OpenAIAgentsSDK"
type: entity
tags: [框架, AI, Agent, OpenAI, SDK]
sources: [raw/09-archive/2026-07-21-【手搓 Agent 第0关】认知扫盲篇（下）：Agent 工程选型、架构体系、场景落地完整论证 - Alkaid2077.md, raw/09-archive/2026-10-02 - Agent 的意图路由怎么设计？.md]
last_updated: 2026-10-08
---

## 定义
OpenAI Agents SDK 是 OpenAI 推出的采用代码优先编排方式的 AI Agent 开发工具包，支持通过常规代码实现动态 Agent 流程编排。

## 关键信息
- **代码优先编排**（code-first orchestration）：用常规代码而非可视化流程编排 Agent
- **分诊 Agent 与 handoff（意图路由实现，2026-10-02，详见 [[摘要-agent-意图路由设计]]）**：SDK 把每个子 Agent 包装成一个工具交给分诊 Agent 使用——工具名 `transfer_to_{子agent名}`（如 transfer_to_refund_agent），工具描述为 "Handoff to the X agent to handle the request" + 开发者写的 handoff_description；分诊 Agent 选中哪个就调用对应工具，把对话交给另一个 Agent 接手的动作叫 **handoff**。因此路由准确率完全取决于每个子 Agent 的介绍（handoff_description）写得清不清楚

## 关联连接
- [[OpenAI]] — OpenAI 公司
- [[code-first-orchestration]] — 代码优先编排
- [[摘要-agent-engineering]] — 来源
- [[意图路由]] — 分诊/handoff 所解决的问题
- [[摘要-agent-意图路由设计]] — 来源（handoff 机制详解）
- [[Anthropic]] — 给出枚举/结构化输出路由建议的对照方
