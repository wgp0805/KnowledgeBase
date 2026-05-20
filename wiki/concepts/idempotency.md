---
title: "idempotency"
type: concept
tags: [并发, 安全, 分布式]
sources: [raw/01-articles/高并发下如何防止重复下单？.md]
last_updated: 2026-05-20
---

## 定义

幂等性（Idempotency）是指同一个操作执行多次的结果与执行一次的结果相同。在分布式系统中，幂等性是解决重复提交、网络重试等问题的核心设计理念。

## 核心原理

### 幂等 vs 非幂等

- **幂等**：调用 1 次或 N 次，结果相同（如只创建一个订单）
- **非幂等**：调用 N 次可能产生 N 个不同结果

### 实现方案

#### 1. Token 方案（推荐）

```java
// 1. 客户端提交前先申请唯一 Token
// 2. 提交时携带 Token
// 3. 服务端用 Lua 脚本原子性检查并消费 Token
String luaScript = """
    if redis.call('get', KEYS[1]) == '1' then
        redis.call('del', KEYS[1])
        return 1
    else
        return 0
    end
    """;
```

#### 2. 业务唯一标识方案

利用业务的自然唯一性（如 userId + productId + submitTime），通过数据库唯一约束实现幂等。

#### 3. AOP 注解方案

```java
@Idempotent(key = "#request.userId + ':' + #request.submitToken", expireTime = 300)
public ApiResponse submitOrder(@RequestBody OrderSubmitRequest request) { ... }
```

### 关键要点

- 幂等性检查**必须在事务开始前完成**
- Token 有效期应合理设置（通常 5 分钟）
- 使用 Lua 脚本保证 Redis 操作的原子性

## 关联连接
- [[摘要-prevent-duplicate-order]] — 来源
- [[distributed-lock]] — 分布式锁
- [[Redis]] — Token 存储
- [[duplicate-submit]] — 重复提交问题
