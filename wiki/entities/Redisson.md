---
title: "Redisson"
type: entity
tags: [Redis, 分布式锁, Java]
sources: []
last_updated: 2026-05-29
---

## 定义
Redisson 是一个高级的 Redis Java 客户端，提供了分布式锁（RLock）、分布式集合、分布式对象等丰富的分布式数据结构，是实现分布式锁的首选方案。

## 关键信息
- RLock：可重入分布式锁，基于 Lua 脚本实现原子操作
- 看门狗机制：自动续期，防止业务未完成锁已过期
- RedLock 算法：多节点 Redis 环境下的分布式锁方案
- 与 RedisTemplate 对比：Redisson 封装了分布式数据结构，RedisTemplate 是基础客户端
- 分布式对象：RBucket、RMap、RList、RSet 等

## 关联连接
- [[Redis]] — 底层存储
- [[distributed-lock]] — 分布式锁概念
- [[RedisTemplate]] — Spring Redis 客户端
