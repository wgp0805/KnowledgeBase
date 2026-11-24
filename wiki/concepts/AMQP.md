---
title: "AMQP"
type: concept
tags: [概念, 消息队列, 协议, 标准]
sources: ["raw/09-archive/SpringBoot4.2正式发布，人麻了！.md"]
last_updated: 2026-11-24
---

## 定义
AMQP（Advanced Message Queuing Protocol）是应用层消息队列协议标准。需要区分两个不兼容的版本：**AMQP 0-9-1**（[[RabbitMQ]] 的原生协议，灵活但偏私有）与 **AMQP 1.0**（OASIS 标准化协议，跨厂商跨语言一致性好）。

## 关键信息
- **0-9-1**：RabbitMQ 长期使用的默认协议，围绕 exchange/queue/binding 建模，Java 生态通过 `amqp-client` 与 Spring AMQP 使用
- **1.0**：完全不同的线格式与模型（link/session 概念），由 OASIS 标准化，理论上任何符合标准的 broker 都能互通
- **两者不是替代关系**：在 RabbitMQ 3.x/4.x 里可以共存，客户端按端口/插件选择；老系统不必强制迁移
- **Spring Boot 4.2 新增 1.0 官方支持**：把 1.0 收进官方 starter，不用再自己拼第三方库；受益场景是**多语言架构**——.NET/Go/Python 服务与 Java 用同一套标准协议通信，减少协议适配层维护
- **选型判断**：全 Java + 全 0-9-1 → 升级 4.2 不强制迁移；要做多语言异构或对接标准化消息中间件 → 值得评估 1.0
- **同类概念对照**：MQTT（IoT 轻量）、Kafka 协议（日志型流）、[[Pulsar]]（计算存储分离）

## 关联连接
- [[RabbitMQ]] — 两种 AMQP 的主要载体
- [[SpringBoot]] — 4.2 提供官方 1.0 支持
- [[异步消息]] — 所属架构能力
- [[MQ]] / [[message-queue]] — 上层选型视角
- [[Kafka]] — 不同路线对照
- [[摘要-springboot4-2发布]] — 来源
