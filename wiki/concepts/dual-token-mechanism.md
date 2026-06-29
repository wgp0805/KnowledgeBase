---
title: "dual-token-mechanism"
type: concept
tags: [认证, JWT, Token, 续期]
sources: [raw/01-articles/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md, raw/01-articles/一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？.md]
last_updated: 2026-06-29
---

## 定义

双 Token 机制是一种解决 JWT Token 续期问题的方案，通过签发两个不同用途的 Token 来平衡安全性和用户体验。**它本质不是"两个字符串"，而是把"登录态"拆成两层**：一层负责日常通行（Access Token），一层负责长期续命（Refresh Token）。

## 为什么单 Token 不够：根本矛盾

单 Token 在面向大量 C 端用户时会撞上一堵墙——**过期时间怎么设**：

| 设置 | 后果 |
|------|------|
| 短（15–30 分钟） | 安全好，但用户填表 401 跳登录"制造血压" |
| 长（7–30 天） | 体验好，但 Token 泄露后窗口很长 |
| 长 + 黑名单 | JWT 原本省掉的服务端状态查询又加回来，"看起来像 JWT、跑起来像 Session" |

**双 Token 不是炫技，它专门来拆这个矛盾**：把"高频暴露的访问凭证"和"低频出现的续签凭证"分开做有效期设计。

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

## 关键设计哲学：Refresh Token 不应该做成 JWT

很多人误把 Refresh Token 也实现为长 TTL 的 JWT——这是反模式。

**正确做法**：Refresh Token 应当是**随机字符串**，服务端存其 **hash**，关联 `userId / deviceId / 过期时间`。

```
Refresh Token = secureRandom 字符串
Redis 存储: key=hash(rt), value={userId, deviceId, expiry}
```

这样才有"**可撤销的登录态**"——这是 Refresh Token 真正值钱的地方：

| 触发事件 | 服务端操作 |
|---------|-----------|
| 用户退出登录 | 删除该设备的 Refresh Token 记录 |
| 用户修改密码 | 删除该用户**所有设备**的 Refresh Token |
| 检测到风险设备 | 删除对应设备的 Refresh Token |
| 管理员封禁用户 | 删除所有 Refresh Token |

如果 Refresh Token 也做成无状态 JWT 不存任何状态，它只是一个更长寿的 JWT——单 Token 的"无法主动失效"问题原地复现。

## 安全强化：Refresh Token Rotation

进阶方案是**每次刷新都换新 Refresh Token、旧的立刻作废**，详见 [[refresh-token-rotation]]。这能：
1. 限制泄露 Token 的可用窗口（用过即换）
2. 检测重放攻击（旧 Token 二次出现 = 异常 → 吊销整组 token family）

需注意前端必须配套**并发刷新控制**，否则旧 RT 被多次使用会误触发踢登录。

## 存储位置建议

| 端 | Access Token | Refresh Token |
|----|-------------|---------------|
| **Web** | 内存（避免 XSS 窃取） | HttpOnly + Secure + SameSite Cookie |
| **App** | 内存或安全存储 | iOS Keychain / Android Keystore |

Cookie 模式下别忘了配 CSRF 防护（SameSite 不是免死金牌，严谨系统还会校验 Origin / Referer 或叠加 CSRF Token）。

## 不适合双 Token 的场景

- 内部管理后台（用户少，重新登录可接受）
- 短期活动页（生命周期就几天）
- 已有 Session 架构（Session 天然有状态，删 Session 即可）

双 Token 真正适合：**移动 App、SaaS、开放平台、面向 C 端 Web 应用**——用户量大、登录态保持很多天、业务接口希望保留 JWT 无状态校验、安全又不能完全忽略。

## 关联连接
- [[JWT]] — JWT 技术实体
- [[refresh-token-rotation]] — 安全强化方案 + 并发刷新坑
- [[Token认证机制]] — 上位认证范式
- [[token-blacklist]] — Token 黑名单机制（互补/兜底）
- [[jwt-stateless]] — 单 Token 局限性的根源
- [[Axios]] — 前端 Token 刷新实现
- [[Redis]] — RefreshToken 存储
- [[摘要-token-redis-interview]] — "是什么/怎么做"视角
- [[摘要-jwt-双token续签设计]] — "为什么/工程边界"视角
- [[摘要-springboot4-security7-vue3-best-practice]] — Spring Security 工程实践
