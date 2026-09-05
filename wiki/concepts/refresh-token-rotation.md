---
title: "refresh-token-rotation"
type: concept
tags: [认证, JWT, OAuth2, 安全, Refresh Token]
sources: [raw/01-articles/一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？.md]
last_updated: 2026-06-29
---

## 定义

Refresh Token Rotation（**刷新令牌轮换**）是双 Token 机制的安全强化方案：**每次刷新接口都同时签发新的 Access Token 和新的 Refresh Token，并立刻作废旧的 Refresh Token**。配合"重放检测"，旧 Token 一旦二次出现，整组 token family 全部吊销。该方案源自 **RFC 9700 OAuth 2.0 Security Best Current Practice**。

## 核心原理

### 轮换流程

```
旧 RT (有效)
   │ 调用刷新接口
   ▼
服务端：验证 → 删除旧 RT → 生成新 AT + 新 RT → 返回
   │
   ▼
新 RT (有效)，旧 RT 立刻失效
```

### 重放检测（Token Family）

- 一个登录会话生成的所有 Refresh Token 视为同一个 **token family**（通常用 family_id 关联）
- 正常情况下，旧 RT 用过一次后**永远不该再出现**
- 若服务端检测到已作废的旧 RT 再次请求刷新 → **判定为重放攻击或并发 bug**
- 处理策略：吊销整组 token family，强制该设备重新登录

### 与"不轮换"的对比

| 方案 | 安全性 | 复杂度 | 客户端要求 |
|------|--------|--------|------------|
| Refresh Token 长期复用 | 低，泄露后长期可用 | 简单 | 无并发限制 |
| **Refresh Token Rotation** | 高，泄露窗口受限 + 检测重放 | 中 | **必须做并发刷新控制** |

## 前端 401 并发刷新坑

Access Token 过期的瞬间，页面上往往**多个请求同时返回 401**（列表/用户信息/通知/权限等）。

**错误做法**：每个 401 都触发一次刷新 → 第一个刷新成功后旧 RT 已废，后续刷新拿旧 RT 失败 → 触发重放检测 → 用户被踢登录页。

**正确做法**：
```javascript
let refreshing = false;
let queue = [];

async function handle401(originalRequest) {
  if (refreshing) {
    // 后续 401 排队等候
    return new Promise(resolve => {
      queue.push(token => {
        originalRequest.headers.Authorization = `Bearer ${token}`;
        resolve(api(originalRequest));
      });
    });
  }

  refreshing = true;
  try {
    const tokens = await refreshToken();
    saveTokens(tokens);
    queue.forEach(retry => retry(tokens.accessToken));
    queue = [];
    return api(originalRequest);
  } finally {
    refreshing = false;
  }
}
```

**核心约束**：同一时刻，**只允许一个刷新请求在路上**，其他失败请求排队、拿到新 Access Token 后统一重放。

## 后端工程要点

- Refresh Token **必须存服务端**（Redis 存 hash），无状态 JWT 实现的 RT 无法做轮换检测
- 旧 RT 删除与新 RT 写入应在**同一事务/原子操作**中，防止半失败
- 重放检测命中时，应**吊销整组 token family**（按 family_id 批量删除），而不是只废这一个
- 刷新接口要做风险检查：设备指纹、IP 异常、客户端版本

## 退出/改密码/封禁场景

| 触发事件 | 操作 |
|---------|------|
| 用户主动退出 | 删除当前设备的 Refresh Token |
| 修改密码 | 删除该用户**所有设备**的 Refresh Token |
| 管理员封禁 | 删除所有 Refresh Token + 业务接口校验用户状态 |
| 检测到 RT 重放 | 吊销整组 token family，该设备重新登录 |
| Access Token 残留风险 | 短 TTL 自然过期，必要时叠加 Access Token 黑名单/版本号 |

## 适用边界

**适合**：移动 App、SaaS、开放平台、面向 C 端 Web 应用（用户量大、保持长期登录、JWT 无状态校验 + 安全风险敏感）。

**不适合**：内部管理后台（用户少、可接受频繁登录）、短期活动页（生命周期短）、已有 Session 架构（Session 天然有状态、能直接撤销）。

## 关联连接
- [[dual-token-mechanism]] — 上位机制
- [[JWT]] — 底层 Access Token 技术
- [[Token认证机制]] — 上层认证范式
- [[token-blacklist]] — 互补的 Access Token 兜底方案
- [[jwt-stateless]] — 单 Token 局限性的对照
- [[Redis]] — Refresh Token hash 存储
- [[摘要-jwt-双token续签设计]] — 来源文章
