---
title: "ContextRefreshedEvent"
type: entity
tags: [Spring, 事件, 启动]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
ContextRefreshedEvent 是 Spring 框架在上下文刷新（启动完成）时发布的事件，建议在此位置注册服务、开启入口流量。

## 关键信息
- **触发时机**：Spring 上下文刷新（启动完成）时
- **最佳实践**：在 ContextRefreshedEvent 或 SmartLifecycle 等位置注册服务、开启入口流量
- **解决问题**：确保 Spring 启动完成后才开启入口流量，避免事件丢失

## 关联连接
- [[摘要-SpringEvent别瞎用]] — 来源
- [[SpringEvent]] — 相关机制
- [[SmartLifecycle]] — 替代位置
- [[ApplicationContext]] — 事件发布者
- [[Spring]] — 所属框架
