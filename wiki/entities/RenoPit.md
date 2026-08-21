---
title: "RenoPit"
type: entity
tags: [开源项目, AI应用, 装修, React, FastAPI]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
「装闭 RenoPit」是 fthux 开源的 AI 装修报告项目，完整业务链覆盖从装修素材上传到 AI 报告生成。项目代码托管于 [fthux/RenoPit](https://github.com/fthux/RenoPit)，技术栈为 React 前端 + FastAPI 后端 + Celery 异步 Worker + PostgreSQL/Redis 依赖。

## 关键信息
- **Demo 模式**：通过 `VITE_DEMO_MODE` 环境变量启用，动态导入 `demo/mockApi.ts` 劫持 `window.fetch`，命中 Mock Handler 后等待 200ms 模拟延迟，未命中透传真实 fetch。`normalizePath()` 兼容 `/api` 与 `/api/v1`，`matchPath()` 支持 `:id` 动态参数。写操作返回 400 提示部署后端，页面组件无需 Demo 专用副本。
- **健康检查**：`/health/data` 调用 `run_all_checks()` 执行八项检查分三组：
  - 核心依赖（PostgreSQL/Redis/文件系统）→ 错误即 unhealthy
  - 业务依赖（LLM/Celery/应用数据）→ 错误或警告即 degraded
  - 信息检查（Python 运行时/外部网络）→ 仅展示
  - 同时提供 JSON 接口与 HTML 仪表盘
- **Docker 部署**：Compose 定义五服务（PostgreSQL/Redis/FastAPI/Celery Worker/前端），`depends_on.condition: service_healthy` 等待核心依赖就绪，三个命名卷（postgres_data/uploads/reports）持久化。生产镜像由 Nginx 提供静态文件，`/api/` 转发到 `backend:8000`，SSE 关闭代理缓冲并设读取超时一小时。
- **系列文章**：共 14 篇源码解析，覆盖入口、数据模型、上传、异步任务、Prompt、LLM、文档核查、网页与 PDF 报告、Demo 模式、健康检查、Docker 部署的完整链路。

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[fthux]] — 项目作者
- [[FastAPI]] — 后端框架
- [[Celery]] — 异步任务 Worker
- [[PostgreSQL]] — 核心依赖数据库
- [[Redis]] — 核心依赖缓存
- [[Docker]] — 容器化部署
- [[Nginx]] — 生产反向代理
- [[React]] — 前端框架
- [[Vite]] — 前端构建工具
- [[DemoMode]] — Demo 模式概念
- [[HealthCheck]] — 健康检查方法论
- [[SSE]] — 服务器发送事件
