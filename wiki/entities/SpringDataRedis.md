---
title: "SpringDataRedis"
type: entity
tags: [Redis, Spring, 数据访问]
sources: []
last_updated: 2026-05-29
---

## 定义
Spring Data Redis 是 Spring Data 家族的一部分，提供了对 Redis 的抽象和集成，包括 RedisTemplate 和 Repository 抽象，简化了 Redis 的使用。

## 关键信息
- 核心组件：RedisTemplate、StringRedisTemplate
- 连接工厂：LettuceConnectionFactory（默认）、JedisConnectionFactory
- Lettuce：基于 Netty 的异步 Redis 客户端（Spring Boot 默认）
- Jedis：同步 Redis 客户端（较旧但更简单）
- Repository 抽象：类似 JPA 的 Redis Repository（较少使用）
- 自动配置：spring-boot-starter-data-redis

## 关联连接
- [[Redis]] — 底层存储
- [[RedisTemplate]] — 核心操作类
- [[Jedis]] — Redis 客户端实现
- [[SpringBoot]] — 整合框架
