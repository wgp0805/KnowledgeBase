---
title: "摘要-skywalking-docker-compose-install"
type: source
tags: [SkyWalking, 分布式追踪, Docker, 部署]
sources: [raw/01-articles/2026-07-22-分布式链路追踪系统之docker-compose安装skywalking - Linux-1874.md]
last_updated: 2026-07-23
---

## 核心摘要
本文详细介绍了使用 Docker Compose 部署 SkyWalking 9.3.0 + Elasticsearch 8.4.2 的完整过程。包含环境准备（Docker 安装）、编写 docker-compose.yml（三服务：elasticsearch、skywalking-oap、skywalking-ui）、私有仓库配置（insecure-registries）、启动验证等步骤。其中 OAP 使用 gRPC 11800 和 HTTP 12800 端口，UI 暴露 8080 端口。

## 关联连接
- [[SkyWalking]] — 分布式链路追踪系统
- [[Elasticsearch]] — 存储后端
- [[Docker]] — 容器化部署
- [[distributed-tracing]] — 分布式链路追踪