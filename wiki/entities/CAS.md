---
title: "CAS"
type: entity
tags: [SSO, 认证, 开源项目, Yale]
sources: [raw/09-archive/2026-10-31 - 我司用了 5 年的单点登录方案！从实现到部署实战详解，稳的一批!.md]
last_updated: 2026-11-02
---

## 定义

CAS（Central Authentication Service）是 Yale 大学发起的开源项目（2004 年 12 月成为 JA-SIG 项目），为企业级 Web 应用提供可靠的单点登录解决方案。CAS Server 为需要独立部署的 Web 应用，CAS Client 支持 Java、.Net、PHP、Perl、Apache、uPortal、Ruby 等多种客户端。

## 关键信息

### 架构组成

- **CAS Server**：独立部署的认证中心，负责用户认证与 Ticket 签发
- **CAS Client**：部署在各个业务系统中，拦截请求并重定向到 CAS Server 认证

### 标准过滤器链（Spring Boot 集成）

| 顺序 | 过滤器 | 作用 |
|------|--------|------|
| Order 0 | `SingleSignOutFilter` | 单点登出，放在最前 |
| Order 1 | `IgnoreSSLValidateFilter`（自定义） | 忽略 SSL 校验 |
| Order 2 | `MyAuthenticationFilter`（自定义重写） | 用户认证，核心改造点 |
| Order 3 | `Cas20ProxyReceivingTicketValidationFilter` | Ticket 校验 |
| Order 4 | `CharacterEncodingFilter` | 设置 UTF-8 编码 |
| Order 6 | `HttpServletRequestWrapperFilter` | 请求包装 |

### 前后端分离适配（核心改造）

AJAX 请求拿不到 302 重定向，前端 Vue 的 response 拦截器拦不到。改造方法：重写 `AuthenticationFilter.doFilter()`，检测 `x-requested-with: XMLHttpRequest`，AJAX 请求直接返回 JSON `{"code":202}`，前端收到后自行跳转 CAS 登录页。

### 与其他 SSO 方案的对比

- **CAS**：票据验证机制，适合统一账号密码身份认证
- **JWT**：所有服务靠约定生成 token，或集中生成集中判断
- **OAuth2**：授权第三方服务使用我方资源

## 关联连接
- [[CAS协议]] — 协议概念
- [[SSO]] — 单点登录概念
- [[摘要-cas-前后端分离单点登录]] — 来源
- [[SpringSecurity]] — 常与 CAS 集成的认证框架
- [[小哈]] — 文章作者
