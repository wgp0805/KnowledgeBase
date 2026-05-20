---
title: "consistent-hashing"
type: concept
tags: [分布式, 负载均衡, 分片]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
一致性哈希（Consistent Hashing）是一种分布式哈希算法，将节点和数据通过哈希函数映射到同一个环上，使得在节点增减时只影响相邻节点的数据分布，最小化数据迁移量。

## 关键信息
- 固定 Hash 分片（Kafka/RocketMQ 方案）：按消息 Key（如用户ID）哈希取模，同 Key 消息路由到同一分区保证顺序
- 一致性哈希：将节点映射到哈希环上，节点增减只影响环上相邻节点，但存在数据分布不均的问题
- Kafka 将 Topic 分为多个 Partition，每个 Partition 可存储在不同 Broker 上，支持水平扩展
- 百亿级场景通常结合两种方案：固定 Hash 保证顺序 + 一致性哈希减少重平衡影响

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[message-queue]] — 消息队列分片策略
- [[Kafka]] — 基于 Partition 的分片方案