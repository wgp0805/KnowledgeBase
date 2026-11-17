---
title: "Hera"
type: entity
tags: [日志平台, 可观测性, SpringBoot, 分布式]
sources: [raw/09-archive/2026-11-16 - SpringBoot集成Hera，让日志查看从“找罪证”变“查答案”！.md]
last_updated: 2026-11-17
---

## 定义
Hera 是一套面向分布式系统的日志平台（文中推荐 2.5+ 版本，支持 SpringBoot 2.x/3.x），定位不是"换一个日志查看工具"，而是"分布式系统可观测性的基础设施建设"：以 SpringBoot starter 无侵入集成为主，打通"日志采集—传输—存储—分析—交互"完整链路，提供业务标签聚合、traceId 全链路串联与按业务重要性分级存储能力。

## 关键信息

### 解决的三大传统日志死穴
1. **日志分散、缺业务维度聚合**：本地文件要逐台登录查看；ELK 支持检索但查"某用户的下单日志"要拼用户 ID/订单号多个条件——Hera 可按业务标签（businessType/env/userId 等）直接筛选
2. **链路断裂**：请求跨网关/服务 A/服务 B/数据库却没有统一链路 ID，排查靠"东拼西凑"（文中案例：支付超时问题排查 4 小时才发现中间件连接池耗尽）
3. **存储成本两难**：全量存储成本高（案例：电商平台为存全年日志每年多花 200 万），抽样存储易丢关键信息；Hera 按业务重要性分级存储（核心业务 30 天、非核心 7 天），节省 60% 存储成本

### 五层架构
- **采集层**：Hera Agent 嵌入 SpringBoot 应用，无侵入采集，支持自定义字段（链路 ID/用户 ID/业务标签）
- **平台层**：日志清洗、字段解析、按业务规则路由存储
- **存储层**：核心日志存 [[Elasticsearch]]（快速检索），归档日志存 HDFS（降成本）
- **分析层**：全文检索、链路追踪、日志聚合统计
- **交互层**：Web 控制台 + OpenAPI

### SpringBoot 集成要点
- **依赖**：`com.hera:hera-log-spring-boot-starter` + `hera-trace-spring-boot-starter`（2.5.3）
- **配置**：agent-address 多节点逗号分隔；level 生产建议 WARN+；custom-fields 支持 key/value 与 key/value-provider 两种——userId 用 `HeraCustomFieldProvider` 实现类从 ThreadLocal 的 UserContext 取当前登录用户（需 @Component 注册，返回值不能为 null）
- **无侵入**：原有 SLF4J/Logback 日志代码零改造，输出自动携带 custom-fields 与 traceId
- **链路追踪**：hera.trace.enabled + sampling-rate（生产高并发可设 0.5 控损耗）+ trace-id-header（默认 `X-Hera-Trace-Id`），HTTP 请求头跨服务自动传递，控制台输入一个 traceId 看多服务完整日志链路（文中口径：跨服务排查效率至少提升 5 倍）
- **控制台三步定位**：筛服务与环境 → 业务字段检索（userId/orderNo）→ 点 traceId 看链路/点"堆栈"看完整异常堆栈；另支持日志聚合统计趋势图定位异常峰值

### 性能、高可用与安全
- **性能**：异步采集（async-queue-size 默认 512，可调 2048）、日志分级（生产收紧到 WARN）、批量传输（batch-size 默认 50，可调 100）
- **高可用**：Agent 集群多地址防单点；Agent 不可用时日志落本地缓存（默认 /tmp/hera/log/cache）恢复后自动补发；存储分级（ES 7 天快速检索 + HDFS 30 天归档，非核心直接进 HDFS）
- **安全**：mask-fields 字段脱敏（手机号/身份证号）、按"服务+环境"配置查看权限（开发只看测试、生产仅运维与架构师）、操作审计（记录所有查看/导出）

### 避坑三则
1. 自定义字段缺失 → value-provider 实现类没加 @Component 或方法返回 null
2. 跨服务链路失效 → 各服务 trace-id-header 配置不一致，或网关层没透传 X-Hera-Trace-Id 头
3. 采集性能损耗高 → 降日志级别、扩异步队列、用 [[Arthas]] 查看 Hera Agent 线程 CPU 占用

### 效果口径（文中案例）
- 平均排障时间 2 小时 → 15 分钟；日志存储成本节省 60%；分布式系统"黑盒变白盒"

## 关联连接
- [[摘要-springboot集成hera日志平台]] — 来源
- [[SpringBoot]] — 集成框架（starter 无侵入接入）
- [[ELK日志系统]] — 传统对照方案（强通用检索、弱业务维度聚合）
- [[可观测性]] — 上位能力域（日志/指标/追踪三支柱）
- [[distributed-tracing]] — traceId 全链路串联的同域概念
- [[Elasticsearch]] — 核心日志检索存储
- [[ThreadLocal]] — userId 自定义字段的取值来源
