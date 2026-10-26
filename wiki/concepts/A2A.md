---
title: "A2A"
type: concept
tags: [AI, Agent, 协议, 通信]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/09-archive/2026-09-30-a16z 最新深度对话：这才是 personal agent 的正确打开方式.md]
last_updated: 2026-10-08
---

## 定义
Agent-to-Agent 协议，实现分布式 Agent 间通信和编排，是 MCP 之外的另一种 Agent 互操作协议。

## 关键信息
- Spring AI Alibaba 通过 Nacos 实现 A2A 分布式 Agent 间通信
- AgentScope-Java 支持 A2A 实现跨进程 Agent 编排
- A2A 与 MCP 互补：MCP 解决 Agent 与外部工具/服务的连接，A2A 解决 Agent 与 Agent 之间的协作
- 支持跨服务、跨进程的 Agent 调用与编排
- **Agent to Agent 是"下一个互联网雏形"（a16z，2026-09）**：agent 将拥有自己的电子邮件地址和电话号码，一个 agent 代表买家、另一个代表卖家，自己谈、自己协调、自己完成交易，人只在最初设定参数；服务业将从"人类预订人类服务"→"agent 预订人类服务"→"agent 预订 agent 服务"逐步重构（典型例子：买家的 agent 联系 Etsy 手织袜子老奶奶的 agent 下单，双方全程没有直接对话）
- **商业含义**：A2A 会催生新的长尾经济——有技能、有时间但接触不到大市场的人，可通过自己的 agent 被大市场找到、匹配、委托，类似 Uber 把供给方接入市场但范围广得多
- **早期落地形态**：个人 Agent 之间直接拉通协调日程、联合策划活动（如 [[Instinct]] 的可信网络），按夫妻/朋友/同事关系设置细粒度、可撤销的访问权限，而非无限共享信息

## 关联连接
- [[MCP]] — 互补协议（Agent-工具 vs Agent-Agent）
- [[SpringAI_Alibaba]] — A2A 实现框架
- [[AgentScope_Java]] — A2A 支持框架
- [[Agent]] — 所属核心概念
- [[摘要-java-ai框架选型指南-2026]] — 来源（工程实现视角）
- [[摘要-a16z-personal-agent对话]] — 来源（Agent to Agent 未来图景）
- [[personal-ai-agent]] — A2A 的主要应用赛道
- [[Instinct]] — Agent 间协调的先行实践
