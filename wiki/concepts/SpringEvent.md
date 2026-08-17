---
title: "SpringEvent"
type: concept
tags: [Spring, 事件机制, 发布订阅, 最终一致性]
sources: [raw/01-articles/Spring Event 别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-17
---

## 定义
Spring Event 是 Spring 框架提供的基于事件的发布订阅机制，通过 [[ApplicationEvent]] 基类、`ApplicationEventPublisher.publishEvent()` 和 `@EventListener` 注解实现事件发布与监听的解耦。属于应用内发布订阅模式，适合最终一致性场景，不适合强一致性场景。与 MQ 互补：MQ 适合应用间跨微服务解耦，Spring Event 适合应用内解耦。

## 关键信息

### 核心机制
- **事件定义**：继承 [[ApplicationEvent]] 类，定义事件属性
- **事件发布**：`applicationContext.publishEvent(event)`，Spring 按顺序执行订阅者
- **事件监听**：`@EventListener` 注解或实现 `ApplicationListener` 接口
- **设计模式**：[[观察者模式]]，发布者和监听者互不依赖

### 生产环境六大陷阱（小哈线上踩坑总结，详见 [[摘要-spring-event-使用陷阱]]）
1. **优雅关闭**：ApplicationContext 关闭期间不得 getBean，否则广播事件报错；必须先切断入口流量（Http/MQ/RPC）再关闭上下文
2. **启动阶段事件丢失**：EventListener 注册滞后于 init-method；应在 Spring 完全启动后（SmartLifecycle/ContextRefreshedEvent）才开启入口流量
3. **强一致性不适合**：提单场景库存扣减与订单需完全一致，Spring Event 无法提供"订阅异常→回滚"能力
4. **最终一致性适合**：提单成功后的收尾工作（发 MQ、释放锁），失败重试至成功即可
5. **可靠性保证**：三种重试方案——`@Retryable` 注解、Kafka 消费组重试、故障管理平台
6. **幂等性**：有重试就要有幂等，Spring 不知道哪些订阅者成功/失败，重试时全部执行，订阅逻辑必须幂等

### 适用场景判断
- **适合**：发布者不关心事件如何处理/处理结果；订阅者多个、可异步可同步、各自独立互不依赖；最终一致性场景
- **不适合**：强一致性场景（如提单的库存扣减+订单创建需原子性）

### 三种重试方案
1. **`@Retryable` 注解**：spring-retry 依赖，`maxAttempts` + `backoff` 递增间隔
2. **Kafka 消费组重试**：消费失败返回失败，Kafka 自动重试，可配死信队列
3. **故障管理平台**：超最大重试次数上报故障 MQ，人工排查后点击重试，RPC SPI 调用业务系统重试

### Spring Event vs MQ
| 维度 | Spring Event | MQ |
|------|--------------|-----|
| 适用范围 | 应用内 | 应用间（跨微服务） |
| 复杂度 | 轻量小巧 | 强大但更重 |
| 场景 | 业务逻辑解耦 | 微服务事件广播 |
| 关系 | 互补，不矛盾 | 互补，不矛盾 |

## 关联连接
- [[ApplicationEvent]] — Spring 事件机制基础类
- [[Spring]] — 所属框架
- [[观察者模式]] — 底层设计模式
- [[最终一致性]] — 适用业务特性
- [[幂等性]] — 订阅者必备特性
- [[优雅关闭]] — 生产环境前置条件
- [[摘要-spring-event-使用陷阱]] — 来源
- [[摘要-理解Spring中的ApplicationListener与ApplicationRunner区别]] — 相关 Spring 事件机制
- [[小哈]] — 来源作者
