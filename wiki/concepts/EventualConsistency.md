---
title: "EventualConsistency"
type: concept
tags: [概念, 分布式系统, 一致性, 架构]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
最终一致性（Eventual Consistency）是一种弱一致性保证：系统在停止更新后，所有副本最终会达到一致状态，但中间可能存在短暂不一致。在事件驱动架构中，[[SpringEvent]] 和 [[MQ]] 适合最终一致性场景——例如提单成功后发 MQ、释放锁等收尾工作，即使失败也应重试至成功。

## 与强一致性对比
- [[StrongConsistency|强一致性]]：要求操作完全一致，失败需回滚
- 最终一致性：允许短暂不一致，通过重试达到一致

## 可靠性保证
1. 订阅者自行重试（[[SpringRetry]] @Retryable）
2. 依赖 [[Kafka]] 消费组重试，可发 [[DeadLetterQueue|死信队列]]
3. 上报故障管理平台，人工介入后重试

## 关联连接
- [[StrongConsistency]] — 对立概念
- [[SpringEvent]] — 适用该一致性的机制
- [[PublishSubscribePattern]] — 适用该一致性的模式
- [[Idempotency]] — 最终一致性 + 重试必须配合幂等
- [[SpringRetry]] — 重试框架
- [[Kafka]] — 消费组重试
- [[DeadLetterQueue]] — 死信队列
- [[重试机制]] — 相关概念
- [[指数退避重试]] — 相关概念
- [[CAP理论]] — 一致性理论框架
