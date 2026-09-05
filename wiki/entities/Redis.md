---
title: "Redis"
type: entity
tags: [缓存, 键值存储, 秒杀]
sources: [raw/09-archive/springboot整合redis.md, raw/09-archive/Docker部署Redis全攻略：持久化、自定义网络与配置详解.md, raw/09-archive/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md, raw/09-archive/高并发下如何防止重复下单？.md, raw/01-articles/秒杀系统怎么区分真实用户和黄牛脚本？.md]
last_updated: 2026-08-20
---

## 定义
Redis 是一个开源的内存数据结构存储系统，用作数据库、缓存和消息代理，支持字符串、哈希、列表、集合、有序集合等多种数据类型。

## 关键信息
- 五大数据类型：String、Hash、List、Set、ZSet（有序集合）
- RedisTemplate 操作 API：ValueOperations、HashOperations、ListOperations、SetOperations、ZSetOperations
- 持久化方式：RDB（快照）和 AOF（追加文件）
- 支持主从复制、哨兵模式、集群模式
- 常见应用：缓存加速、分布式锁、计数器、排行榜

### Token 存储应用
- **Token 黑名单**：存储已失效的 JWT Token，TTL 与 Token 过期时间对齐
- **RefreshToken 存储**：存储长期有效的 RefreshToken，支持主动吊销
- **高可用方案**：Sentinel（哨兵模式）或 Cluster（集群模式）
- **性能**：单次查询 < 1ms，单机 QPS 十几万

### 幂等性与分布式锁
- **幂等性 Token**：存储提交 Token，使用 Lua 脚本保证原子性检查和消费
- **分布式锁**：通过 Redisson 实现分布式锁，支持锁超时、续期、可重入
- **锁粒度设计**：按 userId + submitToken 维度加锁，避免锁竞争

### 秒杀防刷场景
- **前端校验串存储**：预检接口生成随机串 + 时间戳标记位，存 30 秒，前端同算法计算后回传比对（参见 [[前端校验串]]）
- **GETDEL 原子操作（Redis 6.2+）**：取值和删除在一个原子操作里完成，用于校验串"取出即失效"防 [[重放攻击]]。读和删之间没有任何其他客户端能插进来
- **Lua 脚本保证原子性（Redis 6.2 以下）**：`GET` + `DEL` 用 Lua 脚本封装，禁止拆成两条独立命令（高并发下两步之间是竞态窗口）
- **热点 Key 风险**：秒杀峰值下全站请求集中打向少数 Key，会形成 [[热点Key]] 烤糊所在节点（如 Redisson RRateLimiter 限流器 Key）

## 关联连接
- [[SpringBoot]] — 与 Spring Boot 整合
- [[Docker]] — Redis 容器化部署
- [[JWT]] — Token 存储场景
- [[token-blacklist]] — Token 黑名单机制
- [[dual-token-mechanism]] — 双 Token 续期
- [[idempotency]] — 幂等性实现
- [[distributed-lock]] — 分布式锁实现
- [[前端校验串]] — 秒杀防刷第 1 层
- [[重放攻击]] — GETDEL 防御目标
- [[热点Key]] — 秒杀峰值风险
- [[Redisson]] — 高级 Java 客户端
- [[摘要-token-redis-interview]] — Redis 存 Token 分析
- [[摘要-springboot4-security7-vue3-best-practice]] — 工程实践
- [[摘要-prevent-duplicate-order]] — 高并发防重复下单
- [[摘要-秒杀系统防刷分层体系]] — 秒杀防刷场景来源
