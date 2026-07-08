---
title: "SpringCloudGateway"
type: entity
tags: [SpringCloud, 网关, 微服务]
sources: [raw/01-articles/面试官：为什么需要 Gateway 网关，它有什么作用？.md]
last_updated: 2026-07-08
---

## 定义
Spring Cloud Gateway 是 Spring Cloud 生态中的 API 网关组件，基于 Spring WebFlux 和 Reactor 构建，提供路由转发、负载均衡、限流、鉴权等横切关注点。

## 关键信息
- 基于 WebFlux：响应式、非阻塞、高性能
- 核心概念：Route（路由）、Predicate（断言）、Filter（过滤器）
- 限流：支持 RequestRateLimiter（基于 Redis + 令牌桶）
- 集成服务发现：与 Nacos、Eureka 等注册中心集成
- 替代 Zuul：Spring Cloud 官方推荐的网关方案
- 全局过滤器：GlobalFilter 处理跨切面逻辑（鉴权、日志等）
- 灰度发布：通过自定义 `AbstractGatewayFilterFactory` 识别 `X-Gray` 请求头，实现灰度流量标记与隔离
- 灰度比例控制：在网关过滤器中使用随机数按比例放行流量（如 10%），支持渐进式灰度

### War 包部署外置 Tomcat（技术探索）
Spring Cloud Gateway 官方设计上以 jar 包 + 内嵌 Netty 运行，不支持 War 包外置 Servlet 容器部署。但在传统企业环境中存在强依赖外置 Tomcat 的需求。社区探索了一套改造方案：

- **核心思路**：自定义 WebApplicationInitializer，用 SpringApplication.run() 启动上下文，通过空壳 ReactiveWebServerFactory 排除内嵌 Netty 冲突
- **Context-Path 修复**：AOP 切面修改 ServerWebExchange 的 Path，去掉 context-path 前缀
- **可正常工作**：基础路由转发、断言匹配、GlobalFilter、Nacos 动态路由刷新
- **致命短板**：
  - IO 模型冲突：外层 Tomcat 阻塞线程池 + 内层 Netty 非阻塞 Reactor → 吞吐量暴跌，QPS 下降 50% 以上
  - NettyRoutingFilter 长链接复用异常、限流计数不准、灰度路由高并发匹配异常
  - 健康探针错乱、Actuator 指标丢失、句柄泄漏
  - 官方不支持，版本升级后改造代码大概率失效
- **结论**：理论可行但生产不推荐。建议用原生 jar 包或 spring-cloud-starter-gateway-mvc（官方 Servlet 版）

### 网关五大核心作用
网关是微服务系统的统一入口，将横切关注点集中管理：

| 作用 | 说明 | 对应技术 |
| --- | --- | --- |
| 路由转发 | 根据请求路径将请求转发到对应微服务 | Predicate + Route |
| 身份认证 | 统一校验 Token、权限，不用每个服务都鉴权 | GlobalFilter |
| 限流熔断 | 保护后端服务不被突发流量压垮 | Sentinel / RequestRateLimiter |
| 日志监控 | 统一记录请求日志、响应时间、状态码 | GlobalFilter |
| 协议转换 | 外部 HTTP → 内部 RPC，或反向 | 自定义 Filter |

记忆口诀：路由、鉴权、限流、日志、协议转换。

### Route / Predicate / Filter 三核心概念
- **Route（路由）**：一条转发规则，包含 ID、目标 URI、一组断言和一组过滤器。`lb://` 前缀表示启用负载均衡，后面是注册中心服务名
- **Predicate（断言）**：匹配条件，Path 和 Method 都满足才走该路由
- **Filter（过滤器）**：分为 Pre（前置）和 Post（后置），在请求转发前和响应返回后执行自定义逻辑。`GlobalFilter` 对所有路由生效，`GatewayFilter` 只对配置了的路由生效

完整链路：请求进来 → 遍历所有 Route → Predicate 匹配 → Pre Filter → 转发到目标服务 → Post Filter → 返回响应。

### Gateway vs Zuul 对比

| 对比维度 | Zuul 1.x | Spring Cloud Gateway |
| --- | --- | --- |
| 编程模型 | 同步阻塞（Servlet） | 异步非阻塞（WebFlux + Netty） |
| 性能 | 一般，线程池模型 | 高性能，少量线程处理大量并发 |
| filter 种类 | pre / route / post / error | pre / post（更简洁） |
| 限流支持 | 需额外集成 | 内置 RequestRateLimiter |
| Spring 官方支持 | 已弃用 | 官方推荐 |

核心区别：Gateway 基于响应式编程（Reactor + Netty），异步非阻塞，性能远超 Zuul 1.x 的同步阻塞模型。Zuul 已不在 Spring Cloud 官方路线图内。

### 自定义全局鉴权过滤器
实现 `GlobalFilter` + `Ordered` 接口，所有路由都会经过该过滤器；`getOrder()` 返回值越小优先级越高。典型实现：从请求头获取 Token → 空则返回 401 → JWT 校验 → 将用户信息放入请求头传递给下游服务。

## 关联连接
- [[Nacos]] — 服务注册与发现，lb:// 前缀获取服务实例
- [[SpringBoot]] — 基础框架
- [[microservices]] — 微服务架构
- [[Sentinel]] — 限流熔断配合使用
- [[grayscale-release]] — 全链路灰度发布网关环节
- [[Tomcat]] — 外置 Servlet 容器
- [[Zuul]] — 已被替代的 Netflix 网关
- [[网关]] — 网关概念与五大职责
- [[JWT]] — 鉴权过滤器中校验 Token
- [[Redis]] — RequestRateLimiter 令牌桶依赖
- [[cors]] — 跨域可在网关统一处理
- [[rbac]] — 权限模型与网关鉴权配合
- [[摘要-gateway网关]] — Gateway 五大作用与对比来源
- [[摘要-Spring-Cloud-Gateway-War-Tomcat]] — War 包部署改造来源
