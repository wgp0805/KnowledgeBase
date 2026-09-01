---
title: "DeadLetterQueue"
type: entity
tags: [消息队列, 可靠性, 死信队列]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
死信队列（Dead Letter Queue, DLQ）是消息队列中用于存放无法正常消费的消息的特殊队列，可在其中重新消费消息以实现重试。

## 关键信息
- **作用**：存放消费失败的消息，支持重新消费
- **与 Spring Event 的关系**：Kafka 消费者中使用 Spring Event 时，消费异常可发到死信队列重新消费
- **实现差异**：不同公司的 Kafka 重试能力实现方案可能不同

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 应用场景
- [[Kafka]] — 典型实现
- [[MQ]] — 所属领域
- [[Idempotency]] — 重新消费需保证幂等
