---
title: "Gateway 网关五大作用与 Spring Cloud Gateway 实战"
type: source
tags: [网关, 微服务, SpringCloudGateway, 面试]
sources: [raw/01-articles/面试官：为什么需要 Gateway 网关，它有什么作用？.md]
last_updated: 2026-07-08
---

## 核心摘要

面试导向的 Gateway 网关深度解析文章，核心回答"为什么需要网关"和"网关有什么作用"两个问题。

**网关的本质**：微服务系统的统一入口，将所有非业务逻辑的公共功能集中到一处处理，让各个微服务专注于业务本身。没有网关的微服务架构如同大楼没有大门和前台——每个来访者都可以直接敲任何一扇门。

**网关五大核心作用**：

| 作用 | 说明 | 对应技术 |
| --- | --- | --- |
| 路由转发 | 根据请求路径将请求转发到对应微服务 | Predicate + Route |
| 身份认证 | 统一校验 Token、权限，不用每个服务都鉴权 | GlobalFilter |
| 限流熔断 | 保护后端服务不被突发流量压垮 | Sentinel / RequestRateLimiter |
| 日志监控 | 统一记录请求日志、响应时间、状态码 | GlobalFilter |
| 协议转换 | 外部 HTTP → 内部 RPC，或反向 | 自定义 Filter |

**Spring Cloud Gateway 三核心概念**：
- Route（路由）：包含 ID、目标 URI、一组断言和一组过滤器的转发规则
- Predicate（断言）：匹配条件，Path/Method 等都满足才走该路由
- Filter（过滤器）：Pre（前置）和 Post（后置），执行鉴权、加请求头、记录日志等

完整链路：请求进来 → 遍历 Route → Predicate 匹配 → Pre Filter → 转发到目标服务 → Post Filter → 返回响应。

**Gateway vs Zuul**：Gateway 基于 WebFlux + Netty 异步非阻塞，性能远超 Zuul 1.x 的同步阻塞模型；Zuul 已不在 Spring Cloud 官方路线图内，Gateway 是官方推荐方案。

**面试要点**：自定义 GlobalFilter 实现统一鉴权是必考题，实现 GlobalFilter + Ordered 接口，getOrder() 控制优先级。

## 关联连接
- [[SpringCloudGateway]] — 当前主流 API 网关实现
- [[网关]] — 网关概念定义与五大职责
- [[Zuul]] — 已被替代的 Netflix 网关
- [[Sentinel]] — 限流熔断配合使用
- [[JWT]] — 鉴权过滤器中校验 Token
- [[Nacos]] — lb:// 前缀获取服务实例
- [[Redis]] — RequestRateLimiter 令牌桶依赖
- [[microservices]] — 微服务架构
- [[cors]] — 跨域可在网关统一处理
- [[rbac]] — 权限模型与网关鉴权配合
