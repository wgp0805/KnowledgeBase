---
title: "ApplicationListener"
type: entity
tags: [Spring, 事件驱动, 接口]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
ApplicationListener 是 Spring 框架提供的事件监听者接口，实现该接口可注册为 Spring Event 的监听者。

## 关键信息
- **作用**：注册为 Spring Event 的监听者，接收 Spring 广播的事件
- **替代方式**：也可使用 @EventListener 注解注册
- **注册时机**：滞后于 init-method，可能导致服务启动阶段事件丢失

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 所属机制
- [[EventListener]] — 注解替代方式
- [[ApplicationEvent]] — 监听的事件基类
- [[ApplicationContext]] — 查找监听者的上下文
- [[Spring]] — 所属框架
