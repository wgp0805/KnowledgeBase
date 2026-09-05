---
title: "Keycloak"
type: entity
tags: [认证, SSO, OAuth2, RedHat, 开源]
sources: [raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 定义
Keycloak 是 Red Hat 出品的开源企业级身份认证和访问管理平台，提供 OAuth2、OIDC、SAML、SSO 等标准认证协议的支持。

## 关键信息
- **出品方**：Red Hat
- **核心能力**：
  - OAuth2/OIDC/SAML 标准协议支持
  - 单点登录（SSO）原生支持
  - 社交登录（微信/GitHub/Google 等）
  - 用户管理与统一管理控制台
- **企业认可度**：Red Hat 出品，大量企业生产环境使用
- **部署方式**：支持 Docker 部署，推荐 PostgreSQL 作为生产数据库，MySQL/H2 可选
- **生产建议**：启用 HTTPS（Nginx/Caddy 反向代理）、强密码策略、定期更新镜像、IP 白名单保护管理端口

## 关联连接
- [[RedHat]] — Keycloak 的维护方
- [[SSO]] — 单点登录概念
- [[OIDC]] — OpenID Connect 协议
- [[SAML]] — 安全断言标记语言
- [[OAuth2]] — 授权框架
- [[Docker]] — 部署工具
- [[Nginx]] — 推荐的反向代理
- [[PostgreSQL]] — 推荐的生产数据库
- [[摘要-Docker部署Keycloak]] — 来源
