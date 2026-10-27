---
title: "AtLeastOnce"
type: concept
tags: [消息队列, 可靠性, 投递语义, Kafka]
sources: [raw/09-archive/面试官：Kafka 如何保证消息不丢失？.md]
last_updated: 2026-10-26
---

## 定义

At Least Once（至少一次）是消息投递语义的一种：系统保证消息**不丢**，但不保证**不重**——失败重试或 offset 重复提交时，同一条消息可能被投递/消费多次。它是生产环境的主流选择，代价由"消费端幂等"来偿还，两者相加即为等效的可靠投递。

## 关键信息

- **三档投递语义**：At Most Once（可能丢，发后即忘）／At Least Once（可能重，不丢）／Exactly Once（不丢不重）
- **Kafka 中达成 At Least Once 的姿势**：消费端关自动提交（`enable.auto.commit=false`）、**先消费后提交**——处理失败的消息不提交 offset，下次 poll 还能拉到，最多重复消费不会丢
- **重复的另一面**：offset 提交失败、消费者重启都会把处理过的消息再拉一遍；所以工程口诀是"At Least Once + 消费端幂等"才是生产可用的组合
- **消费端幂等手段**：数据库唯一键约束、Redis 记录已处理消息 ID 等
- **Exactly-Once 的代价**：Kafka 0.11+ 靠幂等生产者 + 事务 + 消费端 `read_committed` 可端到端精确一次，但有性能开销，大部分业务场景仍选 At Least Once + 消费端幂等，成本低得多
- **与 Broker 端配置的呼应**：`min.insync.replicas` 的"宁可写失败、不可写丢"正是 At Least Once 精神在存储侧的体现——牺牲短暂可用性，换取消息不丢

## 关联连接

- [[Kafka]] — 典型实现场景
- [[幂等性]] — 兜住"重复"那一面的配套机制
- [[isr]] — 存储侧"宁可写失败不可写丢"的副本机制
- [[死信队列]] — 重试救不回来的消息的人工兜底
- [[message-queue]] — 所属领域
- [[摘要-kafka消息不丢失]] — 来源
- [[摘要-rabbitmq-idempotency]] — RabbitMQ 场景下的同主题方案（5 种幂等）
