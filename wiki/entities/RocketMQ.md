---
title: "RocketMQ"
type: entity
tags: [消息队列, 中间件]
sources: [raw/01-articles/字节二面：如何设计一个百亿级消息队列？.md, raw/01-articles/Docker-window环境下部署RocketMq.md, raw/01-articles/springboot整合RocketMq.md]
last_updated: 2026-05-19
---

## 定义
RocketMQ 是阿里巴巴开源的分布式消息中间件，具有高吞吐量、高可用性、低延迟和强大的消息回溯能力。

## 关键信息
- 核心组件：NameServer（命名服务）、Broker（消息存储）、Producer（生产者）、Consumer（消费者）
- 消息模型：Topic（主题）、Tag（标签）、Queue（队列）
- 支持普通消息、顺序消息、事务消息、定时/延时消息
- Docker 部署包含 NameServer、Broker 和控制台（rocketmq-dashboard）
- Spring Boot 整合使用 RocketMQTemplate 发送消息
- 环境隔离方案：多环境 Topic 配置


## 关键信息（补充）
- 来自《字节二面：如何设计一个百亿级消息队列》的选型对比：RocketMQ 吞吐能力约 10万 QPS，消息延迟毫秒级
- 数据堆积能力强，支持 PB 级消息堆积
- 提供严格顺序消息、事务消息、定时/延时消息等丰富功能
- 适合需要强一致性和丰富业务特性的场景
- 同步双写和消息分级存储可应用于百亿级场景
## 关联连接
- [[SpringBoot]] — 与 Spring Boot 整合
- [[Docker]] — 容器化部署
- [[Nacos]] — 配置中心
