---
title: "SkyWalking"
type: entity
tags: [APM, 分布式追踪, 可观测性, Apache]
sources: [raw/01-articles/2026-07-21-分布式链路追踪系统之二进制安装skywalking - Linux-1874.md, raw/01-articles/2026-07-22-分布式链路追踪系统之docker-compose安装skywalking - Linux-1874.md]
last_updated: 2026-07-23
---

## 定义
Apache SkyWalking 是一款开源的分布式链路追踪系统（APM），为微服务架构提供可观测性分析能力。核心组件包括 SkyWalking-OAP（可观测性分析平台）和 SkyWalking-UI（前端展示服务）。

## 关键信息
- **版本**：9.3.0
- **存储后端**：支持 Elasticsearch 等多种存储
- **OAP 端口**：gRPC 11800，HTTP 12800
- **UI 端口**：8080
- **部署方式**：支持二进制安装、Docker Compose 部署（三服务：elasticsearch、skywalking-oap、skywalking-ui）
- **运行环境**：依赖 Java（OpenJDK）运行环境，支持 systemd 服务管理
- **Docker Compose 健康检查**：OAP 使用 `/skywalking/bin/swctl ch` 命令，ES 使用 HTTP 9200 集群健康检查，UI 使用 8080 HTTP 检查

## 关联连接
- [[Elasticsearch]] — SkyWalking 常用存储后端
- [[distributed-tracing]] — 分布式链路追踪
- [[摘要-skywalking-install]] — 来源
