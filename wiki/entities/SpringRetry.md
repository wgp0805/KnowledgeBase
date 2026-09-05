---
title: "SpringRetry"
type: entity
tags: [Spring, 重试, 框架]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
Spring Retry 是 Spring 提供的重试框架，通过 @Retryable 注解保证方法出现异常时重新执行直至成功。

## 关键信息
- **核心注解**：@Retryable(value=Exception.class, maxAttempts=3, backoff=@Backoff(delay=100L, multiplier=2))
- **参数**：maxAttempts 最大重试次数，backoff 重试间隔（delay 初始延迟，multiplier 递增倍数）
- **依赖**：需引入 spring-retry pom 依赖
- **应用场景**：Spring Event 订阅者自行重试保证成功

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 应用场景
- [[Idempotency]] — 有重试就要有幂等
- [[Spring]] — 所属框架
