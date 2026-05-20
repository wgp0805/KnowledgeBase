---
title: "Axios"
type: entity
tags: [前端, HTTP, 网络请求]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

Axios 是一个基于 Promise 的 HTTP 客户端，用于浏览器和 Node.js 环境。在前端项目中广泛用于 API 请求。

## 关键信息

### 核心特性

- **拦截器机制**：请求拦截器和响应拦截器，可统一处理 Token、错误等
- **Promise API**：支持 async/await 语法
- **自动转换**：自动转换 JSON 数据
- **取消请求**：支持取消请求

### Token 无感刷新实现

```typescript
let isRefreshing = false
let pendingRequests = []

service.interceptors.response.use(
  async (error) => {
    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // 排队等待刷新完成
        return new Promise((resolve) => {
          pendingRequests.push((newToken) => {
            originalRequest.headers.Authorization = `Bearer ${newToken}`
            resolve(service(originalRequest))
          })
        })
      }
      isRefreshing = true
      // 用 RefreshToken 换取新的 AccessToken
      // 刷新完成后通知所有排队的请求
    }
  }
)
```

### 关键设计

- **isRefreshing 标志位**：确保只刷新一次 Token
- **pendingRequests 队列**：并发请求遇到 401 时排队等待
- **无感体验**：用户感知不到 Token 曾经过期

## 关联连接
- [[摘要-springboot4-security7-vue3-best-practice]] — Axios 在项目中的封装
- [[Vue3]] — 前端框架
- [[JWT]] — Token 认证机制
- [[dual-token-mechanism]] — 双 Token 续期机制
