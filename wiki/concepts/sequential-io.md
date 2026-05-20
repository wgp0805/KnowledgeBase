---
title: "sequential-io"
type: concept
tags: [IO, 存储, 性能优化]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md]
last_updated: 2026-05-20
---

## 定义
顺序IO（Sequential I/O）是一种磁盘访问模式，数据按连续的物理地址依次写入或读取。相比随机IO，顺序IO能充分利用磁盘的预读机制和DMA传输，性能可高出数个数量级。现代消息队列通过消息追加写（Append-Only Log）将随机IO转化为顺序IO。

## 关键信息
- Kafka 和 RocketMQ 均采用消息顺序追加到 CommitLog 文件末尾的方式，最大化磁盘写入吞吐
- 零拷贝（Zero-Copy）技术通过 sendfile 系统调用，将 Page Cache 中的数据直接发送到网卡，避免内核态到用户态的数据拷贝
- 传统的盘 Path为：硬盘→Page Cache→应用程序→Socket，零拷贝缩短为：Page Cache→Socket
- 顺序写 + 零拷贝是支撑百亿级消息队列 QPS 的核心技术

## 关联连接
- [[摘要-bytedance-mq-design]] — 来源
- [[message-queue]] — 消息队列中的IO模型
- [[Kafka]] — 基于顺序IO的消息系统