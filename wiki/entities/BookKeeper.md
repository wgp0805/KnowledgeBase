---
title: "BookKeeper"
type: entity
tags: [分布式存储, 预写日志]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
Apache BookKeeper 是分布式预写日志（WAL）系统，专为低延迟、高持久性的日志存储而设计。它是 Apache Pulsar 的底层存储引擎。

## 关键信息
- 作为 Pulsar 的存储层，实现存算分离架构
- Broker 只负责计算，BookKeeper 负责消息持久化
- 原生支持分层存储：热数据在 SSD，冷数据异步转存到 S3/MinIO
- 支撑 Pulsar 高达 100万 QPS 的吞吐能力

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[Pulsar]] — 云原生消息流平台
- [[tiered-storage]] — 分层存储架构