---
title: "Eureka"
type: entity
tags: [微服务, 注册中心]
sources: [raw/09-archive/为什么越来越多人用Nacos？.md]
last_updated: 2026-08-05
---

## 定义
Eureka 是 Spring Cloud Netflix 生态中的服务注册中心，基于 Netflix 开源技术，遵循 AP 原则（可用性优先），只提供服务注册与发现能力，配置能力需额外组件。

## 关键信息
- **一致性**：AP 模式
- **功能边界**：仅注册中心，无原生配置中心能力，无控制台
- **维护状态**：Eureka 2.x 已停止维护，1.x 版本发展缓慢——选择 Eureka 需提前考虑迁移方案
- **对比定位**：与 Nacos 相比功能单一，是"越来越多人转向 Nacos"的背景原因之一

## 关联连接
- [[Nacos]] — 主要替代者
- [[摘要-为什么越来越多人用Nacos]] — 来源
- [[microservices]] — 微服务架构上下文
- [[SpringCloudAlibaba]] — 取代 Spring Cloud Netflix 的生态
