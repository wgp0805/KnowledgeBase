---
title: "摘要-oauth2-第三方登录"
type: source
tags: [来源, OAuth2, 第三方登录, 认证, 授权]
sources: [raw/01-articles/搞定 OAuth 2.0 第三方登录，So Easy !.md]
last_updated: 2026-09-16
---

## 核心摘要
犬小哈基于「小哈学Java」整理的 OAuth 2.0 第三方登录完整教程：从协议基础（RFC 6749）讲起，覆盖四大授权模式（授权码/隐藏式/密码/客户端凭证）、三方登录数据库三种设计思路（直接注册/映射表/oauth 表），并给出 GitHub 与 QQ 两种第三方登录的完整 Java 代码实战。核心洞察：客户端不接触用户密码，token 短寿命可封装；但 OAuth 本身不告诉你任何用户信息，只是授权协议。

## 提炼要点
- **四角色模型**：Resource Owner（资源拥有者）/ Resource Server（资源服务器）/ Client（客户端）/ Authorization Server（认证服务器）
- **四大授权模式对比**：
  - **Authorization Code（授权码）**：正宗模式，用户先授权拿到 code 再换 token，最安全
  - **Implicit（隐藏式）**：直接拿 token，跳过 code，适合 SPA
  - **Password（密码）**：客户端拿用户名密码换 token，仅高信任场景
  - **Client Credentials（客户端凭证）**：仅 client_id/secret 换 token，无需用户授权
- **OAuth 三大特点**：简单（易理解易使用）、安全（不涉及用户密钥）、开放（任何服务商可接入）
- **三大应用场景**：原生 app 授权、前后端分离单页面应用、第三方登录
- **OAuth 优缺点**：优点是资源服务器与授权服务器解耦、集中式授权、HTTP/JSON 友好；缺点是协议框架太宽泛导致实现兼容性差、本身不提供用户信息
- **数据库设计三方案**：直接注册到 user 表 / 增加映射表（多登录方式映射到注册 id）/ 建立独立 oauth 表（一对一多关系，每个第三方 openid 一列）
- **GitHub 登录流程**：注册 OAuth App → 生成 state 防 CSRF → 用户跳转授权 → 回调拿 code → 换 access_token → 用 token 调 `/user` 接口
- **QQ 登录流程**：申请接入 → 生成 state → 授权拿 code → 换 token（有效期 30 天）→ 拿 openid → 调 `get_user_info` 取用户信息；QQ 需实名认证和备案域名

## 记忆口诀
OAuth 是授权非认证，四大角色三模式，客户端不碰密码，token 换到就是金。

## 关联连接
- [[OAuth2]] — 核心概念
- [[GitHub]] — 实战示例之一
- [[QQ互联]] — 实战示例之二
- [[State-CSRF防护]] — CSRF 防护机制
- [[SSO]] — 关联的单点登录概念
- [[CAS协议]] — 对比的认证协议
- [[JWT]] — Token 机制
- [[摘要-sso-single-sign-on]] — 相关来源
- [[小哈]] — 作者