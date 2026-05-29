---
title: "Sentinel"
type: entity
tags: [微服务, 限流, 熔断, 阿里巴巴]
sources: []
last_updated: 2026-05-29
---

## 定义
Sentinel 是阿里巴巴开源的分布式流量治理组件，提供流量控制、熔断降级、系统负载保护等功能，是微服务架构中保障服务稳定性的核心组件。

## 关键信息
- 流量控制：QPS 模式、线程数模式、关联模式、链路模式
- 熔断降级：慢调用比例、异常比例、异常数三种策略
- 热点参数限流：针对特定参数值限流
- 集群限流：多实例统一限流
- Dashboard：可视化监控和规则配置
- 与 Hystrix 对比：Sentinel 功能更丰富、持续维护

## 关联连接
- [[microservices]] — 微服务架构
- [[SpringCloudGateway]] — 网关限流
- [[Nacos]] — 规则数据源
