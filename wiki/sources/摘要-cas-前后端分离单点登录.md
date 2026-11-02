---
title: "摘要-cas-前后端分离单点登录"
type: source
tags: [来源, CAS, SSO, SpringBoot, 前后端分离]
sources: [raw/01-articles/2026-10-31 - 我司用了 5 年的单点登录方案！从实现到部署实战详解，稳的一批!.md]
last_updated: 2026-11-02
---

## 核心摘要

「Java学习者社区 / 小哈学Java」介绍一套生产使用 5 年的 CAS 单点登录方案，原文来自 CSDN。文章重点解决**前后端分离场景下 CAS 无法重定向**的问题：AJAX 请求拿不到 302，前端 Vue 的 response 拦截器拦不到重定向，于是重写 CAS 源码过滤器。

标准 CAS 客户端过滤器链（按 `@Order` 排序）：

1. `SingleSignOutFilter`（Order 0）— 单点登出
2. `IgnoreSSLValidateFilter`（Order 1，自定义）— 忽略 SSL 校验
3. `MyAuthenticationFilter`（Order 2，自定义重写）— 用户认证
4. `Cas20ProxyReceivingTicketValidationFilter`（Order 3）— Ticket 校验
5. `CharacterEncodingFilter`（Order 4）— UTF-8
6. `HttpServletRequestWrapperFilter`（Order 6）— 请求包装

**核心改造**：`MyAuthenticationFilter` 重写 `AuthenticationFilter.doFilter()`，检测请求头 `x-requested-with: XMLHttpRequest`。若是 AJAX 请求，直接返回 JSON `{"code":202, "msg":"no ticket and no assertion found"}`；非 AJAX 才走正常重定向到 CAS 登录页。前端拦截器收到 `code === 202` 时，自己 `window.location.href` 跳转到后端 `checkTicket` 接口，由后端 `response.sendRedirect` 到前端页面地址。

踩坑记录：

- 证书导入 JDK 必须精确到 `cacerts` 文件，否则报拒绝写入，最好用管理员命令窗口
- 配置地址全用 IP，用 hosts 映射可能出问题
- `casValidationServerUrlPrefix` 要用内网 IP

方案总结里还提到 SSO 的其他实现路线：JWT（所有服务靠约定生成 token，或集中生成集中判断）、OAuth2。

## 关联连接
- [[CAS协议]] — 协议概念
- [[SSO]] — 单点登录概念
- [[SpringBoot]] — 承载框架
- [[FilterRegistrationBean]] — 过滤器注册机制
- [[摘要-sso-single-sign-on]] — 另一篇 SSO 来源
- [[小哈]] — 文章作者
