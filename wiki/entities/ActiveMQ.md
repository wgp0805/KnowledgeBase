---
title: "ActiveMQ"
type: entity
tags: [消息队列, JMS, 消息中间件]
sources: [raw/01-articles/4 种消息队列，如何选型？.md]
last_updated: 2026-07-07
---

## 定义
ActiveMQ 是 Apache 开源的基于 Java 的消息中间件，实现了 JMS（Java Message Service）规范，支持点对点和发布/订阅消息模型。

## 关键信息
- 官方社区对 ActiveMQ 5.x 维护越来越少，较少在大规模吞吐的场景中使用
- 目前主流消息队列选型中已不推荐

## 关联连接
- [[Kafka]] — 高吞吐替代方案
- [[RabbitMQ]] — 轻量路由替代方案
- [[RocketMQ]] — 金融级替代方案
- [[message-queue]] — 消息队列核心概念
- [[摘要-4种消息队列如何选型]] — 来源
