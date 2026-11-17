---
title: "LeaderEpoch"
type: concept
tags: [Kafka, 副本一致性, 高水位, 概念]
sources: [raw/09-archive/面试题：Kafka 高水位了解过吗？为什么 Kafka 需要 LeaderEpoch？.md]
last_updated: 2026-11-16
---

## 定义
LeaderEpoch 是 Kafka 0.11（KIP-101）引入的副本截断机制：每个 Partition 维护一个 `(epoch, startOffset)` 单调递增映射——epoch 在每次 Leader 换届时 +1，startOffset 记录该届 Leader 开始写入的位置；Broker 在日志目录下以 `leader-epoch-checkpoint` 文件持久化（内存另持一份）。它解决的核心问题：**旧版拿高水位 HW 做副本截断依据，因 HW 更新滞后导致数据丢失与日志分叉**。

## 关键信息

### 前置概念对：HW 与 LEO
- **LEO（Log End Offset）**：日志末端位移，下一条待写入消息的 offset；Leader 写一条推一次，Follower 拉到消息就推
- **HW（High Watermark）**：消费者可见边界——只能消费 HW 之前的消息（不含 HW），HW 之后即使已写进 Leader 日志也是"未提交"状态；对 Leader 而言 HW = ISR 中所有副本 LEO 的最小值（这就是"一条消息被 ISR 全部副本收到才可见"的由来，也是 [[isr]] 与 acks=all 语义的底层支撑）
- Follower 更新自己 HW 的规则：取"自己的 LEO"与"Leader Fetch 响应返回的 HW"两者较小值
- 任意时刻 HW ≤ LEO

### 旧机制的病根：HW 天生慢半拍
HW 依赖 Follower **下一轮 Fetch** 才能反映上一轮同步进度（平时几十毫秒无感，宕机重启时致命）。两个经典事故（两副本、acks=1、min.insync.replicas=1 推演）：
1. **数据丢失**：Leader 写入 m2（LEO 3）并 ack → 宕机 → Follower 升主（HW=2）→ 原 Leader 恢复后发现 LEO=3 > HW=2，按规则截断 → m2 永久消失（生产者却收到过 ack）
2. **日志分叉（divergence）**：A、B 同时宕机 → B 先恢复升主在 offset=2 写入 m3 → A 恢复截断自己的 m2 同步 m3 → B 再宕机、A 升主在 offset=2 写入 m4 → 最终 B 的 offset=2 是 m3、A 的是 m4，HW 相同，谁也发现不了——消费者从不同副本读到不同数据，排查极难
- 病根一句话：**HW 是带延迟的滞后值，拿它当截断依据，恢复时可能删掉已提交消息或保留不该保留的位置**

### LeaderEpoch 的救场逻辑：截断前先问 Leader
Follower 恢复后（或 Fetch 响应中发现 epoch 变大）发 OffsetsForLeaderEpoch 请求：
- **Leader 手里 epoch 更大**：说明中间换过主，返回新 epoch 的 startOffset（上一 epoch 实际末端）——Follower 截断到这个**权威位置**再同步
- **epoch 一致**：返回当前 epoch 的 LEO——Follower 自己 LEO 更小就继续拉取；**哪怕自己的 LEO 超过了 HW 也不截断**（只要不超过 Leader 的 LEO，消息都安全保留）
- 场景一回放：A 恢复后问 B，B 答"epoch 1 从 offset=2 开始"，A 的 epoch 0 数据没超过该位置，无多余数据可截——注意 **m2 本身没救回来**：LeaderEpoch 保证的是**副本之间不丢不分叉**；"生产者收到 ack 但消息丢"由生产端语义（acks=all + min.insync.replicas ≥ 2）兜底，两者配合才完整
- 场景二回放：A 按 Leader 给的权威 startOffset 截断重同步，epoch 链条把每次换届记得明明白白，分叉藏不住

### 新旧机制对比
| 维度 | 基于 HW 截断（旧） | 基于 LeaderEpoch（新） |
|---|---|---|
| 截断依据 | 本地 HW（滞后值） | Leader 返回的权威日志位置 |
| 数据丢失 | 可能删掉已提交消息 | 不会，位置由 Leader 确认 |
| 日志分叉 | 可能发生 | epoch 链单调追溯，不会 |
| 换届感知 | 无感知只认 offset | epoch+1，每次换届有记录 |

### 配套生产配置
- `unclean.leader.election.enable`：0.11 起默认从 true 改 false（KIP-106），宁可牺牲可用性不冒丢数据风险——金融/计费场景务必 false
- `acks=all` + `min.insync.replicas=2`（三副本集群）：消息至少 2 副本收到才算提交，与 LeaderEpoch 配合堵住丢数据的三道口子
- 消费端关自动提交，与 HW 可见性配合解决重复消费

### 职责边界（高频追问）
有了 LeaderEpoch 为什么还需要 HW？**两码事**：HW 管消费者可见性与"已提交"语义；LeaderEpoch 管副本截断的正确性——它只替换了 HW 的"截断职责"，不是替换 HW 本身。

## 关联连接
- [[Kafka]] — 所属系统（副本机制总览）
- [[isr]] — HW 计算依赖的同步副本集合
- [[AtLeastOnce]] — acks=all + min.insync.replicas 对应的投递语义
- [[摘要-kafka高水位与leaderepoch]] — 来源
- [[摘要-kafka消息不丢失]] / [[摘要-kafka-为什么无法100%不丢失]] — 姊妹视角（HW 截断丢数据是丢失窗口之一）
- [[摘要-kafka顺序消费]] — 同作者系列（副本机制之外的分区内顺序保障）
- [[小哈]] — 来源作者
