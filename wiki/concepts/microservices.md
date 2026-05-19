---
title: "microservices"
type: concept
tags: [架构, 微服务]
sources: [raw/01-articles/pmhub微服务学习.md]
last_updated: 2026-05-19
---

## 定义
微服务架构是一种将单一应用程序划分为一组小型独立服务的架构模式，每个服务围绕业务能力构建，可独立部署和扩展。

## 关键信息
- 服务注册与发现：Nacos / Eureka / Consul
- 网关路由：Spring Cloud Gateway / Zuul
- 配置中心：Nacos Config / Apollo
- 服务调用：OpenFeign（HTTP）或 Dubbo（RPC）
- 限流熔断：Sentinel / Hystrix / Resilience4j
- 链路追踪：SkyWalking / Zipkin / Jaeger
- 消息驱动：RocketMQ / RabbitMQ / Kafka

## 关联连接
- [[Nacos]] — 注册配置中心
- [[SpringCloudGateway]] — API 网关
- [[Sentinel]] — 限流熔断
- [[RocketMQ]] — 消息队列
