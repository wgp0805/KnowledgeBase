---
title: "HealthCheck"
type: concept
tags: [后端, 运维, 健康检查, 可观测性, 概念]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
后端服务的健康检查机制，通过端点（如 `/health/data`）暴露依赖与运行时状态，用于容器编排就绪探测、运维监控与故障定位。生产级健康检查通常**分级**：核心依赖决定整体可用性，业务依赖影响降级状态，信息检查仅展示。

## 关键信息
- **三组分级**（以 RenoPit 为典型）：
  - 核心依赖（如 PostgreSQL/Redis/文件系统）→ 错误时 `unhealthy`
  - 业务依赖（如 LLM/Celery/应用数据）→ 错误或警告时 `degraded`
  - 信息检查（如 Python 运行时/外部网络）→ 仅展示信息
- **总体状态判定**：任一核心项 error → unhealthy；核心正常但业务 error/warning → degraded；否则 healthy
- **检查内容示例**：
  - 数据库：`SELECT 1` + 连接池状态
  - Redis：`PING` + 内存信息
  - 文件系统：目录可写 + 磁盘剩余空间
  - LLM：TCP 连接 + 模型列表 + 模型存在性
  - Celery：在线 Worker 数 + 队列深度
- **输出形式**：JSON 接口（程序消费）+ HTML 仪表盘（人工查看），显示延迟与 extra 诊断字段
- **容器集成**：Docker Compose 中 `depends_on.condition: service_healthy` 依赖健康检查就绪

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 典型应用
- [[FastAPI]] — 健康检查端点框架
- [[Docker]] — 容器健康检查集成
- [[PostgreSQL]] — 核心依赖检查项
- [[Redis]] — 核心依赖检查项
- [[Celery]] — 业务依赖检查项
