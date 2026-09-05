---
title: "Vite"
type: entity
tags: [前端构建, 开发服务器, ES模块, React]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
新一代前端构建工具与开发服务器，基于原生 ES 模块实现极速冷启动与按需编译。开发服务器默认监听 5173 端口，支持代理配置将 API 请求转发到后端。

## 关键信息
- 在 [[RenoPit]] 开发环境中，Vite 在 5173 端口启动，把 `/api` 代理到 `localhost:8000`
- 通过环境变量（如 `VITE_DEMO_MODE`）控制前端行为，`main.tsx` 中动态导入 Demo 模块
- 生产构建输出静态文件，由 [[Nginx]] 提供服务
- 开发与生产的差异由代理层吸收，React 页面无需维护两套后端地址

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 应用项目
- [[React]] — 配合的前端框架
- [[Nginx]] — 生产环境对应物
- [[DemoMode]] — Vite 环境变量驱动的模式
