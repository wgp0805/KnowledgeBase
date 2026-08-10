---
title: "microservices"
type: concept
tags: [架构, 微服务]
sources:
  - raw/01-articles/pmhub微服务学习.md
  - raw/02-papers/微服务治理技术白皮书.pdf
  - raw/02-papers/Spring Cloud Alibaba笔记.pdf
last_updated: 2026-05-22
---

## 定义
微服务架构是一种将单一应用程序划分为一组小型独立服务的架构模式，每个服务围绕业务能力构建，可独立部署和扩展。

## 关键信息
- 服务注册与发现：Nacos / Eureka / Consul（见 [[服务发现]]）
- 服务通信：同步 RPC（REST/gRPC）与异步消息（见 [[进程间通信]]）
- 网关路由：Spring Cloud Gateway / Zuul
- 配置中心：Nacos Config / Apollo
- 服务调用：OpenFeign（HTTP）或 Dubbo（RPC）
- 限流熔断：Sentinel / Hystrix / Resilience4j
- 链路追踪：SkyWalking（未收录）/ Zipkin / Jaeger
- 消息驱动：RocketMQ / RabbitMQ / Kafka

### 通信选型核心原则
- **外部接口用同步 REST**：实时响应、对外暴露、第三方对接、简单低频短链路
- **内部核心链路/非实时流程用异步消息**：通知/日志/数据同步/积分发放、高并发削峰、需要最终一致性的链路
- 同步兜底用户体验，异步保障系统稳定，配合熔断、降级、事务消息、API 版本治理

## 关联连接
- [[进程间通信]] — 服务通信选型核心概念
- [[同步RPC]] — 同步调用模式
- [[异步消息]] — 异步消息模式
- [[熔断]] — 限流熔断治理
- [[服务发现]] — 注册与寻址
- [[Nacos]] — 注册配置中心
- [[SpringCloudGateway]] — API 网关
- [[Sentinel]] — 限流熔断
- [[RocketMQ]] — 消息队列
- [[摘要-microservice-governance]] — 微服务治理白皮书
- [[摘要-spring-cloud-alibaba]] — Spring Cloud Alibaba 笔记
- [[摘要-微服务架构-进程间通信]] — 进程间通信读书笔记
