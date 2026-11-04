---
title: "摘要-为什么越来越多人用agentic"
type: source
tags: [来源, 原始文件, Agentic, Agent框架, 生产级]
sources: [raw/09-archive/为什么越来越多人用 Agentic？.md]
last_updated: 2026-11-03
---

## 核心摘要

苏三（2026-11-03）介绍 **Agentic**（supercog-ai/agentic）——面向生产环境的 Agent 框架。核心主张：第一代框架（LangChain/AutoGen 等）为"笔记本 Demo 丝滑"而生，搬到生产面对并发、网络、稳定交付时全暴露——**黑盒**（只回一段文本，中间调用链路不可见）、**配置**（工具参数/API Key 写死在代码）、**协作**（多 Agent 通信、人工审批要自己造轮子）。Agentic 在架构底层焊死这三个问题。

**核心架构**：
1. **极简抽象**：只有 Agent / Tool / Run / Thread 四个概念，Agent 循环代码仅几百行直接调 LLM API，无复杂 DAG 抽象可扒开看
2. **事件驱动**：Agent 吐**类型化事件**（`ToolCallEvent` / `ToolResultEvent` / `LLMResponseEvent` / `TextEvent`），可订阅做流式输出、后台通知
3. **基于 Ray**：底层用 Ray Actor 模型托管 Agent，每个 Agent 独立 Actor 有自己的状态和消息队列，天然高并发

**工程增强**：工具执行异步且可配超时/重试/认证；Human-in-the-loop 原生支持（工具需人工审批时无限期暂停等批准，邮件/Webhook 通知）；日志/Trace/上下文管理内置。

**应用示例**：强制 Agent 查库再回答（工具 description 写死"必须调用" + 系统提示词三条规则），事件流中不见 `ToolCallEvent` 即为未查库幻觉——可直接把 Trace 日志喂给 AI 排障，让 AI 定位根因并生成 pytest 回归测试。

**优缺点**：优点——极简透明、事件流、HITL 原生、工程化内置、Ray 并发；缺点——生态较新、Ray 有学习成本、Python 3.12 最稳（不支持 3.13+）、需适应事件订阅式异步思维。

**适用**：生产级 Agent 服务、需强制 Agent 行为、多 Agent 协作团队、需流式/后台通知；快速 Demo 用 LangChain 更快。

## 关联连接
- [[Agentic]] — 本文主角框架实体
- [[苏三]] — 作者
- [[HITL]] — Human-in-the-loop 原生支持
- [[ReAct]] — 核心循环范式
- [[LangChain]] — 对照的第一代框架
- [[AutoGen]] — 对照的第一代框架
- [[可观测性]] — 事件流/Trace 解决的问题
- Ray — 底层运行时（Actor 模型，无独立页，纯文本标注）
- [[ToolCalling]] — 工具调用机制
- [[工具路由]] — 工具执行配置化
