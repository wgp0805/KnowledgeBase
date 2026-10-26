---
title: "SpringRetry"
type: entity
tags: [Spring, 重试, 框架]
sources: [raw/09-archive/SpringEvent别瞎用！被它坑的绩效都没了！.md, raw/01-articles/2026-10-01 - 消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思.md]
last_updated: 2026-10-08
---

## 定义
Spring Retry 是 Spring 提供的声明式重试框架，对可能抛出异常的调用操作进行有策略的重试，用于 Spring 批处理、Spring 集成等场景；通过 @Retryable 注解保证方法出现异常时重新执行直至成功。

## 关键信息
- **核心注解**：@Retryable(value=Exception.class, maxAttempts=3, backoff=@Backoff(delay=100L, multiplier=2))
- **参数**：maxAttempts 最大重试次数，backoff 重试间隔（delay 初始延迟，multiplier 递增倍数）
- **依赖**：需引入 spring-retry pom 依赖（注解式还需 aspectjweaver）
- **应用场景**：Spring Event 订阅者自行重试保证成功
- **编程式用法**：RetryTemplate 设 SimpleRetryPolicy（重试次数+按异常 Map 判定）与 FixedBackOffPolicy（间隔），execute 提交 RetryCallback（正常逻辑）与 RecoveryCallback（耗尽/不可重试时的恢复逻辑）
- **内置重试策略**：Never（不重试）/Always（无限重试，慎用防死循环）/Simple（默认 3 次）/Timeout/ExceptionClassifier/CircuitBreaker（带熔断）/Composite（乐观"任一允许即重试"、悲观"任一不允许即重试"）
- **内置退避策略**：NoBackOff（立即重试）/Fixed/UniformRandom（默认 500–1500ms 随机）/Exponential（默认初始 100ms、最大 30s、乘数递增）/ExponentialRandom（随机乘数）
- **注解式三件套**：启动类 @EnableRetry + 方法 @Retryable(value, maxAttempts, backoff) + 兜底 @Recover；只有抛出指定异常才重试，未指定异常或达上限直接回调 @Recover
- **对比 Guava Retrying**：Spring-Retry **只能根据抛出的异常**判断是否重试，[[GuavaRetrying]] 还能按方法返回值重试、更灵活；两者均线程安全、支持超时/次数/间隔/监听

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[摘要-spring-retry-vs-guava-retry]] — 来源（与 Guava-Retry 对比）
- [[GuavaRetrying]] — 对比的更灵活重试库
- [[重试机制]] — 上位概念
- [[指数退避重试]] — Backoff 支持的策略
- [[SpringEvent]] — 应用场景
- [[Idempotency]] — 有重试就要有幂等
- [[Spring]] — 所属框架
