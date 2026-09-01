---
title: "摘要-SpringEvent别瞎用"
type: source
tags: [来源, Spring, 事件驱动, 可靠性, 踩坑]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 核心摘要
胖虎（Java 专栏）总结公司线上生产环境踩坑后使用 Spring Event 的关键经验。Spring Event 实现基于事件的发布订阅机制，但生产使用有六大要点：①必须先实现优雅关闭服务（ApplicationContext 关闭期间不得 GetBean，否则报错），切断入口流量再关闭上下文；②服务启动阶段事件丢失问题（Kafka consumer init-method 早于 EventListener 注册），应在 Spring 启动完成后（SmartLifecycle/ContextRefreshedEvent）开启入口流量；③强一致性场景不适合发布订阅（无法提供订阅异常→回滚能力）；④最终一致性场景适合（提单成功后发 MQ、释放锁等收尾工作）；⑤必须有额外可靠性保证（订阅者自行重试 @Retryable、依赖 Kafka 消费组重试、上报故障管理平台）；⑥订阅者务必保证幂等（Spring 不知道哪些成功哪些失败，重试时全部执行）。Spring Event 适合应用内订阅发布，MQ 适合应用间解耦，两者不矛盾。

## 关键信息
- **优雅关闭**：ApplicationContext 关闭期间不得 GetBean（Do not request a bean from a BeanFactory in a destroy method implementation）；使用 SpringEvent 前必须先治理服务，关闭时先切断入口流量（Http/MQ/RPC）再关闭上下文
- **启动阶段事件丢失**：Kafka consumer init-method 阶段开始消费，但 EventListener 注册滞后，导致消息处理丢失；最佳实践是在 Spring 启动完成后开启入口流量
- **发布订阅适用场景**：发布者不关心事件如何处理和结果；订阅者多个、可异步可同步、各自独立互不依赖
- **强一致性不适合**：提单场景库存扣减与订单提单必须完全一致，Spring Event 无法提供订阅异常→回滚能力
- **最终一致性适合**：提单成功后发 MQ、释放锁等收尾工作，即使失败也应重试至成功
- **可靠性保证三方案**：
  1. 订阅者自行重试：@Retryable(value=Exception.class, maxAttempts=3, backoff=@Backoff(delay=100L, multiplier=2))
  2. 依赖 Kafka 消费组重试：消费异常返回失败，Kafka 自动重试；可发死信队列
  3. 上报故障管理平台：超最大重试次数上报故障 MQ，故障管理平台消费落库，研发介入后点击重试
- **幂等性**：有重试就要有幂等；Spring 不知道哪些订阅者成功/失败，重试时全部执行，订阅逻辑必须幂等
- **Spring Event vs MQ**：MQ 更强大更重，适合应用间解耦/隔离/事件通知；Spring Event 小巧，适合应用内订阅发布

## 关联连接
- [[SpringEvent]] — 本文核心，Spring 事件发布订阅机制
- [[ApplicationListener]] — Spring 事件监听者接口
- [[ApplicationEvent]] — Spring 事件基类
- [[ApplicationContext]] — Spring 上下文，关闭期间不得 GetBean
- [[EventListener]] — Spring 事件监听注解
- [[SmartLifecycle]] — Spring 生命周期接口，建议在此开启入口流量
- [[ContextRefreshedEvent]] — Spring 启动完成事件
- [[SpringRetry]] — Spring 重试框架，@Retryable 注解
- [[PublishSubscribePattern]] — 发布订阅模式
- [[EventualConsistency]] — 最终一致性，Spring Event 适用场景
- [[StrongConsistency]] — 强一致性，Spring Event 不适用场景
- [[Idempotency]] — 幂等性，订阅者必须保证
- [[GracefulShutdown]] — 优雅关闭，使用 Spring Event 前提
- [[Kafka]] — 消费组重试与死信队列
- [[DeadLetterQueue]] — 死信队列
- [[MQ]] — 消息队列，与 Spring Event 对比
- [[胖虎]] — 本文作者
- [[Spring]] — Spring 框架
- [[SpringBoot]] — Spring Boot，启动完成后开启 Http 流量的启示来源
