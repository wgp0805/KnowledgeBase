---
title: "CAS协议"
type: concept
tags: [认证, SSO, 单点登录, 协议]
sources: [raw/09-archive/公司系统太多，能不能实现账号互通？.md]
last_updated: 2026-07-16
---

## 定义
CAS（Central Authentication Service）是中央认证服务框架，基于 Kerberos 票据方式实现 SSO 单点登录，为 Web 应用系统提供可靠的单点登录解决方案。

## 关键信息
- **核心流程**：用户访问业务系统 → 未登录跳转到 CAS 登录页 → 登录成功生成 ticket → 存入 Redis → 重定向回业务系统 → 业务系统用 ticket 查询 Redis 获取 session → 种 cookie 完成登录
- **Ticket 机制**：CAS 生成唯一票据（UUID），存入 Redis 的数据结构为 `<ticket, sessionid>`
- **安全边界**：CAS 保障的是客户端（CAS 客户端）的用户资源安全，即"用户有没有权限访问我的资源"
- **与 OAuth2 区别**：
  - CAS：统一账号密码身份认证 → 用 CAS
  - OAuth2：授权第三方服务使用我方资源 → 用 OAuth2
- **Demo 实现**：Spring Boot + Redis + Filter，通过 LoginFilter 拦截未登录请求，SSOFilter 处理 ticket 验证

## 关联连接
- [[SSO]] — 单点登录概念
- [[Session]] — 传统会话管理机制
- [[OAuth2]] — 三方授权协议，与 CAS 互补
- [[Redis]] — CAS ticket 存储介质
- [[摘要-sso-single-sign-on]] — 来源
