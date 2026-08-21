---
title: "摘要-renopit-demo-healthcheck-docker"
type: source
tags: [来源, 原始文件, RenoPit, Demo模式, 健康检查, Docker]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 核心摘要
fthux 撰写的「装闭 RenoPit」系列第 14 篇，覆盖该 AI 装修报告项目的运行层：Demo 模式、健康检查与 Docker 部署。Demo 模式通过 `VITE_DEMO_MODE` 环境变量在 `main.tsx` 中动态导入 `demo/mockApi.ts`，劫持 `window.fetch` 拦截 `/api` 请求并返回 `demoData.ts` 固定数据，命中后等待 200ms 模拟网络延迟，未命中则透传真实 fetch（如读取 GitHub Star）。`normalizePath()` 兼容 `/api` 与 `/api/v1`，`matchPath()` 支持 `:id` 动态参数，写操作返回 400 提示部署后端，页面组件无需 Demo 专用副本。

健康检查分三组共八项：核心依赖（PostgreSQL/Redis/文件系统，错误即 unhealthy）、业务依赖（LLM/Celery/应用数据，错误或警告即 degraded）、信息检查（Python 运行时/外部网络，仅展示）。`/health/data` 提供 JSON 接口与 HTML 仪表盘，FastAPI 还提供自定义 Swagger/ReDoc 页面。

Docker Compose 定义 PostgreSQL、Redis、FastAPI、Celery Worker、前端五服务，通过 `depends_on.condition: service_healthy` 等待核心依赖就绪，三个命名卷（postgres_data/uploads/reports）持久化数据。开发环境 Vite 5173 代理 `/api` 到 8000；生产镜像由 Nginx 提供静态文件，`try_files ... /index.html` 支持前端路由，`/api/` 转发到 `backend:8000`，SSE 关闭代理缓冲并设读取超时为一小时。

## 关联连接
- [[RenoPit]] — 本文解析的开源 AI 装修报告项目
- [[fthux]] — 本文作者，博客园博主
- [[PostgreSQL]] — 核心依赖之一，健康检查执行 SELECT 1
- [[Redis]] — 核心依赖之一，健康检查执行 PING
- [[Docker]] — Compose 编排五服务
- [[FastAPI]] — 后端框架，提供健康检查与 Swagger/ReDoc
- [[Celery]] — 异步任务 Worker，健康检查统计在线 Worker 与队列深度
- [[Nginx]] — 生产镜像静态文件服务与反向代理
- [[Vite]] — 开发服务器与前端构建工具
- [[React]] — 前端框架，Demo 模式劫持 window.fetch
- [[SSE]] — Nginx 针对 SSE 关闭代理缓冲
- [[DemoMode]] — 前端无后端演示模式概念
- [[HealthCheck]] — 三组分级健康检查方法论
