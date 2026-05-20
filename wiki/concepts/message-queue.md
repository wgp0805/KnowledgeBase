---
title: "message-queue"
type: concept
tags: [消息队列, 分布式, 异步通信]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
消息队列（Message Queue, MQ）是一种基于生产者-消费者模型的异步通信机制，在分布式系统中承担解耦、削峰填谷和异步处理的角色。核心角色包括 Producer（生产者）、Broker（消息代理）和 Consumer（消费者）。

## 关键信息
- **三大角色**：Producer 发送消息、Broker 存储转发、Consumer 拉取消费
- **核心价值**：解耦（异步通信）、异步（非阻塞）、削峰填谷（应对流量洪峰）
- **存储模型**：采用追加写（CommitLog/顺序日志文件）实现高性能写入
- **主流实现对比**：RabbitMQ（Erlang/10万QPS/微秒延迟）、Kafka（Scala/20万QPS/毫秒延迟）、RocketMQ（Java/10万QPS/毫秒延迟）、Pulsar（Java/100万QPS/毫秒延迟、存算分离）
- **百亿级设计要点**：顺序IO+零拷贝、分层存储（SSD+对象存储）、一致性哈希分片、ISR副本机制、可观测性指标

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[Kafka]] — 高吞吐消息系统
- [[RocketMQ]] — 阿里开源消息中间件
- [[RabbitMQ]] — Erlang轻量消息代理
- [[Pulsar]] — 云原生消息流平台
- [[sequential-io]] — 顺序IO写入机制
- [[tiered-storage]] — 分层存储架构
- [[consistent-hashing]] — 一致性哈希分片
- [[isr]] — 副本同步机制