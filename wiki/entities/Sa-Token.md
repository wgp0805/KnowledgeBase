---
title: "Sa-Token"
type: entity
tags: [权限认证, Java框架, 开源]
sources: [raw/09-archive/为什么越来越多人用Sa-Token？.md, raw/09-archive/告别SpringSecurity！Sa-Token+Gateway+Nacos极简鉴权实战.md]
last_updated: 2026-11-19
---

## 定义
Sa-Token 是一个轻量级 Java 权限认证框架，专注于简化登录认证、权限授权、Session 会话等安全功能，是 Spring Security 和 Shiro 的轻量替代方案。

## 关键信息
- **GitHub Stars**：超过 46K，中文社区迅速崛起
- **最新版本**：v1.45.0（2026年3月），全面适配 Spring Boot 4
- **核心定位**：轻量级权限认证框架，聚焦高频认证场景
- **架构模式**：核心-插件-适配器（Core-Plugin-Adapter）模型
- **学习曲线**：极低，`StpUtil.login()` 一行代码即可上手
- **配置方式**：零配置启动

### 核心架构
- **核心层（sa-token-core）**：零外部依赖，只包含最纯粹的认证逻辑、Session 模型和 SPI 接口定义
- **插件层（sa-token-plugin）**：可插拔功能扩展（Redis 存储、JWT、SSO、OAuth2.0 等）
- **适配层（sa-token-starter）**：桥接到具体 Web 框架（Spring Boot、WebFlux、Solon、JFinal 等）

### 核心组件
- **SaManager**：全局组件注册中心，持有所有全局组件的静态引用
- **SaStrategy**：策略模式核心，允许在不修改核心代码的情况下覆盖内部算法
- **StpUtil**：静态工具类，提供登录、注销、权限检查等一行代码操作

### 核心功能
- **登录认证**：`StpUtil.login(id)` 一行代码完成登录
- **权限控制**：RBAC + 按钮级 + 路由拦截
- **分布式会话**：原生支持 Redis 扩展
- **多账号体系**：通过自定义 StpLogic 实现隔离
- **踢人下线**：框架层面直接拦截
- **Token 生成**：自动注入 Cookie，前端无感知

### 适用场景
- Spring Boot 新项目（强烈推荐）
- 从 Spring Security 迁移（强烈推荐）
- 需要快速交付的项目（强烈推荐）
- 微服务架构（强烈推荐）
- 多端登录策略复杂（强烈推荐）
- 团队对安全不熟悉（强烈推荐）

### 缺点
- 生态不如 Spring Security 成熟
- 功能边界相对聚焦（无 CSRF 保护等复杂安全防护）
- 部分高级功能需要额外配置（JWT、SSO、OAuth2 等）

### Gateway+Nacos 微服务网关鉴权实战（2026-11-16，详见 [[摘要-sa-token-gateway-nacos鉴权实战]]）
- **一行登录**：account 服务 `StpUtil.login(user.getId())` 生成 Token 凭证与 Session 会话；`StpUtil.getSession().set("USER_DATA", user)` 附加会话数据
- **Session 模式选型**：session 模式需 [[Redis]] 存储会话（`sa-token-dao-redis-jackson`）并在微服务间同步，但 token 刷新开箱即用；JWT 无状态无需 Redis 但刷新机制要自己实现——作者选 session 模式
- **网关全局过滤器**：`SaReactorFilter`（`sa-token-reactor-spring-boot-starter`）`addInclude("/**")` 拦截全部路径，`SaRouter.match("/**", "/account/user/doLogin", r -> StpUtil.checkLogin())` 放行登录白名单；`setError` 统一异常返回
- **配置细节**：`token-name` 自定义 token 名（默认 satoken）；`token-prefix: Bearer` 后前端 header 须传 "Bearer <token>"（注意空格，需与前端约定）；`is-concurrent`/`is-share` 控制多端登录与 token 共享
- **RBAC 细粒度鉴权（精确到 path）**：用户-角色-权限五表模型，网关实现 `StpInterface.getPermissionList()/getRoleList()`；数据流：优先读 TokenSession 缓存（account 服务查完角色/权限后通过 `StpUtil.getTokenValueByLoginId(userId)` 反查 token 写回 Redis），未命中走 Feign 调 account 服务回源；无权限用户写空串防穿透
- **WebFlux 三个坑**：① gateway 基于 WebFlux 禁止阻塞调用——Feign 同步调用需 `CompletableFuture.supplyAsync` + 自定义线程池包装（勿用默认 ForkJoinPool）；② `HttpMessageConverters` 不自动注入，需手动 `@Bean` 配置；③ 更彻底的方案是响应式 `WebClient` + `@LoadBalanced` 走 Nacos 服务发现

## 关联连接
- [[SpringSecurity]] — 对比框架
- [[Shiro]] — 另一个对比框架
- [[权限认证框架]] — 核心概念
- [[分布式会话]] — 关键功能
- [[核心-插件-适配器模型]] — 架构设计
- [[摘要-为什么越来越多人用Sa-Token]] — 来源
- [[sa-token-vs-jwt-spring-security]] — 选型对比
- [[RuoYi]] — 使用 Sa-Token 的典型项目
- [[摘要-sa-token-gateway-nacos鉴权实战]] — 来源（Gateway+Nacos 网关鉴权实战）
- [[SpringCloudGateway]] — 实战的网关层（WebFlux）
- [[Nacos]] — 实战的服务发现
- [[rbac]] — 网关鉴权用的权限模型（五表设计）
