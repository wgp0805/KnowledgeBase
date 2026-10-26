---
title: "Quarkus"
type: entity
tags: [Java, 框架, 云原生, NativeImage, Kubernetes]
sources: [raw/09-archive/2026-10-11 - 为什么越来越多人用Quarkus？.md]
last_updated: 2026-10-12
---

## 定义

Quarkus 是面向 Kubernetes 的 Java 云原生应用框架，设计哲学是"构建期确定性优先"：把扫描、解析、Bean 定义、代理生成等重量级工作全部前移到构建阶段，运行时只加载预生成的字节码，从而同时获得极快的启动速度、极低的内存占用和可生产化的 GraalVM Native Image。官方仓库：github.com/quarkusio/quarkus，官网：quarkus.io。

## 关键信息

- **核心架构**：构建期处理 + ArC 依赖注入（构建时直接生成 `new GreetingService(new GreetingBean())` 字节码，无运行时反射查找与动态代理）；满足 Native Image 闭世界假设
- **性能数据**（官方基准 2026-03）：吞吐 19,255 tps vs Spring Boot 7,238 tps（2.7 倍）；JVM 启动 2.9s vs 6.6s；内存 269MB vs 583MB
- **性能数据**（BMW Romania 独立实测 2026-08，CTO Alex Diniș）：JVM 启动 1.3s vs 5.6s；Native 启动约 200ms vs 约 2s；空闲内存 88MB vs 204MB
- **虚拟线程**：Quarkus 4 以 Java 21 为基线，`@RunOnVirtualThread` 注解即可让阻塞式代码运行在虚拟线程上（M:N 调度，阻塞自动挂起释放载体线程）
- **编程模型**：通过 Eclipse Vert.x 统一命令式与响应式，遵循 MicroProfile 和 Jakarta EE 标准；Panache 风格 Repository 免写实现；Dev Mode 支持代码/配置/资源热重载
- **优点**：启动快（Native 200ms）、内存省一半、构建期决策带来运行时确定性、热重载体验好、Native Image 生产就绪
- **缺点**：生态成熟度不如 Spring Boot、Native 镜像构建慢且调试困难、运行时动态性受限、迁移学习曲线、Kotlin 支持弱
- **适用场景**：K8s 弹性伸缩、Serverless/FaaS、高密度部署、AI 推理服务、金融交易系统；长期运行核心服务与重 Spring 生态项目需评估

## 关联连接

- [[摘要-quarkus-cloud-native]] — 来源
- [[构建期处理]] — 核心架构概念
- [[SpringBoot]] — 主要对比与迁移对象
- [[GraalVM]] — Native Image 编译基础
- [[虚拟线程]] — 并发模型
- [[AOT编译]] — 构建期确定性的底层技术
