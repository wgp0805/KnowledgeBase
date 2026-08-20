---
title: "Redisson"
type: entity
tags: [Redis, 分布式锁, Java, 限流, 秒杀]
sources: [raw/01-articles/秒杀系统怎么区分真实用户和黄牛脚本？.md]
last_updated: 2026-08-20
---

## 定义
Redisson 是一个高级的 Redis Java 客户端，提供了分布式锁（RLock）、分布式集合、分布式对象等丰富的分布式数据结构，是实现分布式锁的首选方案。

## 关键信息
- RLock：可重入分布式锁，基于 Lua 脚本实现原子操作
- 看门狗机制：自动续期，防止业务未完成锁已过期
- RedLock 算法：多节点 Redis 环境下的分布式锁方案
- 与 RedisTemplate 对比：Redisson 封装了分布式数据结构，RedisTemplate 是基础客户端
- 分布式对象：RBucket、RMap、RList、RSet 等

### RRateLimiter 与热点 Key 陷阱
- `RRateLimiter` 是 Redisson 提供的分布式限流器，底层是 Lua 脚本，每次 acquire 走一次 Redis 往返
- **限流器自己就是一个 Redis Key**：秒杀峰值下全站请求都往同一个限流 Key 上打，该 Key 瞬间变成整个集群最热的 [[热点Key]]，把所在节点单独烤糊
- **结果**：为保护系统加的限流，成了第一个倒下的组件
- **正确姿势**：两级限流——本地先限（[[Guava]] RateLimiter 或信号量）粗筛，漏下来的小部分再走 RRateLimiter 精算（参见 [[两级限流]]）

## 关联连接
- [[Redis]] — 底层存储
- [[distributed-lock]] — 分布式锁概念
- [[RedisTemplate]] — Spring Redis 客户端
- [[热点Key]] — RRateLimiter 陷阱
- [[两级限流]] — 正确使用姿势
- [[Guava]] — 本地限流对照
- [[限流]] — 通用限流概念
- [[摘要-秒杀系统防刷分层体系]] — RRateLimiter 陷阱来源
