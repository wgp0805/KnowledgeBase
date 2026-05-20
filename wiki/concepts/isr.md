---
title: "isr"
type: concept
tags: [分布式, 副本, 可靠性]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
ISR（In-Sync Replicas，同步副本集合）是 Kafka 中用于保证数据可靠性的副本同步机制。Leader 维护一个与自身保持同步的 Follower 列表（ISR），只有 ISR 中的所有副本都确认写入后，才向 Producer 返回成功。

## 关键信息
- Leader 和 ISR 中的 Follower 保持数据同步，只有 ISR 中的副本可被选为新的 Leader
- acks=all 配置：Producer 等待 ISR 中所有副本确认后才返回成功，保证消息不丢失
- RocketMQ 采用同步双写或异步复制实现类似的数据可靠性
- 百亿级场景推荐：同步刷盘 + 同步双写，最严格保证消息不丢失

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[Kafka]] — ISR 机制实现者
- [[RocketMQ]] — 同步双写实现高可用
- [[message-queue]] — 消息队列可靠性