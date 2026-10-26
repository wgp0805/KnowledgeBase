---
title: "Vite"
type: entity
tags: [前端构建, 开发服务器, ES模块, React]
sources: [raw/09-archive/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md, raw/09-archive/2026-10-12-从 0 到 1：Electron41 + Vite8 + OpenAI SDK 接入 DeepSeek-V4.1-Flash 桌面端AI系统 - yxybox.md]
last_updated: 2026-10-13
---

## 定义
新一代前端构建工具与开发服务器，基于原生 ES 模块实现极速冷启动与按需编译。开发服务器默认监听 5173 端口，支持代理配置将 API 请求转发到后端。

## 关键信息
- 在 [[RenoPit]] 开发环境中，Vite 在 5173 端口启动，把 `/api` 代理到 `localhost:8000`
- 通过环境变量（如 `VITE_DEMO_MODE`）控制前端行为，`main.tsx` 中动态导入 Demo 模块
- 生产构建输出静态文件，由 [[Nginx]] 提供服务
- 开发与生产的差异由代理层吸收，React 页面无需维护两套后端地址
- **桌面 AI 客户端中的用法（2026-10-12，详见 [[摘要-electron41-vite8-deepseek桌面ai]]）**：Vite 8.3 + Vue 3 `<script setup>` 作为 [[Electron]] 渲染层，配合 Arco Design 组件库与 Pinia 管理主题/会话状态；布局采用 Titlebar + Sidebar + router-view + keep-alive 的桌面三段式

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 应用项目
- [[React]] — 配合的前端框架
- [[Nginx]] — 生产环境对应物
- [[DemoMode]] — Vite 环境变量驱动的模式
- [[摘要-electron41-vite8-deepseek桌面ai]] — 来源（Vite 8 桌面 AI 客户端）
