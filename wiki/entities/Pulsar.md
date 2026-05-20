---
title: "Pulsar"
type: entity
tags: [消息队列, 流处理, 云原生]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
Apache Pulsar 是云原生分布式消息流平台，使用 Java 编写。采用存算分离架构（计算层 Broker + 存储层 BookKeeper），支持多层存储、多租户和地域复制。

## 关键信息
- 定位于云原生、存算分离、多租户一体化消息平台
- 吞吐量高达 100万 QPS，在四者中吞吐能力最强
- 消息延迟在毫秒级
- 数据堆积能力极强，原生支持分层存储（SSD + 对象存储 S3/MinIO）
- Pull 模式消费
- 分区内支持消息顺序
- 独特优势：计算与存储分离，Broker 无状态，BookKeeper 负责持久化

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[Kafka]] — 高吞吐消息系统对比
- [[RocketMQ]] — 阿里开源消息中间件
- [[RabbitMQ]] — 轻量级消息代理
- [[BookKeeper]] — Pulsar 底层存储引擎
- [[message-queue]] — 消息队列核心概念
- [[tiered-storage]] — 分层存储架构