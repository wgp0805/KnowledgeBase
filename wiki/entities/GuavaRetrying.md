---
title: "GuavaRetrying"
type: entity
tags: [实体, Java, 重试框架, Guava生态]
sources: [raw/01-articles/2026-10-01 - 消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思.md]
last_updated: 2026-10-08
---

## 定义
Guava Retryer（依赖 `com.github.rholder:guava-retrying:2.0.0`，第三方扩展而非 Google 官方 [[Guava]] 核心库）是线程安全的 Java 重试框架，通过 RetryerBuilder 构建重试者包装正常逻辑，与 [[SpringRetry]] 相比支持更灵活的重试源定义——尤其能**按方法返回值**判断是否重试。

## 关键信息
- **构建方式**：`RetryerBuilder.<Boolean>newBuilder()` 链式配置，入口用 `java.util.concurrent.Callable` 的 call 方法
- **重试源（可叠加多个）**：`retryIfException`（runtime+checked 异常重试，error 不重试）、`retryIfRuntimeException`、`retryIfExceptionOfType(Xxx.class)`（仅特定异常）、`retryIfResult(res -> res==false)`（按返回值/正则/空值重试）
- **等待与停止策略**：`withWaitStrategy(WaitStrategies.fixedWait(3, TimeUnit.SECONDS))`、`withStopStrategy(StopStrategies.stopAfterAttempt(3))`
- **监听**：`withRetryListener(RetryListener)` 每次重试后回调（如记录第 N 次失败），可注册多个按顺序调用
- **对比 SpringRetry**：Guava 更便捷灵活（能按返回值重试），Spring-Retry 只能根据抛出的异常判断；两者都将正常方法与重试方法解耦、支持超时/次数/间隔设置
- **与 [[重试机制]] 的关系**：两者都是并发场景下可靠性兜底的实现，重试仍需操作具备幂等性

## 关联连接
- [[摘要-spring-retry-vs-guava-retry]] — 来源
- [[SpringRetry]] — 对比的 Spring 重试框架
- [[Guava]] — 生态归属（注意非其核心库）
- [[重试机制]] — 上位概念
- [[指数退避重试]] — 可选的退避策略
