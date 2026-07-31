---
title: "OIDC"
type: concept
tags: [认证, 身份验证, OAuth2, SSO]
sources: [raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 定义
OpenID Connect（OIDC）是基于 OAuth 2.0 协议的身份认证层，通过 ID Token（JWT 格式）和 UserInfo 端点提供标准化的用户身份验证机制。

## 关键信息
- **定位**：OAuth 2.0 上层的认证协议，解决"你是谁"的问题
- **核心组件**：
  - ID Token：JWT 格式的用户身份凭证
  - UserInfo 端点：获取用户详细信息的 API
  - Discovery 文档：/.well-known/openid-configuration
- **与 OAuth 2.0 的关系**：OAuth 2.0 管授权（你能做什么），OIDC 管认证（你是谁）
- **与 Keycloak 的关系**：Keycloak 原生支持 OIDC，作为身份提供商（IdP）

## 关联连接
- [[OAuth2]] — OIDC 的底层授权协议
- [[SSO]] — 单点登录，OIDC 可实现 SSO
- [[SAML]] — 另一种 IDaaS 标准协议
- [[Keycloak]] — 支持 OIDC 的企业身份平台
- [[摘要-Docker部署Keycloak]] — 来源
