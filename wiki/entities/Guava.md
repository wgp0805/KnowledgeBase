---
title: "Guava"
type: entity
tags: [Java, Google, 工具库, 限流]
sources: [raw/09-archive/秒杀系统怎么区分真实用户和黄牛脚本？.md, raw/09-archive/2026-10-01 - 消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思.md]
last_updated: 2026-10-08
---

## 定义
Guava 是 Google 开源的 Java 核心工具库，提供集合、缓存、并发、限流等基础工具。其中 `RateLimiter` 是单机限流的常用实现。

## 关键信息
- 厂商：Google
- 核心组件：`RateLimiter`（令牌桶单机限流）、`Cache`（本地缓存）、`EventBus`、`Optional` 等
- 在秒杀防刷中的角色：[[两级限流]] 的本地粗筛层——按实例数把总配额粗略切分，绝大部分超额请求在进程内就被挡掉，根本不出网
- 定位：单机限流，无法跨实例协同（跨实例需分布式限流如 Redisson RRateLimiter）
- **命名澄清（2026-10-01）**：常被一起讨论的重试库 **Guava Retrying**（`com.github.rholder:guava-retrying:2.0.0`）是第三方扩展，**不是 Guava 核心库的一部分**，详见 [[GuavaRetrying]]

## 关联连接
- [[两级限流]] — 本地粗筛层实现
- [[限流]] — 通用限流概念
- [[Redisson]] — 分布式限流对照
- [[摘要-秒杀系统防刷分层体系]] — 来源
- [[GuavaRetrying]] — 生态中的第三方重试库（非本库组件）
- [[摘要-spring-retry-vs-guava-retry]] — 来源（命名澄清）
