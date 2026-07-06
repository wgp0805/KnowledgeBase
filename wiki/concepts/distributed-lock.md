---
title: "distributed-lock"
type: concept
tags: [并发, 分布式, Redis]
sources: [raw/01-articles/高并发下如何防止重复下单？.md, raw/01-articles/2026-07-05-AI Agent 30天速成｜Day10 笔记 - 云淡风轻YangG.md]
last_updated: 2026-07-06
---

## 定义

分布式锁是在分布式环境下，控制多个实例对共享资源进行互斥访问的机制。它保证在同一时刻，只有一个实例能执行临界区代码。

## 核心原理

### 基于 Redis 的分布式锁（Redisson）

```java
RLock lock = redissonClient.getLock(lockKey);
try {
    boolean acquired = lock.tryLock(waitTime, leaseTime, TimeUnit.MILLISECONDS);
    if (acquired) {
        // 执行业务逻辑
    }
} finally {
    if (lock.isHeldByCurrentThread()) {
        lock.unlock();
    }
}
```

### 使用注意事项

| 要点 | 说明 |
|------|------|
| 锁粒度 | 不要太粗（影响性能）也不要太细（增加复杂度） |
| 锁超时 | 必须设置合理的超时时间，防止死锁 |
| 锁续期 | 对于长时间操作，需要实现锁续期机制（WatchDog） |
| 可重入性 | 同一个线程可以重复获取锁 |
| 容错性 | Redis 集群故障时要有降级方案 |

### 订单提交场景

```java
// 锁的 key 包含 userId 和 submitToken，保证同一提交只有一个线程处理
String lockKey = String.format("order:submit:lock:%s:%s", userId, submitToken);
RLock lock = tryLock(lockKey, 100, 5000); // 等待 100ms，锁持有 5s
```

### Agent 会话锁场景
多实例 Agent 部署时，同一用户并发对话导致 Redis 会话消息错乱。基于 Redis SETNX 实现会话互斥锁：
```
SETNX agent:session:lock:{sessionId} "locked" EX 30
```
- 单会话同一时间仅允许一条对话执行
- 锁过期时间 30s，对话结束主动释放锁
- 同会话新请求检测锁存在直接返回"对话处理中"

## 关联连接
- [[摘要-prevent-duplicate-order]] — 来源
- [[idempotency]] — 幂等性
- [[Redis]] — Redisson 底层依赖
- [[Redisson]] — Redis 分布式锁实现
- [[摘要-ai-agent-day10-tool-pipeline]] — 来源
