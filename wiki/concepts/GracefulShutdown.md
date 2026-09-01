---
title: "GracefulShutdown"
type: concept
tags: [概念, 运维, 可靠性, Spring]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
优雅关闭（Graceful Shutdown）是服务关闭时的有序退出机制。使用 [[SpringEvent]] 前必须先实现优雅关闭：关闭时先切断入口流量（Http/MQ/RPC），再关闭 [[ApplicationContext]]。关键约束——ApplicationContext 关闭期间不得 GetBean（"Do not request a bean from a BeanFactory in a destroy method implementation"），否则报错。

## 关键实践
- 先切断入口流量（Http/MQ/RPC）再关闭上下文
- ApplicationContext 关闭期间不得 GetBean
- 启动阶段对称问题：应在 Spring 启动完成后（[[SmartLifecycle]]/[[ContextRefreshedEvent]]）开启入口流量

## 关联连接
- [[SpringEvent]] — 使用前提
- [[ApplicationContext]] — 关闭期间不得 GetBean
- [[BeanFactory]] — GetBean 的提供者
- [[SmartLifecycle]] — 启动完成后开启入口流量
- [[ContextRefreshedEvent]] — 启动完成事件
- [[HealthCheck]] — 相关概念
- [[降级]] — 相关的可靠性手段
