---
title: "SAML"
type: concept
tags: [认证, SSO, 企业级, 安全断言]
sources: [raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 定义
SAML（Security Assertion Markup Language）是一种基于 XML 的安全断言标记语言，用于在身份提供商（IdP）和服务提供商（SP）之间交换认证和授权数据，是企业级 SSO 的主流协议之一。

## 关键信息
- **定位**：企业级跨域单点登录标准协议，基于 XML 格式
- **核心组件**：
  - IdP（Identity Provider）：身份提供商，负责认证用户
  - SP（Service Provider）：服务提供商，依赖 IdP 认证结果
  - Assertion：SAML 断言，包含认证/属性/授权信息
- **消息流**：用户访问 SP → SP 重定向到 IdP → IdP 认证 → 返回 SAML Assertion → SP 建立本地会话
- **与 OIDC 对比**：SAML 偏企业级（XML/重客户端），OIDC 偏互联网（JSON/轻量/原生支持移动端）
- **与 Keycloak 的关系**：Keycloak 原生支持 SAML，可作为 IdP

## 关联连接
- [[SSO]] — SAML 实现的单点登录
- [[OIDC]] — 现代替代协议
- [[OAuth2]] — 授权协议
- [[Keycloak]] — 支持 SAML 的企业身份平台
- [[摘要-Docker部署Keycloak]] — 来源
