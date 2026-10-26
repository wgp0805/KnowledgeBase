---
title: "摘要-spring-retry-vs-guava-retry"
type: source
tags: [来源, 原始文件, Java, Spring, 重试框架]
sources: [raw/09-archive/2026-10-01 - 消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思.md]
last_updated: 2026-10-08
---

## 核心摘要
对比两个线程安全的 Java 重试框架。Spring Retry 提供声明式重试：编程式用 RetryTemplate（配 SimpleRetryPolicy 重试次数 + FixedBackOffPolicy 间隔 + RetryCallback/RecoveryCallback），注解式用 @EnableRetry + @Retryable(value, maxAttempts, backoff=@Backoff(delay, multiplier)) + @Recover 兜底，内置 Never/Always/Simple/Timeout/ExceptionClassifier/CircuitBreaker/Composite 等重试策略与 NoBackOff/Fixed/UniformRandom/Exponential/ExponentialRandom 等退避策略；但只能根据抛出的异常判断是否重试。Guava Retryer（guava-retrying，com.github.rholder）通过 RetryerBuilder 构建，除异常源（retryIfException/OfExceptionOfType/RuntimeException）外还支持按返回值重试（retryIfResult，如返回 false 或匹配正则），并可配 WaitStrategies/StopStrategies/RetryListener 监听。结论：两者都把正常逻辑与重试解耦、可设超时/次数/间隔，Guava-Retry 更灵活便捷（能按返回值重试），Spring-Retry 只能按异常重试。

## 关联连接
- [[SpringRetry]] — Spring 声明式重试框架
- [[GuavaRetrying]] — Guava 生态的灵活重试库
- [[重试机制]] — 上位概念
- [[指数退避重试]] — 两框架均支持的退避策略
