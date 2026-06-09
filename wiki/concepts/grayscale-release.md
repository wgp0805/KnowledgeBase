---
title: "grayscale-release"
type: concept
tags: [部署策略, 微服务, 发布流程]
sources: [raw/01-articles/全链路灰度发布：从"灰飞烟灭"到"稳如老狗"，我只用了这8步！！.md]
last_updated: 2026-06-09
---

## 定义
灰度发布（Grayscale/Canary Release）是一种渐进的软件部署策略，将新版本先部署到少量节点（灰度节点），引导小部分流量验证，确认稳定后再逐步全量推广。全链路灰度发布则要求灰度标识在网关→上游服务→下游服务的整条调用链中一致传递，确保灰度流量全程只走灰度节点。

## 关键信息
- 与蓝绿部署不同：灰度是渐进式切流，蓝绿是两套环境瞬间切换
- 核心挑战：灰度标记在分布式调用链中不丢失、不透传
- 技术栈选型（安全版本）：Spring Cloud 2022.0.3 + Spring Cloud Alibaba 2022.0.0.0-RC2 + Nacos 2.2.3 + Spring Cloud Gateway 3.1.3

### 8步实施路线
1. **Nacos 命名空间隔离**：创建 prod-namespace 和 gray-namespace 两个命名空间，通过 `service.gray.tag` 标记节点身份
2. **网关灰度过滤器**：实现 AbstractGatewayFilterFactory，识别请求头 `X-Gray` 并标准化为 `X-Gray: true/false`
3. **服务间标记传递**：通过 Feign 自定义 RequestInterceptor 透传 `X-Gray` 头
4. **自定义负载均衡**：实现 ReactiveLoadBalancer，按灰度标记匹配对应节点
5. **测试验证**：分不带标记（走生产）和带 `X-Gray:1` 头（走灰度）两种场景
6. **监控告警**：Prometheus + Grafana 监控灰度服务 QPS/响应时间/错误率
7. **一键回滚**：注释网关过滤器 + Nacos 下线灰度服务
8. **比例控制**：网关层随机数判断，逐步放流（如 10%）

### 常见踩坑点
- 网关切了灰度，但服务间调用走默认轮询负载均衡，请求打到生产节点
- Nacos 命名空间混用，灰度服务注册后生产服务拿到双倍节点
- Feign 调用时未透传 `X-Gray` 头，下游无感知
- 服务元数据中 `service.gray.tag` 未配置，负载均衡无法区分节点

## 关联连接
- [[摘要-全链路灰度发布-8步实战教程]] — 来源
- [[microservices]] — 微服务架构
- [[Nacos]] — 命名空间隔离
- [[SpringCloudGateway]] — 网关灰度过滤
- [[OpenFeign]] — 灰度标记传递
- [[gray-tag-propagation]] — 标记传播机制
