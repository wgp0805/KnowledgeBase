---
title: "摘要-spring-boot-4.1-发布"
type: source
tags: [Spring Boot, 框架升级, gRPC, 安全]
sources: [raw/01-articles/Spring Boot 4.1.0 震撼发布！新特性，惊爆了！.md]
last_updated: 2026-06-26
---

## 核心摘要

2026 年 6 月 10 日 Spring Boot 4.1.0 正式发布，以"更好写、更安全、更好观测"为基调推出多项关键特性：官方 `spring-boot-starter-grpc-server` 让 gRPC 微服务零配置启动；新增 `InetAddressFilter` 给 HTTP 客户端加上 SSRF 防护门；`spring.datasource.connection-fetch=lazy` 实现 JDBC 连接懒借出，事务方法未真正执行 SQL 时不占用连接池；`@RedisListener` 自动配置省去手动注册 `RedisMessageListenerContainer`；OpenTelemetry 上下文自动跨 `@Async` 传播、`/actuator/info` 新增进程信息。升级注意：4.0 已废弃 API 被移除，Apache Derby 集成被废弃，Maven `-DskipTests` 不再跳过 AOT 处理。

## 关联连接

- [[SpringBoot]] — 主体框架，本次升级所属
- [[Spring]] — 底层框架
- [[Redis]] — `@RedisListener` 自动配置目标
- [[microservices]] — gRPC 官方支持服务于微服务通信
- [[Java]] — Kotlin 基线升至 2.3 并支持 Java 25
