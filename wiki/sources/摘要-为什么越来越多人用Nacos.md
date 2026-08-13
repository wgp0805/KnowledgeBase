---
title: "摘要-为什么越来越多人用Nacos"
type: source
tags: [来源, 微服务, Nacos, 注册中心, 配置中心]
sources: [raw/09-archive/为什么越来越多人用Nacos？.md]
last_updated: 2026-08-05
---

## 核心摘要
苏三从"从 Eureka 到 Nacos，微服务注册中心的一次认知升级"视角拆解 Nacos 越来越普及的原因。核心答案：Nacos 把**服务注册与发现**和**动态配置管理**这两件微服务架构最核心的事做成了"一件事"，只需维护一套系统，且服务发现与配置推送共享同一套基础设施。文章深入底层原理：Nacos 采用 **AP/CP 双模**设计哲学（服务发现走 Distro 协议的 AP 最终一致性，配置管理走 JRaft 的 CP 强一致性，按场景切换）；Distro 协议以**责任分片 + 读写分离**实现高吞吐服务发现，注册表更新使用 **CopyOnWrite** 消除读写并发冲突；配置推送用的是**长轮询（Long Polling）**而非 WebSocket。性能上 Nacos 2.0 将通信从 HTTP 升级为 gRPC，服务发现延迟从 800ms 降到 20ms（降 96%）；Nacos 3.0 定位从"云原生应用平台"升级为"AI Agent 应用平台"，新增 **AI Registry** 模块（模型层/工具层/智能体层），其中工具层即 **MCP Registry**，实现 LLM 与 MCP 工具的自动发现、自动注册与智能检索，降低 Token 消耗。文中附 4 大注册中心（Nacos/Eureka/Consul/ZooKeeper）对比、3 步实战跑通（单机启动 + Spring Boot 接入 + @RefreshScope 动态刷新）与适用场景选型表。

## 关联连接
- [[Nacos]] — 文章核心实体
- [[苏三]] — 文章作者
- [[Distro协议]] — Nacos 自研的 AP 一致性协议
- [[AI Registry]] — Nacos 3.0 面向 AI Agent 的新模块
- [[长轮询]] — 配置推送机制
- [[Eureka]] — 主要对比对象（2.x 已停止维护）
- [[SpringCloudAlibaba]] — 深度集成生态
- [[microservices]] — 微服务架构上下文
- [[MCP]] — MCP Registry 关联协议
- [[Agent]] — AI Agent 场景
