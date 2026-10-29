---
title: "idempotency"
type: concept
tags: [并发, 安全, 分布式]
sources:
  - raw/09-archive/高并发下如何防止重复下单？.md
  - raw/09-archive/百度面试官：RabbitMQ 如何防止重复消费？5种解决方案，你知道几个？.md
  - raw/09-archive/2026-10-28 - SpringBoot接口幂等性方案：4种策略+代码实战，告别重复提交.md
last_updated: 2026-10-29
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

### 消息消费场景的两种幂等方案

绝大多数消息队列只保证**至少一次投递**，服务重启、网络重试极易产生重复消息，导致重复退款、重复加积分等脏数据。两种方案二选一：

1. **业务幂等（优先推荐）**：所有消费逻辑支持重复执行无副作用（如根据订单号判断是否已处理）
2. **唯一键去重**：数据库记录已处理消息 ID，重复消息直接拦截丢弃

### 关键要点

- 幂等性检查**必须在事务开始前完成**
- Token 有效期应合理设置（通常 5 分钟）
- 使用 Lua 脚本保证 Redis 操作的原子性

### 四种工程方案的横向对照（2026-10 补充）

早期本页记录的是"消息消费场景"的视角；从**接口防重**视角看，可整理的方案有四种，选型判据是"有没有天然唯一业务键"：

| 方案 | 延迟 | 复杂度 | 外部依赖 | 适用场景 |
|------|------|--------|----------|----------|
| Token 令牌（预生成+一次性+原子删除） | 中 | 低 | Redis | 下单、支付 |
| 数据库唯一索引（异常即幂等） | 低 | 低 | 无 | 支付、注册 |
| 分布式锁（lock + requestId 幂等表） | 中 | 中 | Redis / ZK | 抢券、秒杀 |
| 请求内容摘要（MD5/SHA256 + `setIfAbsent`） | 低 | 中 | Redis | 转账、回调 |

补充两个易踩的坑：
- **内容摘要方案必须在业务异常时回删键**，否则失败后的合法重试会被误判为重复请求
- **唯一索引方案要把唯一键异常翻译成"成功响应"**（查已存在记录返回），否则用户会看到一个本不该出现的错误

详见 [[幂等性]] 与 [[摘要-springboot接口幂等性4种策略]]。

## 关联连接
- [[幂等性]] — 幂等性总纲（含 4 方案选型）
- [[摘要-springboot接口幂等性4种策略]] — 四方案代码实战
- [[摘要-prevent-duplicate-order]] — 来源
- [[摘要-rabbitmq-idempotency]] — RabbitMQ 消息幂等方案
- [[摘要-微服务架构-进程间通信]] — 微服务 IPC 中的消息幂等场景
- [[distributed-lock]] — 分布式锁
- [[Redis]] — Token 存储、SETNX 去重
- [[RabbitMQ]] — 消息队列重复消费
- [[duplicate-submit]] — 重复提交问题
- [[异步消息]] — 消息重复消费难题
