---
title: "Resilience4j"
type: entity
tags: [熔断, 微服务, Java, 函数式编程]
sources: [raw/09-archive/携程二面：什么是熔断？你之前项目怎么处理的？.md]
last_updated: 2026-08-05
---

## 定义
Resilience4j 是社区维护的轻量级熔断降级框架，基于 Java 8 函数式编程风格，是 Hystrix 推荐的替代品。

## 关键信息
- **特点**：基于 Java 8 函数式编程，轻量级
- **现状**：活跃维护中
- **定位**：Hystrix 推荐替代品，Spring Boot 友好
- 选型建议：新项目可在 Sentinel（功能全、控制台好用、社区活跃）与 Resilience4j（轻量、函数式风格、Spring Boot 友好）之间选择

## 关联连接
- [[Hystrix]] — 被替代的老牌框架
- [[熔断]] — 核心能力
- [[Sentinel]] — 功能更全的竞品
- [[摘要-携程二面-熔断]] — 框架对比来源