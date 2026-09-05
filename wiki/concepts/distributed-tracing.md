---
title: "distributed-tracing"
type: concept
tags: [可观测性, APM, 分布式, 架构]
sources: [raw/01-articles/2026-07-21-分布式链路追踪系统之二进制安装skywalking - Linux-1874.md]
last_updated: 2026-07-22
---

## 定义
分布式链路追踪（Distributed Tracing）是一种跟踪请求在分布式系统中完整路径的可观测性技术，能够监控和诊断微服务架构中的性能瓶颈和异常。

## 关键信息
- **核心能力**：追踪请求跨服务的完整调用链路、记录每个节点的耗时和状态
- **代表产品**：SkyWalking、Zipkin、Jaeger
- **核心组件**：OAP（可观测性分析平台）、UI（前端展示）、存储后端

## 关联连接
- [[SkyWalking]] — Apache 开源链路追踪系统
- [[Elasticsearch]] — 常用存储后端
- [[摘要-skywalking-install]] — 来源
