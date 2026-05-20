---
title: "token-blacklist"
type: concept
tags: [认证, JWT, Redis, 安全]
sources: [raw/01-articles/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

Token 黑名单是一种在保持 JWT 无状态优势的同时，实现 Token 主动吊销的机制。只存储"已失效"的 Token，正常请求不写 Redis。

## 核心原理

### 实现方式

```java
// 退出登录时，把 token 加入黑名单
public void logout(String token) {
    long ttl = jwtUtil.getExpiration(token) - System.currentTimeMillis();
    if (ttl > 0) {
        redisTemplate.opsForValue().set(
            "blacklist:" + token, "1", ttl, TimeUnit.MILLISECONDS
        );
    }
}

// 验证 token 时，先查黑名单
public boolean isTokenValid(String token) {
    if (redisTemplate.hasKey("blacklist:" + token)) {
        return false;
    }
    return jwtUtil.verify(token);
}
```

### 设计要点

- **TTL 对齐**：黑名单 key 的过期时间与 Token 剩余有效期一致，避免垃圾数据
- **前缀区分**：使用 `blacklist:` 前缀，便于管理和批量操作
- **轻量存储**：只存失效 Token，存储开销小

### 与白名单方案对比

| 方案 | 存什么 | Redis 查询次数 | 能否主动吊销 | 适用场景 |
|------|--------|---------------|-------------|---------|
| 纯 JWT | 不存 | 0 | 不能 | 跨服务、一次性凭证 |
| JWT + 黑名单 | 存失效 token | 1 | 能 | 多数业务系统 |
| Token 存 Redis（白名单） | 存所有 token | 1 | 能 | 需要在线状态管理 |

## 关联连接
- [[JWT]] — JWT 技术实体
- [[jwt-stateless]] — JWT 无状态原理
- [[Redis]] — 黑名单存储
- [[摘要-token-redis-interview]] — 详细分析
