---
title: "Kafka"
type: entity
tags: [消息队列, 分布式系统, 流处理]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
Kafka 是由 Apache 软件基金会开发的开源分布式事件流平台，使用 Scala 和 Java 编写。最初由 LinkedIn 开发，后捐赠给 Apache。以高吞吐量、持久化存储和流处理能力著称。

## 关键信息
- 定位于高吞吐消息与日志采集场景，单集群可达 20万 QPS
- 消息延迟在毫秒级，但相比 RabbitMQ 偏高
- 数据堆积能力强，采用 Page Cache + 顺序写大幅提升性能
- Pull 模式消费，消费者自主控制消费速率
- 分区内保证消息顺序，分区间不保证全局顺序
- 使用 ISR (In-Sync Replicas) 机制保证数据可靠性
- 零拷贝技术（sendfile）优化网络传输

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[RocketMQ]] — 同类消息中间件对比
- [[RabbitMQ]] — 同类消息中间件对比
- [[Pulsar]] — 云原生消息流平台
- [[message-queue]] — 消息队列核心概念
- [[sequential-io]] — 顺序IO写入机制
- [[isr]] — ISR 副本同步机制