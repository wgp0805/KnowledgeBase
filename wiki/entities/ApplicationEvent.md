---
title: "ApplicationEvent"
type: entity
tags: [Spring, 事件机制, 观察者模式]
sources:
  - raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md
  - raw/01-articles/Spring Event 别瞎用！被它坑的绩效都没了！.md
last_updated: 2026-08-17
---

## 定义
ApplicationEvent 是 Spring 事件机制的基础类，用于定义应用程序事件。通过观察者模式实现事件发布与监听的解耦。

## 关键信息
- 观察者模式：一个事件发布者，多个事件监听者
- 事件定义：继承 ApplicationEvent 类，定义事件属性
- 事件发布：通过 ApplicationEventPublisher.publishEvent() 发布
- 事件监听：使用 @EventListener 注解监听事件
- 解耦优势：发布者和监听者互不依赖，新增功能只需添加监听器
- 典型应用：订单创建后发邮件、送积分、更新库存等场景

### 生产环境陷阱（小哈线上踩坑总结，详见 [[摘要-spring-event-使用陷阱]]）
- **优雅关闭**：ApplicationContext 关闭期间不得 getBean，否则广播事件报错；必须先切断入口流量再关闭上下文
- **启动阶段事件丢失**：EventListener 注册滞后于 init-method；应在 Spring 完全启动后才开启入口流量
- **强一致性不适合**：无法提供"订阅异常→回滚"能力
- **最终一致性适合**：失败重试至成功即可
- **三种重试方案**：`@Retryable` 注解、Kafka 消费组重试、故障管理平台
- **幂等性**：重试时全部执行所有订阅者，订阅逻辑必须幂等

## 关联连接
- [[Spring]] — 所属框架
- [[观察者模式]] — ApplicationEvent 体现的设计模式
- [[ApplicationContext]] — ApplicationEventPublisher 的实现
- [[SpringEvent]] — Spring Event 概念与生产实践
- [[摘要-spring-design-patterns]] — 来源文章
- [[摘要-spring-event-使用陷阱]] — 来源（生产环境踩坑总结）
- [[摘要-理解Spring中的ApplicationListener与ApplicationRunner区别]] — 对比 Spring 中 ApplicationListene…
