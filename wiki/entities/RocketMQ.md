---
title: "RocketMQ"
type: entity
tags: [消息队列, 中间件]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md, raw/01-articles/Docker-window环境下部署RocketMq.md, raw/01-articles/springboot整合RocketMq.md, raw/01-articles/高并发下如何防止重复下单？.md, raw/01-articles/RocketMQ 已正式接入 AI ！.md]
last_updated: 2026-07-01
---

## 定义
RocketMQ 是阿里巴巴开源的分布式消息中间件，具有高吞吐量、高可用性、低延迟和强大的消息回溯能力。

## 关键信息
- 核心组件：NameServer（命名服务）、Broker（消息存储）、Producer（生产者）、Consumer（消费者）
- 消息模型：Topic（主题）、Tag（标签）、Queue（队列）
- 支持普通消息、顺序消息、事务消息、定时/延时消息
- Docker 部署包含 NameServer、Broker 和控制台（rocketmq-dashboard）
- Spring Boot 整合使用 RocketMQTemplate 发送消息
- 环境隔离方案：多环境 Topic 配置

### 异步订单处理应用
- **削峰填谷**：将同步订单请求转为异步处理，提升系统吞吐量
- **消息发送**：使用 `asyncSend` 异步发送，配合 SendCallback 处理结果
- **消费者幂等**：基于 requestId 进行幂等检查，防止重复消费
- **状态回写**：处理完成后更新 Redis 中的处理状态

### RocketMQ for AI（5.5.0 战略升级）
- **[[LiteTopic]]（轻量主题）**：百万级、自动创建、TTL 过期、开销极低，把每个 AI 会话/Agent 任务映射为独立 Topic。
- **Multi-Agent 异步通信**：把长耗时 AI 调用从同步阻塞变为异步非阻塞，提升吞吐。
- **分布式会话状态管理**：状态外置、应用节点无状态化，断线按 Offset 断点续传。
- **智能算力调度**：流量整形 + 消息优先级 + 定速消费，优化稀缺 GPU 算力。
- **生态**：原生支持 MCP、A2A 协议，可对接 LangChain/CrewAI/AutoGen/Dify。

## 关联连接
- [[SpringBoot]] — 与 Spring Boot 整合
- [[Docker]] — 容器化部署
- [[Nacos]] — 配置中心
- [[idempotency]] — 消费者幂等实现
- [[摘要-prevent-duplicate-order]] — 异步订单处理
- [[LiteTopic]] — RocketMQ for AI 的核心新特性
- [[摘要-rocketmq-接入ai]] — RocketMQ 5.5.0 接入 AI 解析
