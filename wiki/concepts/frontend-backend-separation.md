---
title: "frontend-backend-separation"
type: concept
tags: [架构, 前后端分离, Web开发]
sources:
  - raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md
  - raw/02-papers/前端工程化_4小时速通（语雀同款）.pdf
last_updated: 2026-05-22
---

## 定义

前后端分离是一种 Web 应用架构模式，前端和后端独立开发、独立部署，通过 API 接口进行数据交互。

## 核心原则

### 架构特点

- **前端**：Vue/React SPA 应用，负责 UI 渲染和用户交互
- **后端**：RESTful API 服务，负责业务逻辑和数据处理
- **通信**：JSON 格式数据交换

### 关键约定

| 约定 | 说明 |
|------|------|
| 统一响应格式 | `{ code, message, data, timestamp }` |
| 统一错误码 | 系统级 < 1000，业务级 ≥ 1000 |
| RESTful 风格 | GET 查询、POST 新增、PUT 修改、DELETE 删除 |
| 接口版本化 | `/api/v1/users` |
| 时间格式统一 | ISO 8601 |
| 分页参数统一 | `page` + `size`，返回 `total` |

### 认证方案

- **JWT 无状态认证**：后端不存储会话
- **Token 在 Header 中传递**：`Authorization: Bearer <token>`
- **CORS 跨域处理**：开发环境用 Vite Proxy，生产环境用 Nginx 反向代理

### 部署架构

```
用户 → Nginx（前端静态资源 + API 反向代理）
         ↓
    后端 API 服务
         ↓
    MySQL + Redis
```

## 关联连接
- [[SpringBoot]] — 后端框架
- [[Vue3]] — 前端框架
- [[JWT]] — 认证方案
- [[cors]] — 跨域处理
- [[Nginx]] — 反向代理
- [[摘要-springboot4-security7-vue3-best-practice]] — 完整实践
- [[摘要-frontend-engineering]] — 前端工程化速通
