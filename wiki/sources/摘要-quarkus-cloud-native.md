---
title: "摘要-quarkus-cloud-native"
type: source
tags: [来源, 原始文件, Quarkus, 云原生, Java, 性能优化]
sources: [raw/01-articles/2026-10-11 - 为什么越来越多人用Quarkus？.md]
last_updated: 2026-10-12
---

## 核心摘要

文章回答"为什么越来越多人用 Quarkus"：Spring Boot 继承的运行时反射模型与 Kubernetes 弹性伸缩模型存在结构性错配，导致启动慢（5-15 秒）、内存大（常驻 200MB+）、预热久（前几分钟吞吐只有稳定期 30%-50%）三重困境。Quarkus 把扫描、解析、Bean 定义、代理生成等工作全部前移到构建阶段（ArC 依赖注入直接在构建期生成 `new GreetingService(new GreetingBean())` 字节码），运行时只加载预生成代码，天然满足 Native Image 的闭世界假设。官方基准（2026-03）显示吞吐 19,255 tps vs 7,238 tps、内存 269MB vs 583MB；BMW Romania 独立实测（2026-08）显示 JVM 启动 1.3s vs 5.6s、Native 启动约 200ms vs 2s、空闲内存 88MB vs 204MB。Quarkus 4 以 Java 21 为基线，`@RunOnVirtualThread` 让虚拟线程成为一等公民。缺点是生态成熟度不如 Spring Boot、Native Image 工程成本高、动态性受限、Kotlin 支持弱，适合 K8s 弹性伸缩、Serverless、高密度部署、AI 推理服务等云原生场景。

## 关联连接

- [[Quarkus]] — 文章主角实体
- [[构建期处理]] — 文章核心架构思想
- [[SpringBoot]] — 主要对比对象
- [[GraalVM]] — Native Image 编译基础
- [[虚拟线程]] — Quarkus 4 的并发模型
- [[AOT编译]] — 构建期确定性的底层技术
- [[摘要-aot-vs-jit编译]] — 编译模式对比的既有摘要
