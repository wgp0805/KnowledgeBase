---
title: "双 Token（AccessToken + RefreshToken）安全设计分析"
type: synthesis
tags: [认证, JWT, 安全, Token]
sources: [raw/09-archive/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md]
last_updated: 2026-06-11
---

# 双 Token（AccessToken + RefreshToken）安全设计分析

## 核心矛盾

双 Token 设计的核心优势在于**攻击面不同、不是两个 Token 等价**。假设攻击者同时拿到两个 Token，确实等于获得了永久门票。但这个设计的防御目标不是这种场景。

## 安全优势的五个层次

### 1. 暴露频率不对称

- **AccessToken** 每次请求都带着（Authorization header），经手前端代码、网络传输、可能被日志记录，暴露面极大
- **RefreshToken** 只在续期那一次传输，暴露面小得多
- 常见的攻击手段（XSS 扫 localStorage、中间人嗅探）往往只拿到 AccessToken，拿不到 RefreshToken

### 2. 短效缩小攻击窗口

- 只拿到 AccessToken → 30 分钟就失效，攻击者能发几个请求就废了
- 纯 JWT 一个 Token 管 7 天，偷到就炸了
- [[jwt-stateless]]

### 3. 设备指纹绑定

- 服务端续期时可以校验设备环境（IP、User-Agent、浏览器指纹）
- 发现异常直接拒绝续期，要求重新登录

### 4. RefreshToken Rotation（最佳实践）

- 每次续期时同时生成新 RefreshToken，旧的立即作废
- 攻击者偷到的 RefreshToken 只能用一次
- 如果合法用户先用了，攻击者的 RefreshToken 自动失效

### 5. 被动吊销能力

- RefreshToken 存在 Redis 里，管理员可以主动删除
- 纯 JWT 无法做到主动吊销
- [[token-blacklist]]

## 最终结论

这个设计的核心假设是 **RefreshToken 比 AccessToken 更难偷**，不是两个一样容易。如果攻击者能同时偷到两个，说明系统已经被攻破到一定程度（如全站 XSS），此时防御重心应放在修复 XSS/CSRF 等更根本的安全问题，而不是 Token 机制本身。

## 关键设计要点

| Token 类型 | 有效期 | 存储 | 暴露频率 | 吊销能力 |
|-----------|--------|------|---------|---------|
| AccessToken | 短（30 分钟） | 前端内存/localStorage | 高（每次请求） | ❌ |
| RefreshToken | 长（7 天） | Redis | 低（仅续期） | ✅ 主动吊销 |

## 关联连接

- [[dual-token-mechanism]] — 双 Token 续期方案
- [[token-blacklist]] — Token 黑名单机制
- [[jwt-stateless]] — JWT 无状态原理
- [[JWT]] — JWT 技术实体
- [[Redis]] — RefreshToken 存储
- [[spring-security-jwt-redis-best-practice]] — Spring Security + JWT + Redis 最佳实践
