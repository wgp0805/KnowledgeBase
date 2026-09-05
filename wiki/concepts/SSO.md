---
title: "SSO"
type: concept
tags: [认证, 单点登录, 安全]
sources: [raw/09-archive/公司系统太多，能不能实现账号互通？.md, raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 定义
SSO（Single Sign-On）即单点登录，是一种身份认证机制，允许用户只需登录一次，即可进入多个相互信任的系统，而不需要重新登录。

## 关键信息
- **产生背景**：企业系统矩阵丰富时，用户在不同系统间来回切换体验差，增加密码管理成本
- **核心思想**：通过一个 ticket 进行串接各系统间的用户信息
- **技术实现**：需要专门的登录域名（如 oauth.com）提供所有系统的 sessionId
- **Cookie 限制**：不同域名的系统无法共享 cookie，因此需要中心化的认证服务
- **CAS 实现**：CAS 是 SSO 的主流实现框架，基于票据验证机制
- **与 Session 的关系**：SSO 解决的是跨系统的身份认证，Session 是单系统内的会话管理

## 关联连接
- [[CAS协议]] — SSO 的主流实现框架
- [[Session]] — 单系统内会话管理
- [[Cookie]] — 客户端状态存储（受域名限制）
- [[OAuth2]] — 三方授权协议，与 SSO 互补
- [[OIDC]] — 基于 OAuth2 的身份认证协议
- [[SAML]] — 基于 XML 的企业级 SSO 协议
- [[Keycloak]] — Red Hat 企业身份认证平台（SSO/IdP）
- [[摘要-sso-single-sign-on]] — 来源
- [[摘要-Docker部署Keycloak]] — 来源（Keycloak 企业部署）
