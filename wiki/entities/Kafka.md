---
title: "Kafka"
type: entity
tags: [消息队列, 分布式系统, 流处理]
sources: [raw/09-archive/字节二面：如何设计一个百亿级消息队列？.md, raw/09-archive/4 种消息队列，如何选型？.md, raw/09-archive/2026-10-22 - 面试官：Kafka 如何实现顺序消费？.md, raw/09-archive/面试官：Kafka 如何保证消息不丢失？.md, "raw/09-archive/为什么越来越多人使用 Kafka 4.2 ？.md"]
last_updated: 2026-10-27
---

## 定义
Kafka 是由 Apache 软件基金会开发的开源分布式事件流平台，使用 Scala 和 Java 编写。最初由 LinkedIn 开发，后捐赠给 Apache。以高吞吐量、持久化存储和流处理能力著称。号称大数据的杀手锏，在数据采集、传输、存储中发挥举足轻重的作用。

## 关键信息
- 定位于高吞吐消息与日志采集场景，单集群可达 20万 QPS
- 消息延迟在毫秒级，但相比 RabbitMQ 偏高
- 数据堆积能力强，采用 Page Cache + 顺序写大幅提升性能
- Pull 模式消费，消费者自主控制消费速率
- 分区内保证消息顺序，分区间不保证全局顺序
- 使用 ISR (In-Sync Replicas) 机制保证数据可靠性
- 零拷贝技术（sendfile）优化网络传输
- 基于 Zookeeper 的分布式消息流平台，支持多分区、多副本
- Zookeeper 管理集群配置、leader 选举、Consumer Group 变化时 rebalance

### 重要概念
- **Topic（主题）**：消息的分类，相当于数据库中的表
- **Partition（分区）**：Topic 可拆分为多个分区，部署在不同机器上实现伸缩性
- **批次（Batch）**：消息分批次写入 Kafka 以提高效率
- **Consumer Group（消费者群组）**：由一个或多个消费者组成
- **Broker**：独立的 Kafka 服务器，接收消息、设置偏移量、提交到磁盘
- **Rebalance（重平衡）**：消费者组内实例挂掉后，其他实例自动重新分配订阅分区

### 分区策略
分区是 Kafka 读写数据的最小粒度，支持三种策略：顺序轮询、随机轮询、key hash。相同 Topic 和分区的消息存放在同一个批次中，由独立线程发送到 Broker。

### 优缺点
**优点：**
- 高吞吐、低延迟（每秒几十万条，毫秒级延迟）
- 高伸缩性（Topic 多分区可分布在不同 Broker）
- 高稳定性（分布式多副本，节点宕机不影响集群）
- 持久性、可回溯（消息持久化到磁盘，支持数据回溯）
- 消息有序（保证消息被消费且仅被消费一次）
- 有优秀的 Kafka-Manager Web 管理界面

**缺点：**
- 单机超过 64 个队列/分区时 Load 明显飙升，响应时间变长
- 不支持消息路由、不支持延迟发送、不支持消息重试
- 社区更新较慢

### 选型建议
适合追求高吞吐量的场景，一开始就设计用于日志收集和传输。大型公司建议选用，如果有日志采集功能，首选 Kafka。

### 顺序消费（2026-10-22 来源：[[摘要-kafka顺序消费]]）
Kafka 只保证**分区内有序**，从不承诺全局有序。要实现业务级顺序消费，三层各有一套打法：
- **生产端**：①按业务 key 写入——相同 key 经过哈希落到同一分区，分区内自然是队头队尾的顺序；②防重试乱序——消息未确认时下一条不能写，需开启**幂等生产者**（Producer ID + Sequence Number 去重，`enable.idempotence=true`）并把 `max.in.flight.requests.per.connection` 控制在 5 以内让 Broker 按序确认；③用**粘性分区策略**提升 batch 攒批效率
- **消费端**：分区内有序 ≠ 业务顺序。通用方案是**按 key 路由内存队列**——消费者拿到消息先按 key 哈希放入线程内多个内存队列，同 key 消息单线程串行、不同 key 并行，兼顾吞吐与顺序；配套要求就是幂等消费（[[幂等性]]/唯一键/状态机校验）兜底
- **架构/运维坑**：①分区扩容会改变 key→分区映射，跨分区查 key 顺序会跳变，扩容要选中低峰并重放兜底；②消费组 **rebalance**（消费者进出组）会导致 offset 未提交被重复消费甚至消费中断——消费逻辑保持幂等 + 用手动 ack 和 rebalance 监听器控制提交时机；③消费失败重试会打乱顺序，需用重试队列+死信队列按序重投

### 消息不丢失（2026-10-26 来源：[[摘要-kafka消息不丢失]]）
消息丢失只可能发生在三个环节——**生产者发消息、Broker 存消息、消费者消费**，防丢失就是三端各配一手，缺一不可（口诀：发得稳、存得牢、提得晚）：
- **生产端**：`acks=all`（所有 ISR 副本写入才确认）+ `retries` 调大配合 `delivery.timeout.ms` 控制总重试时长 + **用带回调的 `send()`**（发后即忘连失败都不知道，重试救不回来的要落库/告警人工兜底）+ 开启幂等防重试导致的重复。注意 `acks=all` 单独用不够——ISR 里只剩 Leader 一个副本时 `all` 会退化成 `1`，必须配 Broker 端 `min.insync.replicas` 堵漏洞。Kafka 3.0 起默认 acks 已改为 `all`，但生产环境仍建议显式配置
- **Broker 端**：`replication.factor>=3`（用多副本代替 RAID）+ `min.insync.replicas>=2`（ISR 缩水到 1 副本时写入直接抛 `NotEnoughReplicasException`——宁可写失败、不可写丢，CAP 取舍）+ `unclean.leader.election.enable=false`（禁止落后的非 ISR 副本当 Leader，0.11 起默认 false，防脏选举永久丢消息）
- **消费端**：九成九的事故出在 offset 自动提交（默认每 5 秒提交，不管消息处理完没有——提交 offset 和处理消息是两条线）。正确姿势：`enable.auto.commit=false`，**先消费后提交**（处理完 `commitSync()`）；处理失败的消息不提交，下次 poll 还能拉到，最多重复消费不会丢

高频追问：① `acks=all` 不一定不丢（ISR 缩水退化成 acks=1）；② Exactly-Once 需幂等生产者 + 事务 + 消费端 `read_committed`，有性能开销，大部分业务选 [[AtLeastOnce]] + 消费端幂等；③ 顺序保证靠同业务 key 路由同分区，`max.in.flight.requests.per.connection>1` 且未开幂等时重试会乱序，开幂等后 Kafka 保证重试不乱序；④ 消息积压快速扩容消费者（数量不超过分区数）或新建更多分区的主题搬运。

### Kafka 4.2 新特性（2026-10-27 来源：[[摘要-kafka42共享组]]）
- **共享组（Share Group，KIP-932）转正**：详见 [[共享组]]——按记录协作消费，同一分区消息可同时分给组内多个消费者，30 秒获取锁 + ACCEPT/RELEASE/REJECT/RENEW 四种确认；"发通知/打标签/调外部接口"这类一条一条独立完成的活不再被分区独占卡死，严格顺序场景仍用传统消费者组，两种组可并存按任务挑
- **Streams 服务端再均衡（KIP-1071 转正）**：任务分配从客户端各自计算改为 Broker 持续计算，应用以 streams 组注册，单独的观察与排障入口；一行 `GROUP_PROTOCOL_CONFIG=streams` 开启。注意 4.2.0 的离线迁移有伤数据面缺陷、4.2.1 已修——迁移用 4.2.2，新应用换一个新的 application.id 即可；拓扑大改、正则订阅等边角需对照官方开发指南确认支持范围
- **Streams 死信队列（KIP-1034）**：给异常处理器加了死信——配 `ERRORS_DEAD_LETTER_QUEUE_TOPIC_NAME_CONFIG` 指定主题后，内置处理器把处理失败的**原始记录**送过去，header 带异常名/堆栈/来源主题与偏移量，主流程继续；自写处理器 `handleError` 返回 `Response.resume`（带 ProducerRecord）或 `Response.fail`（让任务停下）。以前常见结局是整条流停住或在 mapValues 里吞异常
- **锚定标点（KIP-1146）**：`ProcessorContext.schedule` 可指定第一次触发的时刻（如 `Instant.parse("2026-10-26T00:00:00Z")` 定整点），后续按起点+间隔推算——以前按墙钟调度，第一次触发取决于进程启动时机，很难卡在整点
- **4.2.x 版本线**：4.2.0（2026-02-17）出能力，4.2.2（2026-09-29）修到能放心上生产（相对 4.2.1 收约 33 个修复）。关键修复：精确一次恢复结束时写的检查点过去可能直留到运行中，不干净挂掉会跳过状态清理；`KafkaStreams.removeStreamThread` 与"换一条流线程"的异常处理撞成死锁（动态缩容踩）；迁移策略已关时仍收经典协议新成员卡在混合协议；降级时经典成员元数据过大致协调状态以后加载不了；`ListDeserializer` 遇截断数据以前静默吐残缺记录，现在当错误；`record-e2e-latency-max` 口径补上处理耗时（升级后告警阈值要重看）；重新认证失败消费者空转打满 CPU；Admin 客户端对已离开集群的分区 Leader 不再干等整个超时；协议解码对超大数组/超多标签加分配上限；jackson-databind/lz4-java/jline 安全升级
- **杂项**：CLI 工具参数对齐（`--bootstrap-server` 各工具通用）、`RecordHeader` 并发读安全、Connect 支持外部 JSON Schema（消息体不必每条塞结构）、客户端跟进 Java 25
- **元数据演进注记**：Kafka 4.0 起元数据只走 KRaft，集群不再单独养一套 ZooKeeper——本页上方"基于 Zookeeper"等条目为旧版（ZK 时代）描述，以实际版本为准

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[RocketMQ]] — 同类消息中间件对比
- [[RabbitMQ]] — 同类消息中间件对比
- [[Pulsar]] — 云原生消息流平台
- [[message-queue]] — 消息队列核心概念
- [[sequential-io]] — 顺序IO写入机制
- [[isr]] — ISR 副本同步机制
- [[摘要-kafka顺序消费]] — 来源（2026-10-22 顺序消费面试题拆解）
- [[幂等性]] — 幂等生产者/幂等消费概念
- [[小哈]] — 来源作者
- [[死信队列]] — 重试兜底相关概念
- [[AtLeastOnce]] — 消息不丢的投递语义与消费端幂等组合（2026-10-26 提炼）
- [[摘要-kafka消息不丢失]] — 来源（2026-10-26 消息不丢失面试题拆解）
- [[共享组]] — 4.2 新消费组模式（KIP-932，按记录协作）
- [[摘要-kafka42共享组]] — 来源（2026-10-27 Kafka 4.2 新特性拆解）
- [[小锋]] — 来源作者
