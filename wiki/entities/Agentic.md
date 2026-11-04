---
title: "Agentic"
type: entity
tags: [AI框架, Agent, Python, 生产级, 开源]
sources: [raw/09-archive/为什么越来越多人用 Agentic？.md]
last_updated: 2026-11-03
---

## 定义

Agentic 是 supercog-ai 开源的**生产级 Python Agent 框架**（GitHub `supercog-ai/agentic`），定位与第一代框架（LangChain/AutoGen）形成代差：第一代解决"能不能跑起来"（Demo 丝滑），Agentic 解决"跑起来之后能不能知道它在干什么、能不能控制它、能不能让它稳定跑完"。核心主张：把 Agent 从"Demo 玩具"变成"生产系统"。

## 关键信息

### 三大设计选择

1. **极简抽象**：只有 Agent / Tool / Run / Thread 四个概念，无需拼装复杂 DAG；Agent 循环代码仅几百行直接调 LLM API，无藏起来的复杂抽象
2. **事件驱动**：Agent 不返回死板文本，而吐**类型化事件**——`ToolCallEvent` / `ToolResultEvent` / `LLMResponseEvent` / `TextEvent`，可订阅做流式输出、后台通知、可观测
3. **基于 Ray**：底层用 Ray 的 Actor 模型托管 Agent，每个 Agent 独立 Actor 有自己的状态和消息队列，天然支持高并发与多 Agent 团队

### 生产级工程增强

- **工具执行异步、可配置**：工具是可配超时、重试、认证的独立组件，不是简单函数
- **Human-in-the-loop 原生支持**：工具执行需人工审批时可无限期暂停等待批准，通知走邮件或 Webhook，不用自己写死循环
- **可观测性内置**：日志、Trace、上下文管理、工具认证都是框架自带

### 防幻觉实践（"不瞎编"助手）

强制 Agent 查库再回答：工具 description 写死"当需要回答 X 时必须调用此工具" + 系统提示词三条规则（先查库、严禁凭空捏造、工具失败直接答"获取失败"）。运行后消费事件流——若模型想捏造数据，事件流里不会出现 `ToolCallEvent`，后台一眼看出没查库。排障闭环：把结构化 Trace 日志喂给 AI 定位根因（如"LLM 忽略了系统提示词的强制要求，工具 description 可能不够有吸引力"），再让 AI 生成 pytest 回归测试防下次发版前回归。

### 优缺点

| 维度 | 说明 |
|------|------|
| 极简透明 | 只有四概念，出问题可直接读循环代码 |
| 事件流 | 多通道、后台运行、流式 UI |
| HITL 原生 | 无限期等待人工输入，邮件/Webhook 通知 |
| Ray 并发 | Actor 天然支持异步与并发，多 Agent 团队从容 |
| 缺点 | 生态较新（非"什么都有"）；Ray 有学习成本；Python 3.12 最稳、不支持 3.13+；需适应事件订阅式异步思维 |

### 适用场景

强烈推荐：生产级 Agent 服务 / 需强制 Agent 行为 / 多 Agent 协作团队 / 需流式与后台通知；需评估：快速 Demo 原型（LangChain 更快）、需大量第三方插件（生态追赶中）。

## 关联连接
- [[摘要-为什么越来越多人用agentic]] — 来源
- [[苏三]] — 介绍作者
- [[HITL]] — Human-in-the-loop 原生支持
- [[ReAct]] — 核心循环范式
- [[LangChain]] — 对照的第一代框架
- [[AutoGen]] — 对照的第一代框架
- [[可观测性]] — 事件流与 Trace 的目标
- [[ToolCalling]] — 工具调用机制
- [[工具路由]] — 工具执行配置化
- [[多智能体编排]] — 多 Agent 协作的上位概念
