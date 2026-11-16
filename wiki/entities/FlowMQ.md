---
title: "FlowMQ"
type: entity
tags: [消息队列, Kafka, 统一消息系统, 存储架构, 开源]
sources: [raw/09-archive/2026-11-13 - FlowMQ Kafka：低成本存储与无感扩容解决方案.md]
last_updated: 2026-11-16
---

## 定义
FlowMQ 是基于 C++ 从零构建的统一消息系统，面向发布/订阅、队列与流处理三种消息范式，兼容 MQTT、Kafka、AMQP、NATS 等消息协议。其 Kafka 协议实现 100% 兼容标准 Kafka 客户端与 Topic/Partition/Consumer Group/认证/保留策略，现有业务无障碍迁移。

## 关键信息

### 对标 Apache Kafka 的四大痛点
1. **计算与存储紧耦合**：Partition 副本绑定指定 Broker，计算资源、磁盘容量、副本位置互相锁死
2. **存储与网络成本攀升**：每副本占独立块存储，多 AZ 部署副本间日志复制产生昂贵跨 AZ 流量
3. **扩容伴随数据迁移**：新 Broker 不自动分担已有 Partition，需 Partition Reassignment，迁移期与在线读写争用磁盘网络
4. **容量负载难均衡**：副本受所在 Broker 磁盘约束，大 Partition 造成节点间资源不均，个别节点先撞瓶颈

### 解决方案：计算存储分离 + 双存储后端
- **Kafka-S3（云上极低成本）**：S3 兼容对象存储承载数据——同存储量下对象存储价格优势明显、按使用量计费（自部署 Kafka 须提前分配高规格容量）、直接读写对象存储避免跨 AZ 复制流量。AWS 1GB/s 多 AZ 场景月成本 **18,138 美元 vs Apache Kafka 286,636 美元**；计算层完全无状态，扩缩容只加减计算节点
- **Kafka-RLog（本地低延迟）**：自研分布式 Log 存储引擎，基于流数据两特点（写入方向始终向后、历史数据写入即不改）把 Partition 日志按序切为多个 Segments（N 个只读封存 + 1 个活跃），**以 Segment 为粒度配置复制组**——历史数据副本更细粒度分散到不同节点；新节点加入自动承接新 Segment 免手动 Reassignment；故障时封存活跃 Segment 切新 Segment，复制协议简化恢复快

### Flexible Quorum 复制协议
设副本总数 N、最小写入 W、最小恢复 R，**W + R > N 即强一致，不要求多数派**（理论基础是 Flexible Paxos，对 [[Paxos]] 多数派假设的放宽）。两 AZ 场景对比：
- Apache Kafka（ISR）：4 副本每 AZ 2 个 + acks=all + min.insync.replicas=3，可容忍单节点故障；整 AZ 故障剩 2 副本不满足写入门槛，补齐需新副本追赶历史日志（大数据量时长期无法恢复）
- Redpanda（Raft）：写入与选主依赖多数派，两 AZ 各 2 副本时失去一个 AZ 仅剩 2 < 3，完全不可用（Kafka Controller 的 KRaft 同样面临）
- **FlowMQ（4-3-2 配置）**：4 副本/写入 3 确认/恢复 2 参与——单 AZ 故障后 2 存活副本满足 R=2 可读可恢复；暂不满足 W=3 但启用备用节点后新数据选用新节点为复制组，**马上自动恢复写入而不必等大规模历史数据搬迁**，全程强一致

### 适用场景
- **S3 后端**：日志留存、用户行为埋点、IoT 上报、审计流水、监控指标等持续大写入长保留场景
- **RLog 后端**：金融交易、在线风控、实时订单、游戏消息、工业控制、私有化消息中台等低延迟高可用场景

## 关联连接
- [[Kafka]] — 兼容对象与对照基准（含传统架构痛点）
- [[Paxos]] — Flexible Quorum 的理论基础（Flexible Paxos 放宽多数派）
- [[MQTT协议]] — FlowMQ 兼容的 IoT 协议
- [[RocketMQ]] / [[Pulsar]] / [[message-queue]] — 消息队列选型全景
- [[程序汪]] — 来源作者
- [[摘要-flowmq-kafka低成本存储无感扩容]] — 来源
