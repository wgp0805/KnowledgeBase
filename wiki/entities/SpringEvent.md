---
title: "SpringEvent"
type: entity
tags: [Spring, 事件驱动, 发布订阅]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
Spring Event 是 Spring 框架提供的基于事件的发布订阅机制，开发者可自定义事件、发布事件，Spring 将事件广播给监听该事件的监听者。

## 关键信息
- **机制**：开发者自定义事件并发布，Spring 在 ApplicationContext 中查找所有监听者广播事件
- **注册方式**：实现 ApplicationListener 接口，或使用 @EventListener 注解
- **生产使用六大要点**：
  1. 必须先实现优雅关闭服务（ApplicationContext 关闭期间不得 GetBean）
  2. 服务启动阶段事件丢失（init-method 早于 EventListener 注册）
  3. 强一致性场景不适合（无法提供订阅异常→回滚）
  4. 最终一致性场景适合（提单成功后收尾工作）
  5. 必须有额外可靠性保证（@Retryable/Kafka 重试/故障管理平台）
  6. 订阅者务必保证幂等（重试时全部执行所有订阅者）
- **适用场景**：应用内订阅发布，业务逻辑解耦
- **不适用场景**：应用间解耦（用 MQ）、强一致性事务（无法回滚）
- **vs MQ**：MQ 更强大更重，适合应用间；Spring Event 小巧，适合应用内

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[ApplicationListener]] — 监听者接口
- [[ApplicationEvent]] — 事件基类
- [[EventListener]] — 监听注解
- [[ApplicationContext]] — 上下文，关闭期间不得 GetBean
- [[SmartLifecycle]] — 建议在此开启入口流量
- [[ContextRefreshedEvent]] — Spring 启动完成事件
- [[SpringRetry]] — @Retryable 重试框架
- [[PublishSubscribePattern]] — 发布订阅模式
- [[EventualConsistency]] — 适用场景
- [[StrongConsistency]] — 不适用场景
- [[Idempotency]] — 订阅者必须保证
- [[GracefulShutdown]] — 使用前提
- [[Kafka]] — 消费组重试对比
- [[MQ]] — 对比方案
- [[胖虎]] — 踩坑经验分享者
- [[Spring]] — 所属框架
