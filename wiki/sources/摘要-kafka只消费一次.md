---
title: "摘要-kafka只消费一次"
type: source
tags: [来源, 原始文件, Kafka, 消息队列, 幂等, ExactlyOnce]
sources: [raw/09-archive/阿里二面：Kafka 怎么保证消费只消费一次的？.md]
last_updated: 2026-11-04
---

## 核心摘要

小哈学Java（2026-11-03）"阿里二面"面试题拆解：**Kafka 默认只保证 At Least Once（不丢但可能重复），"只消费一次"需要消费端额外设计**。重复消费的根因一句话——**业务处理和 offset 提交不是原子操作，中间任何中断都会造成回滚重放**。

**为什么重复**：消费者先拉取、处理业务、再提交 offset，两者之间隔着"真空期"；Broker 只记录提交过的 offset、不知道业务做完没；**rebalance 是放大器**（成员进出/宕机/扩容/心跳超时，未提交 offset 必然重放）；业务处理超过 `max.poll.interval.ms`（默认 5 分钟）主动离组也触发 rebalance。

**方案一：手动提交 offset + 业务幂等（生产首选）**
- 关闭 `enable.auto.commit`，业务全部成功后 `commitSync()`；吞吐敏感可 `commitAsync()`，退出前补 `commitSync()` 兜底
- 注册 `ConsumerRebalanceListener`，`onPartitionsRevoked` 里提交一次，把重复窗口压到最小
- **幂等才是最终防线**（手动提交只缩小窗口，`processMessage` 成功后 `commitSync` 前被 kill -9 仍会重放）：① 数据库唯一索引（消息带唯一业务 ID，最强推荐）② 去重表（消息 ID 做主键）③ Redis SETNX（性能好，注意与业务一致性）④ 乐观锁/状态机（`update ... where status='UNPAID'`，作者最偏爱，状态流转天然幂等）

**方案二：offset 与业务数据放同一个数据库事务**（下游是 MySQL）——事务成功则业务数据+offset 一起落库，失败一起回滚；不再依赖 Broker 提交位点而查 offset 表。本质是把"消费进度"和"业务结果"变原子操作。代价：业务与消费节奏耦合、吞吐下降，适合一致性要求极高、吞吐压力不大的场景（资金/账务）。

**方案三：Kafka 事务与幂等生产者（0.11+ EOS）**
- **幂等生产者**：`enable.idempotence=true`（3.0+ 默认开启，但显式配了 `acks=1`/`retries=0` 冲突配置则需显式设置）。原理：Broker 给生产者分配 PID，每条消息带单调递增 Sequence Number，Broker 记录 `<PID, 分区, 序号>`，序号比预期小即判重丢弃 → 单分区单会话内不重不丢；跨会话/跨分区要靠事务
- **事务**：`initTransactions` + `beginTransaction` + `send` + `sendOffsetsToTransaction` + `commitTransaction`/`abortTransaction`，把"消费 offset 提交"和"下游消息写入"绑成原子操作；`transactional.id` 跨会话稳定、fencing 僵尸实例；下游消费者需 `isolation.level=read_committed`
- **边界**：Kafka 事务只管 Kafka 内部 consume-transform-produce 链路，写 MySQL/调 RPC 等外部副作用管不着，该重复还是重复，最终仍要回到方案一/二的幂等设计

**三方案选型**：一般业务（下单/通知/日志）用方案一；下游是数据库且一致性要求高叠加方案二；纯 Kafka 内部流转（Streams、读 A 写 B）直接方案三。

**记忆口诀**：重复的根子在提交，解决的落点在幂等——提交时机自己控、重复窗口往小压、最后一步靠幂等。

## 关联连接
- [[Kafka]] — 主题实体（只消费一次章节）
- [[AtLeastOnce]] — 默认投递语义（本篇为"如何升级到 Exactly Once"）
- ExactlyOnce — 目标语义（无独立页，见 [[AtLeastOnce]] 与 [[Kafka]]）
- [[幂等性]] — 消费端幂等方案总纲
- [[小哈]] — 作者
- [[摘要-kafka消息不丢失]] — 姊妹篇（"不丢"视角）
- [[摘要-kafka-为什么无法100%不丢失]] — 姊妹篇（"为什么做不到"视角）
- [[摘要-kafka顺序消费]] — 同系列姊妹篇（顺序消费视角）
