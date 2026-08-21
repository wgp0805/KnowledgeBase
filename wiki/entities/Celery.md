---
title: "Celery"
type: entity
tags: [Python, 异步任务, 任务队列, 分布式]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
Python 分布式异步任务队列框架，基于消息传递（通常配合 Redis/RabbitMQ 作为 Broker）实现任务分发与异步执行。广泛用于定时任务、耗时计算、后台处理等场景。

## 关键信息
- 在 [[RenoPit]] 项目中作为异步 Worker，处理 AI 报告生成等耗时任务
- 健康检查统计在线 Worker 数量与 Redis 队列深度
- Docker Compose 中与 FastAPI 共享 uploads/reports 卷，FastAPI 保存的文件可被 Celery 读取，Worker 生成的内容可被 API 返回
- Broker 通常使用 [[Redis]] 或 [[RabbitMQ]]

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 应用项目
- [[FastAPI]] — 配合的后端框架
- [[Redis]] — 常用 Broker
- [[RabbitMQ]] — 常用 Broker
- [[HealthCheck]] — 健康检查项之一
