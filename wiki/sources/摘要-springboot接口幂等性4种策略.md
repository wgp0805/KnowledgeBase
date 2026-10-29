---
title: "摘要-springboot接口幂等性4种策略"
type: source
tags: [来源, 幂等性, SpringBoot, 分布式, Redis]
sources: [raw/09-archive/2026-10-28 - SpringBoot接口幂等性方案：4种策略+代码实战，告别重复提交.md]
last_updated: 2026-10-29
---

## 核心摘要
网络抖动、用户手抖、MQ 重试都可能产生"重复请求"，轻则重复建单，重则重复扣钱。本文把工程上最常用的四种幂等实现一次讲透并配上可复制的代码：① **Token 令牌**（预生成 + 一次性 + Redis 原子删除）；② **数据库唯一索引**（业务唯一键兜底，重复写直接抛异常）；③ **分布式锁**（Redisson `tryLock` + requestId 幂等表双保险）；④ **请求内容摘要**（请求体 MD5/SHA256 作幂等键 + 注解式 AOP 零侵入）。作者的核心结论是：**优先用数据库唯一索引，成本最低；并发量高再上分布式锁或 Token，不要过度设计**。

## 关键信息

### 四种方案对照
| 方案 | 延迟 | 复杂度 | 外部依赖 | 适用场景 |
|------|------|--------|----------|----------|
| Token 令牌 | 中 | 低 | Redis | 有预生成环节：下单、支付 |
| 数据库唯一索引 | 低 | 低 | 无 | 支付、注册 |
| 分布式锁 | 中 | 中 | Redis / ZK | 高并发抢券、秒杀 |
| 请求内容摘要 | 低 | 中 | Redis | 无预生成：转账、回调 |

### ① Token 令牌：最经典、最稳
- **思路**：先拿令牌 → 再执行业务 → 用完即焚
- **核心关键字**：预生成、一次性、Redis 原子删除
- 实现：`GET /token` 用 `UUID.randomUUID()` 生成并写入 `tk:{token}`，TTL 10 分钟；下单接口从 Header 读 `Idempotent-Token`，用 `redis.delete(key)` 的返回值判断是否首次使用
- 要点：UUID 保证全局唯一，Redis TTL 防呆；`delete` 是原子操作，天然并发安全；用 Header 传令牌保持接口语义纯净

### ② 数据库唯一索引：低成本、强一致
- **思路**：把"业务唯一键"做成唯一索引，重复写直接抛异常
- **核心关键字**：天然幂等、异常即幂等
- 实现：JPA `@UniqueConstraint(columnNames = "transaction_id")`，`repo.save()` 命中重复时抛 `DataIntegrityViolationException`，catch 后改为 `findByTxId` 查询返回"已支付"
- 要点：唯一索引兜底，数据库层面 100% 防重；try-catch 把异常转成正常响应，用户体验丝滑；无外部依赖，**老旧系统也毫无压力**

### ③ 分布式锁：高并发大杀器
- **思路**：对"订单号 / 用户ID"加锁，抢到锁再干活
- **核心关键字**：互斥、超时、可重入
- 实现：Redisson `lock.tryLock(3, 5, TimeUnit.SECONDS)`（最多等 3 秒、持锁 5 秒自动释放）；拿到锁后**先做业务幂等检查**（`repo.existsByRequestId`），再真正扣库存
- 要点：Redisson 自带 watchdog 自动续期，不怕死锁；`requestId` 做幂等表实现"锁 + 唯一索引"双保险；`lock.isHeldByCurrentThread()` 防止误删别人的锁

### ④ 请求内容摘要：最透明、最通用
- **思路**：把请求体做 MD5/SHA256，作为幂等键
- **核心关键字**：零额外交互、客户端无感
- 实现：自定义 `@Idempotent(expire = 3600)` 注解 + `@Around` 切面；读取请求体算 `DigestUtils.md5DigestAsHex`，用 `setIfAbsent(key, "1", TTL)` 抢占；抢不到返回"重复请求"，业务抛异常时 `redis.delete(key)` 释放允许重试
- 要点：MD5 把任意长度报文压成 32 位，冲突概率极低；`setIfAbsent` 保证原子性，**异常回删避免误杀**；注解 + AOP 零侵入，老接口 1 行注解即可拥有幂等

### 实施清单
1. 检查核心接口**有没有唯一业务键**——有唯一键就不必上重型方案
2. **优先使用数据库唯一索引**，成本最低
3. 并发量高再上分布式锁或 Token，**不要过度设计**
4. 给关键接口加上监控告警，幂等失败时第一时间知道

## 关联连接
- [[幂等性]] — 幂等性总纲（已收录本文的四方案对照）
- [[幂等性设计]] — 接口层设计实践
- [[idempotency]] — 早期英文页（Token / 唯一标识 / AOP 三方案）
- [[duplicate-submit]] — 重复提交问题
- [[分布式锁]] — 方案三的机制基础
- [[Redisson]] — `tryLock` 与 watchdog 的实现载体
- [[Redis]] — Token 与摘要键的存储
- [[SpringBoot]] — 实现载体
- [[AOP]] — 摘要方案零侵入的实现方式
- [[摘要-prevent-duplicate-order]] — 同主题（高并发防止重复下单）
- [[重复消费解决方案]] — 消息场景下的同源问题
