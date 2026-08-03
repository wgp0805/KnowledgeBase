---
title: "摘要-sso-single-sign-on"
type: source
tags: [来源, 原始文件, SSO, 身份认证, CAS]
sources: [raw/01-articles/公司系统太多，能不能实现账号互通？.md]
last_updated: 2026-07-16
---

## 核心摘要
介绍企业多系统环境下的身份认证演进，从传统 Session/Cookie 机制到分布式 Session 共享，再到 SSO 单点登录（CAS 协议）的完整实现原理。文章通过 CAS 协议的 Demo 代码演示了票据（ticket）验证流程，并对比了 CAS 与 OAuth2 在安全边界上的本质区别：CAS 保障客户端资源安全，OAuth2 保障服务端资源安全。

## 关联连接
- [[CAS协议]] — 中央认证服务框架，实现 SSO 的底层原理
- [[SSO]] — 单点登录概念
- [[Session]] — 传统会话管理机制
- [[Cookie]] — 客户端状态存储
- [[OAuth2]] — 三方授权协议，与 CAS 互补
- [[Redis]] — Session 集中存储方案
