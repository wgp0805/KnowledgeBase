---
title: "LiteTopic"
type: concept
tags: [消息队列, RocketMQ, AI, Multi-Agent]
sources: [raw/01-articles/RocketMQ 已正式接入 AI ！.md]
last_updated: 2026-07-01
---

## 定义
LiteTopic（轻量主题）是 Apache RocketMQ 5.x 专为 AI 场景设计的轻量级 Topic。核心理念是**把每个 AI 会话、每个 Agent 任务都映射成一个独立的轻量 Topic**，解决传统 Topic 创建/管理开销大、无法为海量会话逐个建 Topic 的问题。

## 关键信息

### LiteTopic vs 传统 Topic
| 对比维度 | 传统 Topic | LiteTopic |
| --- | --- | --- |
| 创建方式 | 手动创建，配置复杂 | 自动创建，按需生成（发消息时不存在即自动建） |
| 数量上限 | 有限 | 百万级 |
| 生命周期 | 永久存在 | TTL 自动过期删除 |
| 资源开销 | 较高 | 极低 |
| 适用场景 | 固定业务消息 | AI 会话、Agent 任务 |

### 三大落地能力
1. **Multi-Agent 异步通信**：Supervisor Agent 拆解任务后发送到各 Request Topic（如 `request_agent1_{sessionId}`），子 Agent 通配符订阅（`request_agent1_*`）消费并回写 `response_{sessionId}`，Supervisor 汇总后流式推送用户。把长耗时 AI 调用从同步阻塞变为异步非阻塞。
2. **分布式会话状态管理**：会话状态外置到 RocketMQ（`chat/{sessionId}`），应用节点无状态化；断线重连时新节点订阅同一 LiteTopic，按消费进度（Offset）从断点续传，避免 GPU 算力浪费。
3. **会话隔离**：每个 SessionID 对应独立 LiteTopic，不同会话消息互不干扰。

### 配套的智能调度（RocketMQ for AI）
- 流量整形（削峰填谷）：作为前端请求与后端算力间的缓冲层。
- 消息优先级：堆积时高价值任务（如付费用户）优先获得算力。
- 定速消费（限流）：可精细到单个 LiteTopic 级别，保护算力资源。

## 关联连接
- [[摘要-rocketmq-接入ai]] — 来源
- [[RocketMQ]] — 提供 LiteTopic 的消息中间件
- [[message-queue]] — 消息队列基础能力
- [[multi-agent-collaboration]] — LiteTopic 支撑的 Agent 间异步协作
- [[MCP]] — RocketMQ for AI 原生支持的协议
- [[A2A]] — Agent-to-Agent 协议
