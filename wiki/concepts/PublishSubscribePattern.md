---
title: "PublishSubscribePattern"
type: concept
tags: [概念, 设计模式, 架构, 事件驱动]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
发布订阅模式（Publish-Subscribe Pattern）是一种消息通信模式：发布者不关心事件如何处理和结果，订阅者多个、可异步可同步、各自独立互不依赖。[[SpringEvent]] 是该模式在 Spring 框架内的实现。

## 适用与不适用
- **适用**：发布者不关心处理结果；订阅者独立互不依赖
- **不适用**：[[StrongConsistency|强一致性]]场景（无法提供订阅异常→回滚能力）
- **适用**：[[EventualConsistency|最终一致性]]场景（提单成功后发 MQ、释放锁等收尾工作）

## 关联连接
- [[SpringEvent]] — Spring 实现
- [[ApplicationListener]] — 监听者接口
- [[EventListener]] — 监听注解
- [[EventualConsistency]] — 适用场景
- [[StrongConsistency]] — 不适用场景
- [[观察者模式]] — 相关模式
- [[事件流]] — 相关概念
- [[MQ]] — 应用间解耦的实现
