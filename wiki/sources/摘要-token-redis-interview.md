---
title: "摘要-token-redis-interview"
type: source
tags: [JWT, Redis, 认证, 面试]
sources: [raw/01-articles/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md]
last_updated: 2026-05-20
---

## 核心摘要

本文深入探讨了 JWT 无状态认证的本质及其局限性，解释了为什么在实际业务中需要将 Token 存入 Redis。文章从 JWT 的三段结构（Header、Payload、Signature）讲起，分析了纯 JWT 方案无法解决的四大场景：用户密码被盗需立即踢下线、封禁用户、修改密码后其他设备失效、Token 过期导致表单丢失。介绍了 JWT+Redis 黑名单和 Token 存 Redis（白名单）两种方案的区别与适用场景，并讲解了双 Token（AccessToken + RefreshToken）续期机制。最后给出了面试中如何回答"Token 放 Redis"这个问题的建议。

## 关联连接
- [[JWT]] — JSON Web Token 认证机制
- [[Redis]] — Token 存储与黑名单存储
- [[jwt-stateless]] — JWT 无状态认证原理
- [[token-blacklist]] — Token 黑名单机制
- [[dual-token-mechanism]] — 双 Token 续期方案
