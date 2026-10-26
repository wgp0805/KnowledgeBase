---
title: "AutoGen"
type: entity
tags: [多智能体, 开源框架, 微软, 对话协作]
sources: [raw/09-archive/2026-09-24 - 为什么越来越多人用 AutoGen？.md]
last_updated: 2026-09-28
---

## 定义

AutoGen 是微软研究院在 2023 年末开源的多智能体对话框架，心智模型是「会议室」而非「流程图」：智能体是对话参与者，整个系统是一个群聊，可委派任务、互相批评纠正、调用工具、编写执行代码、向人类提问，目标达成后自行终止——没有任何中央控制器需要提前知晓完整计划。

## 关键信息

- **核心机制**：群聊协作循环——所有参与者共享对话上下文，每条消息广播给所有 Agent；发言者选择策略（轮询/随机/自动 LLM 决定/手动指定）；每轮检查终止条件（TERMINATE、最大轮次、目标达成）
- **v0.4 架构级重构（2025 年初）**：同步 API → 异步事件驱动，0.2.x 代码不兼容；三层架构：`autogen-core`（事件驱动 Actor 运行时）、`autogen-agentchat`（AssistantAgent/UserProxyAgent/GroupChat 高层 API）、`autogen-ext`（OpenAI Assistant、MCP 工作台、gRPC 分布式 Agent）
- **Actor 模型**：每个 Agent 是独立 Actor，自带消息队列与状态，异步消息通信、无中央协调器 → 可分布式部署、原生 OpenTelemetry 追踪、检查点崩溃恢复
- **Java 接入两条路**：autogen4j 纯 Java 移植（Java 17+，类型安全、易集成 Spring Boot，但仅对齐 0.2.x）；或「Java 业务编排 + Python Agent 运行时」双栈方案（REST/gRPC 通信）
- **适用场景**：开放式讨论/辩论、合同与文档审查、头脑风暴、需人类介入的审批流（Human-in-the-loop 原生支持）；不适合确定性流水线、极低延迟、Token 成本敏感场景
- **优缺点**：优点是对话驱动天然适合开放任务、v0.4 架构先进、内置代码执行沙箱（UserProxyAgent）、AutoGen Studio 低代码、微软背书；缺点是 Python 优先 Java 生态薄弱、多轮往返 Token 消耗高、开放式发言可能跑偏
- **现状**：已进入维护模式（bug 修复与安全补丁仍在发），新项目建议直接考虑 Microsoft Agent Framework（MAF）；早期 demo 显示比单智能体表现高 2-10 倍

## 关联连接
- [[group-chat]] — 核心执行模型
- [[LangGraph]] — 「流程图」对照框架
- [[Multi-Agent]] — 所属技术领域
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[MCP]] — v0.4 Ext 层提供的 MCP 工作台
- [[苏三]] — 解读文章作者
- [[摘要-为什么越来越多人用AutoGen]] — 来源
