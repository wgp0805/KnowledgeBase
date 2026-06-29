---
title: "SpringCloudGateway"
type: entity
tags: [SpringCloud, 网关, 微服务]
sources: []
last_updated: 2026-05-29
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

## 关联连接
- [[Nacos]] — 服务注册与发现
- [[SpringBoot]] — 基础框架
- [[microservices]] — 微服务架构
- [[Sentinel]] — 限流熔断配合使用
- [[grayscale-release]] — 全链路灰度发布网关环节
- [[Tomcat]] — 外置 Servlet 容器
- [[摘要-Spring-Cloud-Gateway-War-Tomcat]] — 来源
