---
title: "OpenFeign"
type: entity
tags: [SpringCloud, HTTP客户端, 服务调用]
sources: [raw/01-articles/全链路灰度发布：从"灰飞烟灭"到"稳如老狗"，我只用了这8步！！.md]
last_updated: 2026-06-09
---

## 定义
OpenFeign 是 Spring Cloud 生态中的声明式 HTTP 客户端，允许开发者通过 Java 接口 + 注解定义远程服务调用，屏蔽底层 HTTP 实现细节。早期称为 Feign，Spring Cloud 将其封装为 OpenFeign 并集成负载均衡能力。

## 关键信息
- 声明式调用：`@FeignClient(name = "service-name")` 定义远程服务
- 负载均衡：集成 Spring Cloud LoadBalancer（替代已停维的 Ribbon）
- 拦截器机制：自定义 `RequestInterceptor` 可在请求发送前统一处理（如灰度标记传递）
- 灰度传递实践：通过 `RequestContextHolder.getRequestAttributes()` 获取当前 HTTP 请求，提取 `X-Gray` 头并设置到 Feign 请求中

## 关联连接
- [[摘要-全链路灰度发布-8步实战教程]] — 灰度标记传递
- [[microservices]] — 微服务间调用
- [[grayscale-release]] — 全链路灰度发布
- [[SpringCloudGateway]] — API 网关入口
