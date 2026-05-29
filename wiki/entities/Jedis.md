---
title: "Jedis"
type: entity
tags: [Redis, Java, 客户端]
sources: []
last_updated: 2026-05-29
---

## 定义
Jedis 是一个简洁的 Redis Java 客户端，提供同步的 Redis 命令实现，API 与 Redis 命令一一对应，易于理解和使用。

## 关键信息
- 同步阻塞：基于 BIO 模型
- 线程安全：Jedis 实例非线程安全，需使用 JedisPool
- 与 Lettuce 对比：Jedis 同步简单，Lettuce 异步高性能（Spring Boot 默认 Lettuce）
- 使用场景：简单项目、学习阶段

## 关联连接
- [[Redis]] — 底层存储
- [[SpringDataRedis]] — Spring 集成
- [[RedisTemplate]] — Spring 操作模板
