---
title: "DemoMode"
type: concept
tags: [前端, 演示模式, Mock, 概念]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
前端应用的演示模式，通过环境变量开关在无后端环境下运行完整前端界面。核心实现是劫持 `window.fetch` 拦截 API 请求，命中 Mock Handler 返回固定数据，未命中透传真实 fetch。页面组件无需 Demo 专用副本，请求在浏览器内被拦截。

## 关键信息
- **触发方式**：环境变量（如 `VITE_DEMO_MODE=true`）在入口文件（如 `main.tsx`）中动态导入 Mock 模块
- **fetch 劫持**：保存原始 `window.fetch`，替换为包装函数，先尝试匹配 Mock Handler，命中后可模拟网络延迟（如 200ms），未命中调用原始 fetch
- **路径匹配**：`normalizePath()` 去除查询参数并兼容不同 API 前缀，`matchPath()` 支持 `:id` 动态参数
- **写操作处理**：创建/复制/删除等写操作通常返回 400，提示用户部署完整后端
- **优势**：零后端成本展示完整产品形态，适合 GitHub Pages 等静态托管演示

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 典型应用
- [[Vite]] — 环境变量驱动
- [[React]] — 前端框架
- [[MockApi]] — 相关实现模式
