---
title: "EventListener"
type: entity
tags: [Spring, 事件驱动, 注解]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
@EventListener 是 Spring 提供的注解，用于将方法注册为 Spring Event 的监听者，是 ApplicationListener 接口的注解替代方式。

## 关键信息
- **作用**：注解方式注册事件监听者，替代实现 ApplicationListener 接口
- **注册时机**：滞后于 init-method，可能导致服务启动阶段事件丢失
- **使用场景**：在订单消息处理中，可通过 @EventListener 注册对应状态的事件监听器

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 所属机制
- [[ApplicationListener]] — 接口替代方式
- [[ApplicationEvent]] — 监听的事件基类
- [[Spring]] — 所属框架
