---
title: "摘要-Docker部署Keycloak"
type: source
tags: [认证, Docker, Keycloak, 企业级, SSO]
sources: [raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 核心摘要
使用 Docker 部署 Keycloak 企业级身份认证平台的完整指南。Keycloak 是 Red Hat 出品的企业级身份认证平台，支持 OAuth2/OIDC/SAML/SSO，开箱即用。部署流程：准备 MySQL 或 PostgreSQL 数据库 → 编写 Docker Compose 配置 → 启动服务。生产环境建议使用 Nginx 反向代理启用 HTTPS，定期更新镜像、配置强密码策略和保护管理员账号。常见问题涵盖 HTTPS required 错误、登录跳转失败、忘记管理员密码和社交登录配置失败。

## 关联连接
- [[Keycloak]] — Red Hat 企业级身份认证平台
- [[SSO]] — 单点登录概念
- [[OIDC]] — OpenID Connect 认证协议
- [[SAML]] — 安全断言标记语言
- [[OAuth2]] — 授权协议
- [[Docker]] — 部署工具
- [[Nginx]] — 反向代理
- [[Let's Encrypt]] — 免费 SSL 证书
- [[PostgreSQL]] — 推荐的 Keycloak 数据库
- [[MySQL]] — 备选 Keycloak 数据库
