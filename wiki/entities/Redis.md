---
title: "Redis"
type: entity
tags: [缓存, 键值存储]
sources: [raw/01-articles/springboot整合redis.md, raw/01-articles/Docker部署Redis全攻略：持久化、自定义网络与配置详解.md]
last_updated: 2026-05-19
---

## 定义
Redis 是一个开源的内存数据结构存储系统，用作数据库、缓存和消息代理，支持字符串、哈希、列表、集合、有序集合等多种数据类型。

## 关键信息
- 五大数据类型：String、Hash、List、Set、ZSet（有序集合）
- RedisTemplate 操作 API：ValueOperations、HashOperations、ListOperations、SetOperations、ZSetOperations
- 持久化方式：RDB（快照）和 AOF（追加文件）
- 支持主从复制、哨兵模式、集群模式
- 常见应用：缓存加速、分布式锁、计数器、排行榜

## 关联连接
- [[SpringBoot]] — 与 Spring Boot 整合
- [[Docker]] — Redis 容器化部署
- [[Jedis]] — Java 客户端
- [[SpringDataRedis]] — Spring 封装
