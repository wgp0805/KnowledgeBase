---
title: "SpringCloudAlibaba"
type: entity
tags: [Spring, 微服务, 中间件]
sources: [raw/02-papers/Spring Cloud Alibaba笔记.pdf, raw/01-articles/Spring Cloud Stream 整合 RocketMQ 完全指南.md]
last_updated: 2026-07-21
---

## 定义
Spring Cloud Alibaba（SCA）是阿里巴巴基于 Spring Cloud 规范实现的一站式微服务解决方案，提供 Nacos（注册配置）、Sentinel（流量治理）、RocketMQ（消息）、Seata（分布式事务）等生态组件。

## 关键信息
- **版本兼容性（关键）**：SCA 版本必须与 Spring Boot / Spring Cloud 严格对齐
  - SCA 2023.0.x → Spring Cloud 2023.0.x → Spring Boot 3.2.x
  - SCA 2022.0.x → Spring Cloud 2022.0.x → Spring Boot 3.0.x/3.1.x
  - SCA 2021.0.x → Spring Cloud 2021.0.x → Spring Boot 2.6.x/2.7.x
  - SCA 2.2.x → Spring Cloud Hoxton → Spring Boot 2.2.x/2.3.x
- **RocketMQ Binder**：`spring-cloud-starter-stream-rocketmq` 实现 SCS 与 RocketMQ 的桥接
- **完整版本对照表**：参见 [SCA 版本说明](https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E)

## 关联连接
- [[摘要-spring-cloud-alibaba]] — Spring Cloud Alibaba 笔记
- [[摘要-spring-cloud-stream-rocketmq]] — SCS + RocketMQ 整合指南
- [[SpringCloudStream]] — 事件驱动微服务抽象层
- [[RocketMQ]] — 消息中间件
- [[Nacos]] — 注册配置中心
- [[microservices]] — 微服务架构
