---
title: "Nacos"
type: entity
tags: [微服务, 注册中心, 配置中心]
sources: [raw/01-articles/docker部署nacos.md, raw/01-articles/pmhub微服务学习.md]
last_updated: 2026-05-19
---

## 定义
Nacos（Dynamic Naming and Configuration Service）是阿里巴巴开源的微服务基础设施组件，提供服务发现和配置管理能力。

## 关键信息
- 服务注册与发现：替代 Eureka，支持健康检查
- 配置管理：动态配置更新，支持 namespace/group/dataId 三级隔离
- 部署模式：单机（Derby 内嵌数据库）和集群（MySQL 存储）
- Docker 部署方式：环境变量配置 MySQL 数据源
- CAP 理论：遵循 AP 原则（可用性 + 分区容错性）
- 命名空间隔离：通过 namespace 实现环境和配置隔离（如生产/灰度），是全链路灰度发布的第一步
- 灰度实践：创建独立的 gray-namespace，灰度服务注册在此命名空间，通过 `service.gray.tag` 元数据标记节点身份

## 关联连接
- [[Docker]] — 容器化部署
- [[SpringBoot]] — 客户端集成
- [[RocketMQ]] — 消息队列
- [[SpringCloudGateway]] — API 网关
- [[grayscale-release]] — 全链路灰度发布的命名空间隔离基础

- [[摘要-alibaba-product-manual]] — 核心摘要
- [[摘要-pmhub微服务学习]] — 核心摘要
- [[摘要-SpringBoot优雅的加载配置文件的几种方式]] — 核心摘要
