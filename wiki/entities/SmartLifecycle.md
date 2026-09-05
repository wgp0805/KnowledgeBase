---
title: "SmartLifecycle"
type: entity
tags: [Spring, 生命周期, 接口]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
SmartLifecycle 是 Spring 框架的生命周期接口，建议在此位置注册服务、开启入口流量，以避免服务启动阶段 Spring Event 事件丢失。

## 关键信息
- **作用**：Spring 生命周期接口，用于在 Spring 启动完成后执行逻辑
- **最佳实践**：在 SmartLifecycle 或 ContextRefreshedEvent 等位置注册服务、开启入口流量（Http/MQ/RPC）
- **解决问题**：避免 Kafka consumer init-method 阶段开始消费但 EventListener 未注册导致事件丢失

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 相关机制
- [[ContextRefreshedEvent]] — 替代位置
- [[ApplicationContext]] — 生命周期所属
- [[Spring]] — 所属框架
- [[SpringBoot]] — 启动完成后开启 Http 流量的启示来源
