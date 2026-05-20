---
title: "JWT"
type: entity
tags: [认证, 安全, Token]
sources: [raw/01-articles/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

JWT（JSON Web Token）是一种开放标准（RFC 7519），用于在各方之间安全地传输信息作为 JSON 对象。它是一种无状态的认证机制，服务端不需要存储 Token 信息。

## 关键信息

### 三段结构

JWT 由点号分隔的三部分组成：

1. **Header**：声明算法类型（如 HS256）
2. **Payload**：存储用户信息（userId、角色、过期时间等），仅 Base64 编码，**不加密**，不能放敏感数据
3. **Signature**：用 Header + Payload + 服务端密钥计算的签名，用于防篡改

### 认证流程

1. 用户登录，服务端签发 Token
2. 客户端存储 Token（通常 localStorage）
3. 请求时在 Header 中携带：`Authorization: Bearer <token>`
4. 服务端验签，从 Payload 取用户信息，全程不查数据库

### 核心优势

- **无状态**：验签不依赖服务端存储，适合分布式场景
- **跨服务身份传递**：微服务架构中网关验签后下游直接使用

### 局限性

- 无法主动吊销已签发的 Token
- 无法让特定 Token 立即失效
- 需要配合 Redis 黑名单才能实现踢人下线等功能

## 关联连接
- [[摘要-token-redis-interview]] — JWT 与 Redis 的深度分析
- [[摘要-springboot4-security7-vue3-best-practice]] — JWT 在前后端分离项目中的实践
- [[jwt-stateless]] — JWT 无状态认证原理
- [[token-blacklist]] — Token 黑名单机制
- [[dual-token-mechanism]] — 双 Token 续期方案
- [[Redis]] — Token 存储方案
- [[SpringSecurity]] — JWT 集成安全框架
