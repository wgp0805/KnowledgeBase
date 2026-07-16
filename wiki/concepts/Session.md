---
title: "Session"
type: concept
tags: [会话, Web, 认证, 机制]
sources: [raw/01-articles/公司系统太多，能不能实现账号互通？.md]
last_updated: 2026-07-16
---

## 定义
Session 是 Web 应用中面向用户的会话管理机制，通过 SessionID 标识用户，将用户上下文信息保存在服务端内存中，以解决 HTTP 无状态协议下的身份识别问题。

## 关键信息
- **产生原因**：HTTP 是无状态协议，服务器不自动维护客户上下文信息
- **工作原理**：服务器生成 SessionID → 通过 JSESSIONID 存入 cookie → 后续请求携带 SessionID → 服务端从内存中获取对应 session 数据
- **存储方式**：以散列表形式保存在服务器内存中，默认使用 cookie 传递 SessionID
- **JSESSIONID 限制**：不能跨窗口使用，新开浏览器窗口会获得新的 sessionid
- **集群困境**：分布式环境下，session 保存在单台服务器上，负载均衡可能导致请求打到不同服务器而丢失 session
- **解决方案**：
  - Session 复制：不同服务器间复制 session 数据（成本高、有延迟）
  - Session 集中存储：使用 Redis 等统一存储（推荐方案）

## 关联连接
- [[Cookie]] — SessionID 的传递载体
- [[Redis]] — Session 集中存储介质
- [[SSO]] — 跨系统身份认证
- [[CAS协议]] — 基于 ticket 的 SSO 实现
- [[摘要-sso-single-sign-on]] — 来源
