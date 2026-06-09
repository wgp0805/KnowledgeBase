---
title: "kafka-complete-tutorial"
type: synthesis
tags: [Kafka, 消息队列, Docker, 教程]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-06-09
---

# Apache Kafka 完整教程

## Kafka 是什么

Kafka 是 Apache 基金会旗下的分布式事件流平台，由 LinkedIn 开发后开源。它是一个**高吞吐、持久化、分布式**的消息系统，核心是一个 **Commit Log（提交日志）**，所有消息追加写入磁盘，顺序读取。

> Kafka 不是传统消息队列，而是一个**事件流平台**。

## 重点处理的问题

| 问题 | Kafka 的解法 |
|------|-------------|
| **系统解耦** | 生产者只管发消息，消费者只管收消息，双方互不知晓 |
| **削峰填谷** | 流量洪峰先打到 Kafka 缓冲，下游按能力消费，防止系统被冲垮 |
| **异步处理** | 非核心操作（发邮件、写日志）异步执行，不阻塞主流程 |
| **数据管道** | 多个系统之间的数据同步（如 MySQL → ES、日志采集 → 数仓） |
| **流处理** | 对实时数据流做过滤、聚合、Join 等计算 |

## 适合什么场景

- **日志采集与聚合**：最经典的场景，各服务日志 → Kafka → 日志中心
- **Metrics 监控数据**：服务器指标、APM 数据采集传输
- **用户行为追踪**：点击、浏览、下单等埋点事件流
- **系统间数据同步**：CDC（变更数据捕获）、数据库 Binlog 同步
- **事件驱动架构**：微服务间通过事件通信，替代同步 RPC 调用
- **大数据管道**：作为 Flink/Spark 的实时数据源

## 不适合什么场景

- **要求微秒级延迟**：Kafka 毫秒级延迟，如果需要微秒级，选 RabbitMQ 或 Pulsar
- **简单任务队列**：几百 QPS 的场景用 Kafka 太重，Redis List 或 RabbitMQ 更轻量
- **需要丰富路由规则**：Kafka 基于 Topic 的发布订阅，路由能力有限

## 核心概念

| 概念 | 说明 |
|------|------|
| **Topic（主题）** | 消息的分类，类似数据库的表 |
| **Partition（分区）** | Topic 的物理分片，并行度的基础，分区内消息有序 |
| **Producer（生产者）** | 发送消息到 Topic |
| **Consumer（消费者）** | 从 Topic 拉取消息 |
| **Consumer Group** | 一组消费者协同消费，一条消息只被组内一个消费者处理 |
| **Broker** | Kafka 服务器节点，集群由多个 Broker 组成 |
| **Offset** | 消息在分区内的偏移量，Consumer 通过 Offset 记录消费位置 |
| **ISR** | In-Sync Replicas，与 Leader 保持同步的副本集合，保证数据可靠性 |
| **ZooKeeper / KRaft** | 元数据管理。旧版依赖 ZK，新版用 KRaft 去除 ZK 依赖 |

## Docker Compose 部署教程

以下使用 **KRaft 模式**（无需 ZooKeeper），部署一个单节点 Kafka 集群，适合开发测试。

### 1. 目录结构

```
D:\dockerDir\kafka\
├── docker-compose.yml
└── data\          （Kafka 数据持久化目录）
```

### 2. 创建 docker-compose.yml

```yaml
version: '3.8'

services:
  kafka:
    image: apache/kafka:3.9.0
    container_name: kafka
    ports:
      - "9092:9092"          # 内网连接端口（PLAINTEXT）
      - "19092:19092"        # 外网连接端口（CONTROLLER）
    environment:
      # ─── 集群基础配置 ───
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@localhost:9093

      # ─── 监听器配置 ───
      # LISTENER：Kafka 内部定义的监听器名称
      # PLAINTEXT：内网监听（Docker 内部容器间通信）
      # CONTROLLER：KRaft 控制器通信
      # EXTERNAL：外网监听（宿主机或远程连接）
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093,EXTERNAL://0.0.0.0:19092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,EXTERNAL://localhost:19092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT,EXTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER

      # ─── Topic 与存储配置 ───
      KAFKA_LOG_DIRS: /var/lib/kafka/data
      KAFKA_NUM_PARTITIONS: 3                    # 默认分区数
      KAFKA_DEFAULT_REPLICATION_FACTOR: 1        # 默认副本因子（单节点=1）
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1  # Offset 主题副本数
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"    # 生产者写入不存在的 Topic 时自动创建
      KAFKA_LOG_RETENTION_HOURS: 168             # 消息保留时间（7天）
      KAFKA_LOG_RETENTION_BYTES: -1              # 消息保留大小（-1=不限）
      KAFKA_LOG_SEGMENT_BYTES: 1073741824        # 单个日志段文件大小（1GB）
      KAFKA_MESSAGE_MAX_BYTES: 1048576           # 单条消息最大字节（1MB）

      # ─── 性能参数 ───
      KAFKA_SOCKET_SEND_BUFFER_BYTES: 102400     # Socket 发送缓冲区
      KAFKA_SOCKET_RECEIVE_BUFFER_BYTES: 102400  # Socket 接收缓冲区
      KAFKA_SOCKET_REQUEST_MAX_BYTES: 104857600  # Socket 请求最大字节（100MB）
      KAFKA_COMPRESSION_TYPE: producer           # 压缩类型（producer=生产者指定）
    volumes:
      - D:\dockerDir\kafka\data:/var/lib/kafka/data
    healthcheck:
      test: ["CMD-SHELL", "kafka-topics.sh --bootstrap-server localhost:9092 --list"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### 3. 参数详解

#### 集群基础参数
| 参数 | 说明 |
|------|------|
| `KAFKA_NODE_ID` | 节点唯一 ID，集群中每个 Broker 必须不同 |
| `KAFKA_PROCESS_ROLES` | 节点角色。`broker,controller` 表示该节点既当 Broker 也当 Controller（单节点模式）；生产环境应分离角色 |
| `KAFKA_CONTROLLER_QUORUM_VOTERS` | KRaft 集群投票者列表，格式 `ID@host:port`，多个用逗号分隔 |

#### 监听器参数（最易混淆的部分）
| 参数 | 说明 |
|------|------|
| `KAFKA_LISTENERS` | Kafka 进程绑定的监听地址和端口。每个监听器有一个名字（如 PLAINTEXT），格式 `NAME://ip:port` |
| `KAFKA_ADVERTISED_LISTENERS` | **关键参数**。公告给客户端（Producer/Consumer）的连接地址。客户端连接的是这个地址，而非 LISTENERS。如果客户端连接不上，94% 是这个配错了 |
| `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP` | 将监听器名称映射到安全协议（PLAINTEXT/SSL/SASL_PLAINTEXT 等） |
| `KAFKA_INTER_BROKER_LISTENER_NAME` | Broker 之间通信使用的监听器名称 |
| `KAFKA_CONTROLLER_LISTENER_NAMES` | Controller 通信使用的监听器名称 |

> **监听器经验法则**：容器内通信用容器名（kafka:9092），宿主机通信用 localhost:19092。

#### 存储参数
| 参数 | 说明 |
|------|------|
| `KAFKA_LOG_DIRS` | 数据目录，挂载到宿主机实现持久化 |
| `KAFKA_LOG_RETENTION_HOURS` | 消息保留时间，超过后自动删除。默认 168 小时（7天） |
| `KAFKA_LOG_RETENTION_BYTES` | 基于大小的保留策略，-1 表示不限制 |
| `KAFKA_LOG_SEGMENT_BYTES` | 单个日志段文件大小，达到后滚动新文件。默认 1GB |
| `KAFKA_MESSAGE_MAX_BYTES` | 单条消息最大尺寸，超限拒绝。默认 1MB |

### 4. 启动与验证

```bash
# 创建数据目录
mkdir -p D:\dockerDir\kafka\data

# 启动容器
docker-compose -f D:\dockerDir\kafka\docker-compose.yml up -d

# 查看日志
docker logs -f kafka

# 验证 Kafka 是否就绪 —— 列出 Topic
docker exec kafka kafka-topics.sh --bootstrap-server localhost:9092 --list

# 创建测试 Topic
docker exec kafka kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test-topic --partitions 3 --replication-factor 1
```

### 5. 发送与消费测试

```bash
# 启动生产者（输入消息后回车发送）
docker exec -it kafka kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-topic
> hello kafka
> 这是一条测试消息

# 启动消费者（实时接收消息）
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning

# 查看 Topic 详情
docker exec kafka kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic test-topic
```

### 6. 常用故障排查命令

```bash
# 查看所有 Topic
docker exec kafka kafka-topics.sh --bootstrap-server localhost:9092 --list

# 查看 Consumer Group 详情
docker exec kafka kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-group --describe

# 重置 Consumer Offset 到最早
docker exec kafka kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-group --topic test-topic --reset-offsets --to-earliest --execute

# 查看 Broker 信息
docker exec kafka kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```

### 7. Spring Boot 集成示例

**pom.xml 依赖：**

```xml
<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
```

**application.yml：**

```yaml
spring:
  kafka:
    bootstrap-servers: localhost:19092
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.apache.kafka.common.serialization.StringSerializer
    consumer:
      group-id: my-group
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      auto-offset-reset: earliest
```

**生产者：**

```java
@Service
public class KafkaProducer {
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    public void send(String topic, String message) {
        kafkaTemplate.send(topic, message);
    }
}
```

**消费者：**

```java
@Component
public class KafkaConsumer {
    @KafkaListener(topics = "test-topic", groupId = "my-group")
    public void listen(String message) {
        System.out.println("收到消息: " + message);
    }
}
```

## 性能要点

- 顺序写磁盘：Kafka 消息追加到文件末尾，利用磁盘顺序 IO 远快于随机 IO
- 零拷贝（sendfile）：消费时从文件直接发送到网卡，不经过用户态，减少数据拷贝次数
- 页缓存（Page Cache）：利用操作系统空闲内存做缓存，避免 JVM GC 影响
- 批量压缩：生产者和 Broker 层面支持批量压缩（gzip/snappy/lz4/zstd），降低网络带宽消耗

## 关联连接

- [[Kafka]] — Kafka 实体页面
- [[message-queue]] — 消息队列核心概念
- [[sequential-io]] — 顺序 IO 写入机制
- [[isr]] — ISR 副本同步机制
- [[consistent-hashing]] — 一致性哈希分片
- [[tiered-storage]] — 分层存储架构
- [[RabbitMQ]] — 同类消息中间件对比
- [[RocketMQ]] — 同类消息中间件对比
- [[Pulsar]] — 云原生消息流平台
- [[摘要-bytedance-mq-design]] — 来源文章摘要
- [[Docker]] — Docker 容器部署
