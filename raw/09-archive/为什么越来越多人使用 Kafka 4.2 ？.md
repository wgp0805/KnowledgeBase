---
title: "为什么越来越多人使用 Kafka 4.2 ？"
source: "https://mp.weixin.qq.com/s/8uyLHRHWr45UJ4Fmf0-Ggw"
author:
  - "[[小锋]]"
published:
created: 2026-10-27
description: "介绍下 Kafka 4.2 这个版本新特性 ~"
tags:
  - "clippings"
---
小锋 java1234 *2026年10月27日 09:06*

大家好，我是锋哥。

> 很多人对 Kafka 的印象是“特别能扛的消息队列”。这没错，但只说了一半。Kafka 底下真正存的，是一份可以回放的提交日志；到了 4.2，它才补上队列式消费这一块：同一个分区里的消息，也能分给多个人一起处理。2026 年 9 月 29 日发布的 4.2.2，则收拾了几个容易在半夜把人叫醒的问题。今天锋哥来好好聊聊 Kafka 4.2 这个版本 。

---

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/b10969ef29f7a7169e11eabfd0f8f4d9_MD5.webp)

## 目录

- 先把 Kafka 讲明白
- 4.2 这条线强在哪
- 同一个分区，可以一起搬
- Streams 更接近能上生产的样子
- 4.2.2 补上的几处关键修复
- 在本地跑一段共享消费

## 先把 Kafka 讲明白

Kafka 是一套分布式的提交日志。生产者把消息写进主题，消息落到分区里，按到达顺序往后追加。Broker 负责把这些日志存住、转发出去；控制器负责选主、记元数据。从 4.0 开始，元数据只走 KRaft，集群里不再单独养一套 ZooKeeper。

它被用得这么广，靠的是三大特性。吞吐高，日志可以按偏移量回放，消费进度记在消费端自己手里。日志采集、订单事件、指标、流计算，中间那一层经常就是它。

传统消费者组有一条很硬的规矩：同一个分区，同一时刻只交给组里的一个消费者。分区里的顺序因此很稳。订单处理、发短信、调用一个慢接口，这种“一条一条干活”的活，也会被这条规矩卡住。人加得再多，一个分区还是只有一双手。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/37cb7f4f269517f80fb46c7f85d376bd_MD5.webp)

一条消息从写进到被读走，大致是这样：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/7dfc2d4adfc05291204e45b4037e90f4_MD5.png)

记住这张图就够了。后面 4.2 改的，主要是最后两步：谁来读，读完怎么算数。

## 4.2 这条线强在哪

4.2.0 在 2026 年 2 月 17 日发布，这一版把力气花在了能力上。共享组（Share Group）转正，Kafka Streams 的服务端再均衡也进入了核心能力的正式版。4.2.1 接着修了共享组路径上的死锁，以及 Streams 组离线迁移里的严重问题。4.2.2 是修复版，相对 4.2.1 大约收了 33 个问题，定位很明确：把 4.2 已经交给你的能力，修到能放心开着。

所以“4.2 到底有多强”，要连着看。新本事在 4.2.0，能上生产的版本号停在 4.2.2。

顺手变好的地方也值得一句。命令行工具的参数终于对齐了， `--bootstrap-server` 这种写法在各工具之间通用。 `RecordHeader` 的并发读安全了。Connect 可以用外部 JSON Schema，消息体里不必每条都塞一份结构。客户端还跟上了 Java 25。

## 同一个分区，可以一起搬

共享组是 4.2 最有存在感的变化，对应 KIP-932。消费者组按分区分配：这块分区归你，那块归我。共享组改成按记录协作。同一条分区里的消息，可以同时发给组里的多个消费者，每条消息带一把有时限的获取锁。锁的默认时长是 30 秒，期间别人拿不到这条。处理完要给个说法。

四种说法，记起来不费劲：

- `ACCEPT` ：处理好了。
- `RELEASE` ：这次没处理好，放回去，让别人或下次再试。
- `REJECT` ：这条数据本身有问题，别再投递了。
- `RENEW` ：还在处理，把锁续上。这是 4.2 新加的，专门给那些比锁时间还长的慢任务。
![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/7584b9e53e88521fb609bb8a37deb04e_MD5.jpg)

确认关系可以画成下面这样。锁住、处理、给出结论，结论再回到协调器。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/52f063ef0969954e3c4765adfdca8c34_MD5.png)

适合共享组的，是一条一条能独立完成的活：发通知、打标签、调用外部接口。分区内的严格顺序仍然交给原来的消费者组。两种组可以同时存在，按任务挑，不必把整条链路都改掉。

显式确认时， `acknowledge` 只是先记在本地， `commitSync` 或下一次 `poll` 才会把结果送到集群。下面这段按订单场景写，坏数据直接拒绝，临时失败则放回去重试。

```typescript
/** * 订单共享消费者。 * 同一个分区里的订单可以由组内多个实例一起处理。 */public class OrderShareConsumer {
    /**     * 拉取订单，并按处理结果逐条确认。     */    public void consume() {        Properties props = new Properties();        props.setProperty("
            bootstrap.servers"
          , "localhost:9092");        props.setProperty("
            group.id"
          , "order-workers");        props.setProperty("
            key.deserializer"
          ,                "
            org.apache.kafka.common.serialization.StringDeserializer"
          );        props.setProperty("
            value.deserializer"
          ,                "
            org.apache.kafka.common.serialization.StringDeserializer"
          );        // 显式确认：每条记录都要给出 ACCEPT、RELEASE 或 REJECT        props.setProperty("
            share.acknowledgement.mode"
          , "explicit");        // 严格按 
            max.poll.records
           限流，避免一次抱走太多慢订单        props.setProperty("
            share.acquire.mode"
          , "record_limit");        props.setProperty("
            max.poll.records"
          , "20");
        try (KafkaShareConsumer<String, String> consumer = new KafkaShareConsumer<>(props)) {            consumer.subscribe(List.of("orders"));            while (true) {                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(1000));                for (ConsumerRecord<String, String> record : records) {                    try {                        handleOrder(record.value());                        consumer.acknowledge(record, AcknowledgeType.ACCEPT);                    } catch (IllegalArgumentException badData) {                        consumer.acknowledge(record, AcknowledgeType.REJECT);                    } catch (Exception temporary) {                        consumer.acknowledge(record, AcknowledgeType.RELEASE);                    }                }                consumer.commitSync();            }        }    }
    /** 处理一笔订单。数据不合法时抛出 IllegalArgumentException。 */    private void handleOrder(String body) {        if (body == null || body.isBlank()) {            throw new IllegalArgumentException("空订单");        }        // 这里写真正的业务：扣库存、发短信、写下游    }}
```

调用外部接口经常超过 30 秒。这种时候在循环里对还没做完的记录发 `              AcknowledgeType.RENEW            ` ，并保持 `poll` 。续锁成功后，这条记录会再次出现在 `poll` 的结果里。续锁会拖住整组的投递进度，只留给真正慢的记录。

## Streams 更接近能上生产的样子

Kafka Streams 负责在 Kafka 里面把流算完：过滤、关联、开窗、把结果再写回主题。以前再均衡由客户端自己算任务该分给谁，成员一变，全组要停下来对一次。4.2 把 KIP-1071 的核心能力转正。任务分配改到 Broker 上持续计算，应用以 streams 组注册，观察和排障也有了单独的入口。

打开方式就一行配置：

```javascript
props.put(StreamsConfig.GROUP_PROTOCOL_CONFIG, "streams");
```

4.2.0 的离线迁移有一个会伤到数据面的缺陷，4.2.1 已修。要从经典协议迁到 streams 组，直接用 4.2.2。新应用更省事，换一个没用过的 `              application.id            ` 即可。核心能力已经可以上生产；拓扑大改、正则订阅这类边角，仍要对照官方开发指南，确认自己用到的那一块在支持范围内。

另一件天天会碰到的事是脏数据。以前处理中间抛异常，常见结局是整条流停住，或者你自己在 `mapValues` 里吞掉。KIP-1034 给异常处理器加了死信。配好主题名，内置处理器会把出错的原始记录送过去，并在头里带上异常名、堆栈、来源主题和偏移量。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Kafka%204.2%20%EF%BC%9F/2c420b95177d4165f8f91a003bf7d849_MD5.jpg)

```cs
/** * 订单流的基础配置。 * 处理失败的原始记录会进入 order-dlq，主流程继续往下走。 */public class OrderStreamConfig {
    /** 组装 Streams 配置，包含死信主题和新的再均衡协议。 */    public static Properties create() {        Properties props = new Properties();        
            props.put(StreamsConfig.APPLICATION_ID_CONFIG,
           "order-hourly");        
            props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG,
           "localhost:9092");        
            props.put(StreamsConfig.GROUP_PROTOCOL_CONFIG,
           "streams");        
            props.put(StreamsConfig.ERRORS_DEAD_LETTER_QUEUE_TOPIC_NAME_CONFIG,
           "order-dlq");        
            props.put(StreamsConfig.PROCESSING_EXCEPTION_HANDLER_CLASS_CONFIG,
                          "
            org.apache.kafka.streams.errors.LogAndContinueProcessingExceptionHandler"
          );        return props;    }}
```

自己写处理器时，在 `handleError` 里返回 `              Response.resume            ` ，带上要送进死信的 `ProducerRecord` 。想让任务停下来，就返回 `              Response.fail            ` 。

还有一个小而实用的变化：锚定标点（KIP-1146）。以前按墙钟调度，第一次触发取决于进程什么时候跑起来，很难卡在整点。现在可以指定第一次的时刻，后面的触发按这个起点加间隔推。

```typescript
/** * 每小时整点结算一次。 * startTime 钉住第一次触发的时刻。 */@Overridepublic void init(ProcessorContext<String, String> context) {    context.schedule(            Instant.parse("2026-10-26T00:00:00Z"),            Duration.ofHours(1),            PunctuationType.WALL_CLOCK_TIME,            timestamp -> settleHourlyOrders());}
```

## 4.2.2 补上的几处关键修复

4.2.2 的发布说明读起来像一份维修单。挑几条真正会影响线上判断的：

精确一次那边，恢复结束时写下的检查点，过去可能一直留到运行中。进程要是不干净地挂掉，状态清理会被跳过。这个口子补上了。

`              KafkaStreams.removeStreamThread            ` 可能和“换一条流线程”的异常处理撞在一起，形成死锁。动态缩容的应用会踩到。

消费者组在迁移策略已经关掉时，仍可能接受经典协议的新成员，最后卡在混合协议里出不来。降级时，如果经典成员的元数据特别大，组的协调状态也可能写成以后加载不了。这两处都修了。

`ListDeserializer` 遇到写到一半就截断的数据，以前会静静吐出一条残缺记录。现在会把这种输入当成错误。

监控也诚实了一点。 `record-e2e-latency-max` 过去只算了拉取，漏了处理耗时，和 KIP-613 的定义对不上。升级后看这块延迟，数字会把处理时间算进去，告警阈值记得重新看一眼。

另外，重新认证失败后消费者空转打满 CPU、缓存中的分区 Leader 已经离开集群时 Admin 客户端干等整个超时，这两类“看起来像卡住了”的问题也有了着落。协议解码对超大数组和超多标签字段做了分配上限，jackson-databind、lz4-java、jline 也跟着做了安全升级。

## 在本地跑一段共享消费

单机试用直接用官方镜像 `apache/kafka:4.2.2` 。共享组在单节点上要把协调主题的副本数降到 1，否则主题建不起来。下面这份编排按官方单节点示例改过，镜像版本是 4.2.2。

```ruby
services:  broker:    image: apache/kafka:4.2.2    hostname: broker    ports:      - "9092:9092"    environment:      KAFKA_NODE_ID: 1      KAFKA_PROCESS_ROLES: broker,controller      KAFKA_LISTENERS: CONTROLLER://:29093,PLAINTEXT_HOST://:9092,PLAINTEXT://:19092      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT_HOST://localhost:9092,PLAINTEXT://broker:19092      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@broker:29093      CLUSTER_ID: 4L6g3nShT-eMCtK--X86sw      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1      KAFKA_SHARE_COORDINATOR_STATE_TOPIC_REPLICATION_FACTOR: 1      KAFKA_SHARE_COORDINATOR_STATE_TOPIC_MIN_ISR: 1
```

集群起来之后，先写几笔订单。生产者这边和以前一样，4.2 没有换掉这套 API。

```typescript
/** * 往 orders 主题写一笔订单，供共享消费者读取。 */public class OrderProducer {
    /** 发送一条订单消息。 */    public void send(String orderId, String body) {        Properties props = new Properties();        props.setProperty("
            bootstrap.servers"
          , "localhost:9092");        props.setProperty("
            key.serializer"
          ,                "
            org.apache.kafka.common.serialization.StringSerializer"
          );        props.setProperty("
            value.serializer"
          ,                "
            org.apache.kafka.common.serialization.StringSerializer"
          );
        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {            producer.send(new ProducerRecord<>("orders", orderId, body));            producer.flush();        }    }}
```

然后把前面的 `OrderShareConsumer` 起两份，指向同一个 `              group.id            ` 。两份实例会从同一条分区里各自领走不同的订单。

[2026年，锋哥又开始收Java+AI大模型编程学员了！目前活动，送AI编程+Python+AI大模型VIP。。](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247572972&idx=1&sn=b1a5984d81f733dde57e775e57d41ac2&scene=21#wechat_redirect)