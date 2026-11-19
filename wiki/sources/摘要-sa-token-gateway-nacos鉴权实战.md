---
title: "摘要-sa-token-gateway-nacos鉴权实战"
type: source
tags: [来源, 权限认证, 微服务, 网关, Sa-Token]
sources: [raw/09-archive/告别SpringSecurity！Sa-Token+Gateway+Nacos极简鉴权实战.md]
last_updated: 2026-11-19
---

## 核心摘要
IT码徒 2026-11-16 文章（源自掘金），实战讲解如何用轻量级权限认证框架 [[Sa-Token]] 替代配置繁琐的 [[SpringSecurity]]，在 [[SpringCloudGateway]] + [[Nacos]] 微服务架构下实现极简认证与鉴权。核心思路：account 服务用 `StpUtil.login()` 一行代码生成 Token 凭证与 Session；gateway 注册 `SaReactorFilter` 全局过滤器拦截全部路由做登录校验，再通过实现 `StpInterface` 接口 + RBAC 五表模型实现精确到 path 的细粒度权限校验，角色/权限数据经 Redis 缓存 + Feign RPC 回源。

## 关键要点
- **动机**：Spring Security 太重、配置项繁多难懂；自研 token 生成/校验/刷新/权限分配工作量大；Sa-Token 用 `StpUtil.login(Object id)` 一个方法完成登录
- **Session 模式 vs JWT**：Sa-Token session 模式需要 Redis 存储会话并在微服务间同步；JWT 无状态无需 Redis 但刷新 token 机制要自己实现，作者选 session 模式（刷新开箱即用、功能更多）
- **配置要点**：`token-name` 自定义 token 名称（默认 satoken）、`token-prefix: Bearer` 前缀（前端 header 需带 "Bearer " 空格）、`is-concurrent`/`is-share` 控制多端登录
- **网关鉴权**：`SaReactorFilter.addInclude("/**")` 拦截全部路径，`SaRouter.match("/**", "/account/user/doLogin", r -> StpUtil.checkLogin())` 放行登录接口白名单
- **RBAC 细粒度鉴权**：用户-角色-权限五表模型；网关实现 `StpInterface.getPermissionList()/getRoleList()`，先查 Redis（TokenSession 中的 ROLES/PERMS），未命中走 Feign 调 account 服务
- **WebFlux 响应式坑**：gateway 基于 WebFlux 不允许阻塞调用，Feign 同步调用需用 `CompletableFuture.supplyAsync` + 自定义线程池包装（方式一）；或改用响应式 `WebClient` + `@LoadBalanced` 走 Nacos 服务发现（方式二）；`HttpMessageConverters` 需手动配置 Bean
- **权限写回 TokenSession**：account 服务查到角色/权限后，通过 `StpUtil.getTokenValueByLoginId(userId)` 反查 token 并把结果写入 Redis 的 TokenSession，供网关直接读取，无权限用户写入空串防穿透

## 关联连接
- [[Sa-Token]] — 核心框架
- [[SpringSecurity]] — 被替代的重型方案
- [[SpringCloudGateway]] — 网关层（WebFlux 响应式）
- [[Nacos]] — 服务发现
- [[Redis]] — Session 存储与权限缓存
- [[rbac]] — 权限模型（五表设计）
- [[微服务]] — 架构场景
- [[IT码徒]] — 来源公众号
