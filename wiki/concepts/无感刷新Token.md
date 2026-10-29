---
title: "无感刷新Token"
type: concept
tags: [认证, JWT, Token, 续期, 用户体验]
sources: [raw/09-archive/如何做到无感刷新Token.md]
last_updated: 2026-10-28
---

## 定义

无感刷新 Token 是一类让用户**感知不到登录态过期**的 Token 续期机制总称，目标是消除"业务操作中突然跳回登录页"的体验断层。按主导方分两条技术路线：**后端自动刷新**（纯后端、单 token）与**前端 token 续约**（前端主导、双 Token AT/RT）。

## 关键信息

### 路线一：后端自动刷新（单 token）

- 后端在校验 token 时计算 `过期时间 − 当前时间`，小于约定阈值则用 token 内信息重新签发新 token，放入**请求头**返回
- 前端拦截请求头：新 token 与本地不一致 → 替换本地存储
- 特点：全程只有 access-token 一个 token；依赖前端持续发请求才能触发刷新

### 路线二：前端 token 续约（双 Token AT/RT）

- 前后端约定**续约接口**；前端发现 token 快过期时主动调用，后端延长过期时间
- **AT/RT 分工哲学**：
  - **AT（Access Token）**：每个请求都携带，暴露机会多 → TTL 短，**减少劫持风险**
  - **RT（Refresh Token）**：只暴露在 auth 服务中用来刷新 AT，TTL 长，**增加便利性**
- "这是标准的安全处理，无需探讨合理性，好比 https 之于 http"——网络传输安全视角下的必然分工

### 边界场景：表单页长时间无请求

用户长时间填表不发任何请求 → 后端无法感知 token 过期 → 提交时返回 401。

| 路线 | 兜底方案 |
|------|---------|
| 纯后端 | 前端提交遇 401：表单存本地存储→跳登录→登录成功返回原页→从本地存储回显表单 |
| 前端双 Token | ① 监听 RT 过期时间，接近过期时主动/定期刷新 RT；② 做类似草稿箱的表单保存功能 |

### 与既有机制的层级关系

- **无感刷新 Token** 是目标/上位概念
- [[dual-token-mechanism]]（双 Token 机制）是前端续约路线的实现载体
- [[refresh-token-rotation]]（RT 轮换）是双 Token 之上的安全强化
- 三者的共同价值：把"高频暴露的访问凭证"和"低频出现的续签凭证"分开做有效期设计，兼顾安全与体验

## 关联连接
- [[摘要-无感刷新token]] — 来源（小哈，"怎么做"视角）
- [[dual-token-mechanism]] — 双 Token 机制（前端路线实现）
- [[refresh-token-rotation]] — RT 轮换安全强化
- [[JWT]] — 底层认证技术
- [[Token认证机制]] — 上位认证范式
- [[jwt-stateless]] — 单 Token 局限性的根源
- [[token-blacklist]] — 单 Token 折衷方案
- [[摘要-jwt-双token续签设计]] — 同主题姊妹篇（"为什么"视角）
- [[Redis]] — Refresh Token 存储
- [[小哈]] — 提炼来源作者
