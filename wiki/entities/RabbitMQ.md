---
title: "RabbitMQ"
type: entity
tags: [消息队列, 消息代理]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
RabbitMQ 是使用 Erlang 编写的轻量级开源消息代理软件，实现了高级消息队列协议（AMQP）。以低延迟、灵活路由和易用性著称。

## 关键信息
- 定位于轻量级路由、低延迟、协议兼容场景
- 吞吐量约 10万 QPS，适合中小规模场景
- 消息延迟为微秒级，在四者中延迟最低
- 不支持严格的消息顺序保证
- 支持 Push 和 Pull 两种消费模式

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[摘要-rabbitmq-idempotency]] — RabbitMQ 防重复消费方案
- [[Kafka]] — 高吞吐消息系统对比
- [[RocketMQ]] — 阿里开源消息中间件
- [[Pulsar]] — 云原生消息流平台
- [[message-queue]] — 消息队列核心概念
- [[idempotency]] — 幂等性设计