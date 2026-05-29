---
title: "SpringCloudGateway"
type: entity
tags: [SpringCloud, 网关, 微服务]
sources: []
last_updated: 2026-05-29
---

## 定义
Spring Cloud Gateway 是 Spring Cloud 生态中的 API 网关组件，基于 Spring WebFlux 和 Reactor 构建，提供路由转发、负载均衡、限流、鉴权等横切关注点。

## 关键信息
- 基于 WebFlux：响应式、非阻塞、高性能
- 核心概念：Route（路由）、Predicate（断言）、Filter（过滤器）
- 限流：支持 RequestRateLimiter（基于 Redis + 令牌桶）
- 集成服务发现：与 Nacos、Eureka 等注册中心集成
- 替代 Zuul：Spring Cloud 官方推荐的网关方案
- 全局过滤器：GlobalFilter 处理跨切面逻辑（鉴权、日志等）

## 关联连接
- [[Nacos]] — 服务注册与发现
- [[SpringBoot]] — 基础框架
- [[microservices]] — 微服务架构
- [[Sentinel]] — 限流熔断配合使用
