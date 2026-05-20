---
title: "tiered-storage"
type: concept
tags: [存储, 架构, 分布式系统]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
分层存储（Tiered Storage）是一种将数据按访问频率和时效性分配到不同存储介质上的架构策略。热数据存放于高性能 SSD 以支持快速读写，冷数据异步转存到廉价对象存储（如 AWS S3、MinIO）以降低存储成本。

## 关键信息
- Pulsar 原生支持分层存储：热数据在 SSD，冷数据异步转存到 S3/MinIO
- Kafka 在后续版本中也引入了分层存储支持
- 百亿级消息队列每天产生约 10TB 数据，7天保存需要约 70TB 存储，分层存储可大幅降低存储成本
- 分层存储的核心挑战：如何在不影响读写性能的前提下，透明地管理数据在不同层之间的迁移

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[Pulsar]] — 原生支持分层存储的消息平台
- [[BookKeeper]] — Pulsar 底层存储引擎
- [[message-queue]] — 消息队列存储模型