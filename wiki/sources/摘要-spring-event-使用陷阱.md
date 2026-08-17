---
title: "摘要-spring-event-使用陷阱"
type: source
tags: [来源, Spring, 事件机制, 生产实战, 面试]
sources: [raw/01-articles/Spring Event 别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-17
---

## 核心摘要
小哈（犬小哈）总结线上生产环境踩坑经验，梳理 Spring Event 使用的 6 大关键问题。核心观点：Spring Event 是应用内发布订阅机制，适合最终一致性场景，不适合强一致性场景。**生产陷阱**：(1) 优雅关闭——ApplicationContext 关闭期间不得 getBean，否则广播事件报错，必须先切断入口流量（Http/MQ/RPC）再关闭上下文；(2) 启动阶段事件丢失——EventListener 注册滞后于 init-method，Kafka Consumer 在 init-method 阶段发布事件会找不到监听者，应在 Spring 完全启动后（SmartLifecycle/ContextRefreshedEvent）才开启入口流量；(3) 强一致性场景不适合——提单场景库存扣减与订单需完全一致，Spring Event 无法提供"订阅异常→回滚"能力；(4) 最终一致性场景适合——提单成功后的收尾工作（发 MQ、释放锁），失败重试至成功即可；(5) 可靠性保证——三种重试方案：@Retryable 注解、Kafka 消费组重试、故障管理平台；(6) 幂等性——有重试就要有幂等，Spring 不知道哪些订阅者成功/失败，重试时全部执行，订阅逻辑必须幂等。**与 MQ 的关系**：MQ 适合应用间解耦（跨微服务事件广播），Spring Event 适合应用内解耦，两者不矛盾。

## 关键信息
- **优雅关闭**：ApplicationContext 关闭期间不得 getBean，异常信息 `Do not request a bean from a BeanFactory in a destroy method implementation`；必须先切断入口流量再关闭上下文
- **启动阶段事件丢失**：EventListener 注册滞后于 init-method；最佳实践是在 Spring 启动完成后（SmartLifecycle/ContextRefreshedEvent）才开启 Http/MQ/RPC 入口流量
- **强一致性不适合**：提单场景库存扣减与订单需完全一致，Spring Event 无法提供订阅异常→回滚能力
- **最终一致性适合**：提单成功后的收尾工作（发 MQ、释放锁），失败重试至成功即可
- **三种重试方案**：
  1. `@Retryable` 注解（spring-retry 依赖，maxAttempts + backoff 递增间隔）
  2. Kafka 消费组重试（消费失败返回失败，Kafka 自动重试，可配死信队列）
  3. 故障管理平台（超最大重试次数上报故障 MQ，人工排查后点击重试，RPC SPI 调用业务系统重试）
- **幂等性**：Spring 不知道哪些订阅者成功/失败，重试时全部执行所有订阅者，订阅逻辑必须幂等
- **发布订阅模式适用场景**：发布者不关心事件如何处理/处理结果；订阅者多个、可异步可同步、各自独立互不依赖
- **Spring Event vs MQ**：MQ 适合应用间解耦（跨微服务事件广播），Spring Event 适合应用内解耦（小巧轻量），两者不矛盾

## 关联连接
- [[小哈]] — 来源作者
- [[SpringEvent]] — 核心概念
- [[ApplicationEvent]] — Spring 事件机制基础类
- [[Spring]] — 所属框架
- [[观察者模式]] — 底层设计模式
- [[最终一致性]] — 适用业务特性
- [[幂等性]] — 订阅者必备特性
- [[优雅关闭]] — 生产环境前置条件
- [[摘要-理解Spring中的ApplicationListener与ApplicationRunner区别]] — 相关 Spring 事件机制
- [[摘要-springboot-startup-flow]] — Spring Boot 启动流程
- [[摘要-异地多活架构]] — 同作者相关文章
