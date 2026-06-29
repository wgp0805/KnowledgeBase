---
title: "摘要-jwt-双token续签设计"
type: source
tags: [来源, 原始文件, JWT, 认证, OAuth2, 工程实践]
sources: [raw/01-articles/一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？.md]
last_updated: 2026-06-29
---

## 核心摘要

胖虎《一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？》从**根本矛盾**出发回答双 Token 设计的"为什么"。**单 Token 的死循环**：过期时间短 → 用户体验差（填表 401 跳登录）；过期时间长 → 安全风险大（泄露后窗口长）；加黑名单 → JWT 退化成"看起来像 JWT、跑起来像 Session"。双 Token 拆解的本质是**职责分离**：Access Token 短命（10–30 分钟）走业务接口，Refresh Token 长寿（7–30 天）**只走刷新接口**。

**关键洞见**：
1. **Refresh Token 不应该是 JWT** — 应做成"随机字符串 + 服务端存 hash + 关联 userId/设备/过期时间"，这才有"可撤销的登录态"。若做成无状态 JWT，单 Token 的"无法主动失效"问题原地复现
2. **Refresh Token Rotation（轮换）** — 每次刷新换新 Refresh Token、旧的作废；旧 Token 二次出现即视为重放攻击，**整组 token family 一并吊销**。源自 RFC 9700 OAuth 2.0 Security BCP
3. **前端 401 并发刷新坑** — 多个接口同时 401 时，只能允许一个刷新请求在路上，其他失败请求排队等待新 Access Token 后重放；否则旧 Refresh Token 被多次使用，触发轮换检测后用户被误踢
4. **退出/改密码/封禁实际删什么** — 删 Refresh Token 即可（Access Token 自然过期就行），改密码删用户全部 Refresh Token，发现重放删整组 token family
5. **存储建议** — Web Access Token 放内存、Refresh Token 放 HttpOnly+Secure+SameSite Cookie；App 端用 iOS Keychain / Android Keystore

**适用边界**：内部后台/短期活动页/已有 Session 架构没必要硬上双 Token；移动 App、SaaS、开放平台、面向 C 端 Web 应用是双 Token 的核心场景。

## 关联连接
- [[dual-token-mechanism]] — 双 Token 核心机制
- [[refresh-token-rotation]] — 本文最关键的工程概念增量
- [[JWT]] — 底层认证技术
- [[Token认证机制]] — 上层认证范式
- [[jwt-stateless]] — 单 Token 的局限性根源
- [[token-blacklist]] — 单 Token 的折衷方案
- [[Redis]] — Refresh Token 存储
- [[摘要-token-redis-interview]] — 同主题前置文章（"是什么/怎么做"视角）
- [[摘要-springboot4-security7-vue3-best-practice]] — 双 Token 工程实践
