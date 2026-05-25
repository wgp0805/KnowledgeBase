---
title: "ApplicationEvent"
type: entity
tags: [Spring, 事件机制, 观察者模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
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

## 关联连接
- [[Spring]] — 所属框架
- [[观察者模式]] — ApplicationEvent 体现的设计模式
- [[ApplicationContext]] — ApplicationEventPublisher 的实现
- [[摘要-spring-design-patterns]] — 来源文章