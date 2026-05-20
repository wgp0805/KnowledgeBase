---
title: "dual-token-mechanism"
type: concept
tags: [认证, JWT, Token, 续期]
sources: [raw/01-articles/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

双 Token 机制是一种解决 JWT Token 续期问题的方案，通过签发两个不同用途的 Token 来平衡安全性和用户体验。

## 核心原理

### 两种 Token

| Token 类型 | 有效期 | 用途 | 存储位置 |
|-----------|--------|------|---------|
| AccessToken | 短（30分钟） | 实际鉴权 | 前端内存/localStorage |
| RefreshToken | 长（7天） | 换取新 AccessToken | Redis（支持吊销） |

### 续期流程

1. AccessToken 过期 → 前端用 RefreshToken 请求新 AccessToken
2. 服务端验证 RefreshToken 有效性
3. 生成新 AccessToken 返回，用户无感
4. 用户修改密码 → 删除 Redis 中的 RefreshToken → 自动失效

### 前端实现

```typescript
// Axios 响应拦截器中处理 401
if (error.response?.status === 401 && !originalRequest._retry) {
    const refreshToken = getRefreshToken()
    const { data } = await axios.post('/api/auth/refresh', { refreshToken })
    setAccessToken(data.data.accessToken)
    // 重发原始请求
}
```

### 关键设计

- **AccessToken 短有效期**：降低泄露风险
- **RefreshToken 存 Redis**：支持主动吊销
- **无感刷新**：用户感知不到 Token 曾经过期
- **并发处理**：请求队列确保只刷新一次

## 关联连接
- [[JWT]] — JWT 技术实体
- [[token-blacklist]] — Token 黑名单机制
- [[Axios]] — 前端 Token 刷新实现
- [[Redis]] — RefreshToken 存储
- [[摘要-token-redis-interview]] — 详细分析
- [[摘要-springboot4-security7-vue3-best-practice]] — 工程实践
