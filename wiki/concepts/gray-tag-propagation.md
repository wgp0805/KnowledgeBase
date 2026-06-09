---
title: "gray-tag-propagation"
type: concept
tags: [灰度发布, 服务调用, 分布式追踪]
sources: [raw/01-articles/全链路灰度发布：从"灰飞烟灭"到"稳如老狗"，我只用了这8步！！.md]
last_updated: 2026-06-09
---

## 定义
灰度标记传递（Gray Tag Propagation）是全链路灰度发布的核心机制，指灰度标识（通常为 `X-Gray: true` 请求头）在网关入口识别后，经过 Feign/HTTP 调用、负载均衡等环节，完整无丢失地传递到调用链中每个微服务的机制。

## 关键信息
- 标记载体：HTTP 请求头 `X-Gray`，标准化值为 `true` 或 `false`
- 传递链路：网关 → 服务A（Feign拦截器读取当前请求头并写入下游请求） → 服务B
- 实现方式：自定义 Feign 的 `RequestInterceptor`，通过 `RequestContextHolder` 获取当前请求的 `X-Gray` 头
- 断线场景：任何环节忘记传递，灰度流量就会误入生产节点

### 传递流程
1. 网关识别：从原始请求读取 `X-Gray: 1`，标准化为 `X-Gray: true`
2. 路由转发：网关将带标记头的请求转发到服务A
3. Feign 传递：服务A调用服务B时，Feign拦截器自动从当前请求上下文提取标记并写入新请求
4. 负载均衡决策：灰度负载均衡器读取请求头的 `X-Gray` 值，匹配到对应灰度节点

## 关联连接
- [[摘要-全链路灰度发布-8步实战教程]] — 来源
- [[grayscale-release]] — 全链路灰度发布
- [[OpenFeign]] — 标记传递实现
- [[microservices]] — 微服务调用链
