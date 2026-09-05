---
title: "摘要-rabbitmq-idempotency"
type: source
tags: [消息队列, 幂等性, RabbitMQ, 面试]
sources: [raw/01-articles/百度面试官：RabbitMQ 如何防止重复消费？5种解决方案，你知道几个？.md]
last_updated: 2026-05-25
---

## 核心摘要

本文讲解消息队列中重复消费问题的根因和5种幂等性解决方案。重复消费的根本原因是消费者处理完业务逻辑后，在发送ACK之前宕机或网络断开，RabbitMQ未收到ACK会重新投递消息。解决方案包括：唯一消息ID+去重表（最通用）、数据库唯一约束（最省事）、Redis SETNX（高性能）、乐观锁/版本号（适合更新操作）、状态机（适合订单流转）。

## 关联连接
- [[RabbitMQ]] — AMQP 消息代理
- [[idempotency]] — 幂等性设计
- [[Redis]] — Redis SETNX 去重方案
- [[MySQL]] — 数据库唯一约束方案
