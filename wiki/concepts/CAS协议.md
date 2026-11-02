---
title: "CAS协议"
type: concept
tags: [认证, SSO, 单点登录, 协议]
sources: [raw/09-archive/公司系统太多，能不能实现账号互通？.md, raw/01-articles/2026-10-31 - 我司用了 5 年的单点登录方案！从实现到部署实战详解，稳的一批!.md]
last_updated: 2026-11-02
---

## 定义
CAS（Central Authentication Service）是中央认证服务框架，基于 Kerberos 票据方式实现 SSO 单点登录，为 Web 应用系统提供可靠的单点登录解决方案。Yale 大学发起，2004 年 12 月正式成为 JA-SIG 项目。

## 关键信息

### 核心流程
用户访问业务系统 → 未登录跳转到 CAS 登录页 → 登录成功生成 ticket → 存入 Redis → 重定向回业务系统 → 业务系统用 ticket 查询 Redis 获取 session → 种 cookie 完成登录

### Ticket 机制
CAS 生成唯一票据（UUID），存入 Redis 的数据结构为 `<ticket, sessionid>`。

### 安全边界
CAS 保障的是客户端（CAS 客户端）的用户资源安全，即"用户有没有权限访问我的资源"。

### 与 OAuth2 区别
- CAS：统一账号密码身份认证 → 用 CAS
- OAuth2：授权第三方服务使用我方资源 → 用 OAuth2

### Spring Boot 集成的过滤器链
| 顺序 | 过滤器 | 作用 |
|------|--------|------|
| Order 0 | `SingleSignOutFilter` | 单点登出，放在最前 |
| Order 1 | `IgnoreSSLValidateFilter`（自定义） | 忽略 SSL 校验 |
| Order 2 | `MyAuthenticationFilter`（自定义重写） | 用户认证，核心改造点 |
| Order 3 | `Cas20ProxyReceivingTicketValidationFilter` | Ticket 校验 |
| Order 4 | `CharacterEncodingFilter` | 设置 UTF-8 编码 |
| Order 6 | `HttpServletRequestWrapperFilter` | 请求包装 |

### 前后端分离改造（核心）
**问题**：CAS 源码的 `AuthenticationFilter` 认证失败时直接重定向，但 AJAX 请求拿不到 302，Vue response 拦截器拦不到 302。

**解决**：重写 `AuthenticationFilter.doFilter()`，检测请求头 `x-requested-with: XMLHttpRequest`：
- AJAX 请求：直接返回 JSON `{"code":202, "msg":"no ticket and no assertion found"}`
- 非 AJAX 请求：走正常重定向到 CAS 登录页

前端收到 `code === 202` 时，自行 `window.location.href` 跳转到后端 `checkTicket` 接口，由后端 `response.sendRedirect` 到前端页面地址。

### Demo 实现要点
- 依赖：`cas-client-core:3.3.2` + `spring-security-cas` + `joda-time`
- 配置项：`casServerLoginUrl`、`casServerUrlPrefix`、`serverName`
- 踩坑：证书精确导入 `cacerts`（管理员命令窗口）；地址全用 IP 不用 hosts 映射；验证地址用内网 IP

## 关联连接
- [[SSO]] — 单点登录概念
- [[CAS]] — CAS 实体
- [[Session]] — 传统会话管理机制
- [[OAuth2]] — 三方授权协议，与 CAS 互补
- [[Redis]] — CAS ticket 存储介质
- [[摘要-sso-single-sign-on]] — 早期来源
- [[摘要-cas-前后端分离单点登录]] — 最新来源
