---
title: "摘要-kafka高水位与leaderepoch"
type: source
tags: [来源, Kafka, 高水位, LeaderEpoch, 面试题]
sources: [raw/09-archive/面试题：Kafka 高水位了解过吗？为什么 Kafka 需要 LeaderEpoch？.md]
last_updated: 2026-11-16
---

## 核心摘要
小哈学Java 2026-11-16 面试题深拆 Kafka 副本一致性的核心机制。**高水位 HW** 定义消费者可见边界（只能消费 HW 之前的消息），HW = ISR 中所有副本 LEO 的最小值，是 `acks=all` 语义的底层支撑；**LEO** 是日志末端位移（下一条待写入消息的 offset），任意时刻 HW ≤ LEO。旧版 Kafka（0.11 之前）拿 HW 当副本截断依据有两大事故：①数据丢失——Follower 恢复后发现 LEO > HW 就截断"未提交"消息，可能删掉生产者已收到 ack 的消息；②日志分叉——两次故障切换后，不同副本的同一 offset 落着不同消息且 HW 相同，无法察觉。病根是 **HW 是依赖下一轮 Fetch 才更新的滞后值**。Kafka 0.11（KIP-101）引入 **LeaderEpoch**：每个 Partition 维护单调递增 (epoch, startOffset) 映射（leader-epoch-checkpoint 文件），Follower 恢复后先发 OffsetsForLeaderEpoch 请求问现任 Leader"我这个 epoch 的日志末端在哪"，按 Leader 返回的权威位置决定截断或继续同步——用精确日志位置取代滞后 HW，不丢不分叉。边界要分清：LeaderEpoch 管副本截断正确性，HW 管消费者可见性，前者只替换了后者的"截断职责"；生产者侧语义仍由 acks=all + min.insync.replicas 兜底。内容已并入 [[LeaderEpoch]]（新建概念页）与 [[Kafka]]。

## 关联连接
- [[LeaderEpoch]] — 本篇主角概念（新建：HW/LEO 定义与截断机制）
- [[Kafka]] — 主题本体（增量更新）
- [[小哈]] — 来源作者
- [[isr]] — HW 计算依赖的副本集合
- [[摘要-kafka消息不丢失]] / [[摘要-kafka-为什么无法100%不丢失]] — 姊妹篇（HW 截断丢数据是丢失窗口之一）
- [[AtLeastOnce]] — acks=all + min.insync.replicas 兜底的投递语义
