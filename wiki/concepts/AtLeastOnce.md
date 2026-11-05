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

### 为什么做不到 Exactly Once（2026-10-29 来源：[[摘要-kafka-为什么无法100%不丢失]]）

Kafka 的 at-least-once 语义能达成，但"绝对不丢"不在承诺列表里，三个硬限制见 [[Kafka]] 对应章节：① PageCache 与物理磁盘永远有时间差（确认只到内存）；② 同步复制性能代价高到难以接受；③ 分布式系统对抗不了所有副本同时失效的组合故障。工程共识：**"概率足够小 + 出了问题可兜底"** 优于追求数学上的 0 丢失。

### 从 At Least Once 升级到 Exactly Once（2026-11-03 来源：[[摘要-kafka只消费一次]]）

生产者/消费者侧的完整落地路径（详见 [[Kafka]] 对应章节）：
1. **手动提交 + 业务幂等**：关自动提交、业务成功后 `commitSync()`、`onPartitionsRevoked` 补提交；幂等四选一——数据库唯一索引（最强）/ 去重表 / Redis SETNX / 乐观锁状态机
2. **offset 与业务同库事务**：业务数据 + offset 一起落库/回滚，把"消费进度"与"业务结果"变原子操作（代价是吞吐下降）
3. **Kafka 事务 EOS**：幂等生产者（PID + Sequence Number，单分区单会话）+ 事务（`sendOffsetsToTransaction`），但只覆盖 Kafka 内部链路，外部副作用仍需业务幂等

核心认知：**At Least Once 是 Kafka 的默认承诺，Exactly Once 是"Kafka 事务 + 业务幂等"联合才能逼近的目标**，纯靠配置无法覆盖外部系统副作用。

## 关联连接

- [[Kafka]] — 典型实现场景
- [[摘要-kafka只消费一次]] — 来源（三方案落地）
- [[幂等性]] — 兜住"重复"那一面的配套机制
- [[isr]] — 存储侧"宁可写失败不可写丢"的副本机制
- [[死信队列]] — 重试救不回来的消息的人工兜底
- [[message-queue]] — 所属领域
- [[摘要-kafka消息不丢失]] — 来源
- [[摘要-kafka-为什么无法100%不丢失]] — 来源（为什么做不到 100%）
- [[摘要-rabbitmq-idempotency]] — RabbitMQ 场景下的同主题方案（5 种幂等）
