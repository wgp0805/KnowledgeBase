---
title: "Zuul"
type: entity
tags: [网关, Netflix, 微服务, 已弃用]
sources: [raw/01-articles/面试官：为什么需要 Gateway 网关，它有什么作用？.md]
last_updated: 2026-07-08
---

## 定义

Netflix 开源的 API 网关组件，基于同步阻塞（Servlet）模型，是 Spring Cloud 早期默认网关方案，现已被 Spring Cloud Gateway 替代。

## 关键信息

- **编程模型**：同步阻塞（Servlet），基于 ZuulFilter
- **性能**：一般，线程池模型，每个请求占用一个线程
- **Filter 种类**：pre / route / post / error 四种
- **限流支持**：需额外集成，无内置限流组件
- **Spring 官方支持**：已弃用，不在 Spring Cloud 官方路线图内
- **社区活跃度**：低
- **与 Gateway 本质区别**：Gateway 基于 WebFlux + Netty 异步非阻塞，少量线程处理大量并发；Zuul 1.x 同步阻塞，性能差距明显

## 关联连接
- [[SpringCloudGateway]] — 官方推荐的替代方案
- [[网关]] — 网关概念与五大职责
- [[microservices]] — 微服务架构
- [[摘要-gateway网关]] — Gateway vs Zuul 对比来源
