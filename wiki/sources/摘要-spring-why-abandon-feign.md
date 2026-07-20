---
title: "摘要-spring-why-abandon-feign"
type: source
tags: [Spring, Feign, HTTP客户端, 技术]
sources: [raw/01-articles/Spring为什么要"抛弃"Feign？.md]
last_updated: 2026-07-20
---

## 核心摘要
Spring Framework 6 推出原生 @HttpExchange 声明式 HTTP 客户端，Spring Boot 4.x 已深度整合并推荐替代 OpenFeign。本文从层级归属（Spring Cloud 生态 vs Spring Framework 核心）、代理机制（JDK 动态代理 vs HttpServiceProxyFactory 适配器模式）、编程模型（仅阻塞 vs 阻塞+响应式双模）、性能实测（吞吐量 +40%、内存 -35%）四个维度全面对比，给出分步迁移建议。

## 关联连接
- [[苏三]] — 本文作者
- [[OpenFeign]] — 被对比的传统方案
- [[Spring]] — 框架生态
- [[RestClient]] — 底层同步客户端
- [[HttpExchange]] — 本文核心概念
- [[SpringBoot]] — Boot 4.x 整合信息
