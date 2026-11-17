---
title: "distributed-tracing"
type: concept
tags: [可观测性, APM, 分布式, 架构]
sources: [raw/09-archive/2026-07-21-分布式链路追踪系统之二进制安装skywalking - Linux-1874.md, raw/09-archive/2026-11-16 - SpringBoot集成Hera，让日志查看从“找罪证”变“查答案”！.md]
last_updated: 2026-11-17
---

## 定义
分布式链路追踪（Distributed Tracing）是一种跟踪请求在分布式系统中完整路径的可观测性技术，能够监控和诊断微服务架构中的性能瓶颈和异常。

## 关键信息
- **核心能力**：追踪请求跨服务的完整调用链路、记录每个节点的耗时和状态
- **代表产品**：SkyWalking、Zipkin、Jaeger
- **核心组件**：OAP（可观测性分析平台）、UI（前端展示）、存储后端

### 日志侧的 TraceId 检索实践
来自 [[摘要-日志分析命令组合拳]]。在没有接入 APM 平台前，TraceId 依然要在日志里手动串联：微服务用 TraceId 串联请求，而日志文件会滚动（Rolling）成 app.log、app.log.1、app.log.2，因此需要按通配符跨文件搜索，例如 grep "TraceId-20251219001" logs/app.log*。这条命令的价值在于把 APM 平台"请求走过的路径"退化成一串可检索的日志坐标——接入 SkyWalking 前后，TraceId 都是排查的第一入口。

### 请求头透传式日志串联（Hera 实践，2026-11-16）
[[Hera]] 用 `X-Hera-Trace-Id` 请求头做跨服务日志串联：开启 hera.trace 后 SpringBoot 应用自动在 HTTP 头中传递链路 ID，控制台输入一个 traceId 即可看到订单/支付等多个服务的完整日志链路。工程要点：**各服务 trace-id-header 配置必须一致，且网关层必须透传该头**，否则链路断；高并发下可调低采样率（如 0.5）控制损耗。这与 SkyWalking 一类 APM 的自动埋点互为补充——不接 APM 时，"请求头 + 日志字段"是最轻量的链路串联方案（详见 [[摘要-springboot集成hera日志平台]]）。

## 关联连接
- [[SkyWalking]] — Apache 开源链路追踪系统
- [[Elasticsearch]] — 常用存储后端
- [[Hera]] — 请求头透传式 traceId 日志串联实践
- [[摘要-skywalking-install]] — 来源
- [[摘要-日志分析命令组合拳]] — 来源（TraceId 日志检索实践）
- [[摘要-springboot集成hera日志平台]] — 来源（Hera 请求头串联实践）
- [[日志分析]] — 日志侧排查方法论
- [[grep]] — 跨滚动文件搜索 TraceId
