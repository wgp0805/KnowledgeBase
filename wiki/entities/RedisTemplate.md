---
title: "RedisTemplate"
type: entity
tags: [Redis, Spring, Java]
sources: []
last_updated: 2026-05-29
---

## 定义
RedisTemplate 是 Spring Data Redis 提供的 Redis 操作模板类，封装了 Redis 的各种数据结构操作（String、Hash、List、Set、ZSet），是 Spring Boot 中操作 Redis 的标准方式。

## 关键信息
- StringRedisTemplate：专门处理 String 类型的简化版
- 序列化器：默认 JDK 序列化（建议改为 JSON 序列化）
- opsForValue() / opsForHash() / opsForList() / opsForSet() / opsForZSet()
- 事务支持：multi/exec/discard
- Pipeline：批量操作减少网络往返
- 发布订阅：convertAndSend() / MessageListener

## 关联连接
- [[Redis]] — 底层存储
- [[SpringDataRedis]] — 所属模块
- [[SpringBoot]] — 整合框架
- [[Redisson]] — 高级分布式数据结构客户端
