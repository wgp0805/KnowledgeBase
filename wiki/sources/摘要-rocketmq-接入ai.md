---
title: "摘要-rocketmq-接入ai"
type: source
tags: [来源, 原始文件, 消息队列, AI, Multi-Agent]
sources: [raw/01-articles/RocketMQ 已正式接入 AI ！.md]
last_updated: 2026-07-01
---

## 核心摘要
苏三《RocketMQ 已正式接入 AI ！》讲解 Apache RocketMQ 5.5.0 面向 AI 工作负载的战略升级。核心是新特性 **LiteTopic（轻量主题）**：支持百万级、自动创建、TTL 自动过期、资源开销极低，把每个 AI 会话/Agent 任务映射成一个独立轻量 Topic。它解决 AI 应用三大痛点：①用异步非阻塞替代同步阻塞，让 Multi-Agent 协作不被长耗时 AI 推理拖垮（Supervisor 拆任务发消息、子 Agent 消费后回写 Response Topic）；②分布式会话状态管理，把状态外置到 RocketMQ、应用节点无状态化，断线重连按 Offset 断点续传，避免 GPU 算力浪费；③智能算力调度（流量整形削峰填谷 + 消息优先级 + 定速消费限流）。生态上原生支持 MCP 与 A2A 协议，可对接 LangChain/CrewAI/AutoGen/Dify。缺点：完整 AI 能力目前主要在云上版本、开源逐步落地，且需重新设计为异步消息驱动架构。

## 关联连接
- [[LiteTopic]] — 本文核心新特性
- [[RocketMQ]] — 承载 AI 能力的消息中间件
- [[multi-agent-collaboration]] — LiteTopic 天然适配的 Agent 间异步通信
- [[message-queue]] — 削峰填谷、异步解耦的通用能力
- [[MCP]] — RocketMQ for AI 原生支持的协议
- [[A2A]] — Agent-to-Agent 协议，原生支持
- [[苏三]] — 原文作者
