---
title: "MQ"
type: entity
tags: [消息队列, 中间件, 概念]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
MQ（Message Queue，消息队列）是应用间解耦、隔离、事件通知的中间件，比 Spring Event 更强大更重，适合应用间通信。

## 关键信息
- **定位**：应用间解耦、隔离、事件通知
- **vs Spring Event**：MQ 更强大更重，适合应用间；Spring Event 小巧，适合应用内
- **典型场景**：订单支付/完成/履约完成等事件广播给下游微服务
- **常见实现**：[[Kafka]]、[[RabbitMQ]]、[[RocketMQ]]、[[ActiveMQ]]

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 与 Spring Event 对比来源
- [[SpringEvent]] — 对比方案
- [[Kafka]] — 典型实现
- [[RabbitMQ]] — 典型实现
- [[RocketMQ]] — 典型实现
- [[ActiveMQ]] — 典型实现
- [[PublishSubscribePattern]] — 共同的模式基础
