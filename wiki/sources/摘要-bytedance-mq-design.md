---
title: "摘要-bytedance-mq-design"
type: source
tags: [消息队列, 系统设计, 架构]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 核心摘要
这是一篇字节跳动系统设计面试题的深度解析，讨论如何从零设计一个每日处理百亿级消息、峰值QPS达百万级的分布式消息队列系统。

## 关联连接
- [[Kafka]] — 高吞吐分布式消息系统
- [[RocketMQ]] — 阿里巴巴开源分布式消息中间件
- [[RabbitMQ]] — Erlang编写的轻量级消息代理
- [[Pulsar]] — 云原生消息流平台
- [[message-queue]] — 消息队列核心概念
- [[sequential-io]] — 顺序IO与零拷贝技术
- [[tiered-storage]] — 分层存储架构
- [[consistent-hashing]] — 一致性哈希分片
- [[isr]] — In-Sync Replicas 副本同步机制