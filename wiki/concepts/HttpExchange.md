---
title: "HttpExchange"
type: concept
tags: [Spring, HTTP客户端, 声明式调用]
sources: [raw/01-articles/Spring为什么要"抛弃"Feign？.md]
last_updated: 2026-07-20
---

## 定义
Spring Framework 6 推出的原生声明式 HTTP 客户端方案，核心注解为 @HttpExchange，配合 @GetExchange/@PostExchange/@PutExchange/@DeleteExchange 等 HTTP 方法注解。基于适配器模式设计，底层可切换 RestClient（同步阻塞）或 WebClient（异步响应式）。Spring Boot 4.x 已深度整合，官方推荐替代 OpenFeign。

## 关键信息
- **层级归属**：Spring Framework 核心功能，不依赖 Spring Cloud
- **代理机制**：通过 HttpServiceProxyFactory 创建代理实例，返回值类型自动选择执行策略（CompletableFuture/Mono/Flux → WebClient 异步，普通类型 → RestClient 同步）
- **性能**：1000 并发实测，吞吐量比 OpenFeign 高约 40%，内存消耗减少约 35%
- **负载均衡**：Spring Cloud 2026.0 已提供 @HttpExchange 的负载均衡支持
- **配置演进**：Spring Framework 7 将引入 @ImportHttpServices 简化 HttpServiceProxyFactory 手动配置

## 关联连接
- [[摘要-spring-why-abandon-feign]] — 来源
- [[OpenFeign]] — 被对比的传统方案
- [[RestClient]] — 底层同步客户端
- [[Spring]] — 所属框架
- [[SpringBoot]] — Boot 4.x 整合
