---
title: "SkyWalking"
type: entity
tags: [APM, 分布式追踪, 可观测性, Apache]
sources: [raw/01-articles/2026-07-21-分布式链路追踪系统之二进制安装skywalking - Linux-1874.md, raw/01-articles/2026-07-22-分布式链路追踪系统之docker-compose安装skywalking - Linux-1874.md, raw/01-articles/2026-07-26-分布式链路追踪系统之skywalking java agent 的使用、skywalking web界面简介 - Linux-1874.md]
last_updated: 2026-07-27
---

## 定义
Apache SkyWalking 是一款开源的分布式链路追踪系统（APM），为微服务架构提供可观测性分析能力。核心组件包括 SkyWalking-OAP（可观测性分析平台）和 SkyWalking-UI（前端展示服务）。

## 关键信息
- **版本**：9.3.0
- **Java Agent 版本**：8.13.0
- **存储后端**：支持 Elasticsearch 等多种存储
- **OAP 端口**：gRPC 11800，HTTP 12800
- **UI 端口**：8080
- **部署方式**：支持二进制安装、Docker Compose 部署（三服务：elasticsearch、skywalking-oap、skywalking-ui）
- **运行环境**：依赖 Java（OpenJDK）运行环境，支持 systemd 服务管理
- **Docker Compose 健康检查**：OAP 使用 `/skywalking/bin/swctl ch` 命令，ES 使用 HTTP 9200 集群健康检查，UI 使用 8080 HTTP 检查

### SkyWalking Java Agent
- **下载**：`apache-skywalking-java-agent-8.13.0.tgz`，约 30MB
- **核心配置**（`config/agent.config`）：
  - `agent.service_name`：服务名称，对应 SW_AGENT_NAME 环境变量
  - `agent.namespace`：服务所属命名空间
  - `collector.backend_service`：SkyWalking OAP 服务地址（默认 11800 gRPC 端口）
- **启动方式**：通过 `-javaagent:/path/skywalking-agent.jar` JVM 参数附加到目标应用
- **支持语言**：SkyWalking 提供多种编程语言的 Agent，Java Agent 最为成熟
- **目录结构**：包含 config、plugins、activations、bootstrap-plugins、optional-plugins 等子目录

### SkyWalking Web 界面功能
- **仪表盘**：服务列表（Service），包含 Load（分钟请求数）、Success Rate（成功率）、Latency（延迟）、Apdex（应用性能指数）
- **Topology（拓扑图）**：自动生成程序调用关系图
- **Trace（跟踪信息）**：请求的完整调用链追踪
- **Log（日志）**：关联日志查看
- **Instance 概览**：数据库连接池、线程池信息
- **Endpoint（端点信息）**：URL 级别的请求次数、成功率和延迟
- **JVM 监控**：CPU、Memory、GC Time、GC Count、Thread Count、Class Count

## 关联连接
- [[Elasticsearch]] — SkyWalking 常用存储后端
- [[distributed-tracing]] — 分布式链路追踪
- [[Apdex]] — 应用性能指数，SkyWalking 仪表盘中的关键指标
- [[Halo]] — 常作为 SkyWalking Java Agent 演示案例的博客系统
- [[摘要-skywalking-java-agent-使用]] — SkyWalking Java Agent 安装配置与 Web 界面使用教程
- [[摘要-skywalking-install]] — 来源
