---
title: "摘要-kafka消息不丢失"
type: source
tags: [来源, 原始文件, Kafka, 消息队列, 面试题]
sources: [raw/09-archive/面试官：Kafka 如何保证消息不丢失？.md]
last_updated: 2026-10-26
---

## 核心摘要

犬小哈从面试视角剖析 Kafka 消息防丢失问题。核心框架：消息丢失只可能发生在三个环节——**生产者发消息、Broker 存消息、消费者消费**，防丢失就是三端各配一手，缺一不可。生产端核心是 `acks=all` + `retries` 重试 + 带回调的 `send()` 失败落库兜底（Kafka 3.0 起默认 acks 已改为 all）；Broker 端靠多副本：`replication.factor>=3` + `min.insync.replicas>=2`（给 acks=all 兜底，防 ISR 缩水退化成 acks=1）+ `unclean.leader.election.enable=false`（宁可分区不可用也不让落后副本上位）；消费端九成九的事故出在 offset 自动提交——必须 `enable.auto.commit=false`，**先消费后提交**，最多重复消费不会丢。进阶结论：消息不丢的代价是可能重复，所以"At Least Once + 消费端幂等"才是生产可用的组合；Exactly-Once 虽可达成（幂等生产者 + 事务 + read_committed）但有性能开销。记忆口诀九字："发得稳、存得牢、提得晚"。

## 关联连接

- [[Kafka]] — 主题本体（已并入"消息不丢失"章节）
- [[isr]] — acks=all 背后的副本同步机制
- [[AtLeastOnce]] — 至少一次投递 + 消费端幂等的生产可用组合（本篇提炼概念）
- [[幂等性]] — 幂等生产者防重 / 消费端幂等防重复
- [[死信队列]] — 重试超时后的人工兜底链路
- [[message-queue]] — 消息队列核心概念
- [[摘要-kafka顺序消费]] — 同作者姊妹篇（顺序消费三端打法）
- [[重复消费解决方案]] — 防丢失的另一面：重复消费如何治理
- [[小哈]] — 来源作者
