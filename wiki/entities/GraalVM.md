---
title: "GraalVM"
type: entity
tags: [Java, JVM, 编译器, AOT, 多语言运行时]
sources: [raw/01-articles/面试官：什么是 AOT 编译？和 JIT 有什么区别？.md]
last_updated: 2026-07-08
---

## 定义
GraalVM 是 Oracle 开发的多语言运行时，支持 AOT 原生镜像编译（Native Image），可在构建阶段将 Java 应用编译为平台相关的原生二进制文件，启动时无需 [[JVM]]。

## 关键信息
- **Native Image**：`native-image -jar my-app.jar my-app` 输出原生可执行文件，毫秒级启动
- **编译流程**：静态分析阶段（从 main 方法出发做可达性分析，死代码消除）→ 编译优化阶段（内联、逃逸分析、常量折叠，无运行时 profiling）→ 产物生成（平台相关二进制）
- **优势**：启动快、内存占用低、产物小（死代码消除）
- **限制**：反射、动态代理、JNI、动态类加载等动态特性需通过配置文件显式声明（如 `reflect-config.json`）；所有线程必须在构建时可知
- **PGO 优化**：Profile-Guided Optimization，先用 JIT 跑一遍收集 profiling 数据，再用于 AOT 编译，缩小与 JIT 的峰值性能差距
- **生态支持**：[[SpringBoot]] 3 的 Spring AOT 构建时处理配合 GraalVM 可实现毫秒级启动
- **Graal JIT**：GraalVM 也可作为 JIT 编译器替代 [[HotSpot]] 的 C2

## 关联连接
- [[摘要-aot-vs-jit编译]] — 来源
- [[AOT编译]] — 核心能力概念
- [[JIT编译]] — 对比概念
- [[HotSpot]] — 对比的 JVM 实现
- [[JVM]] — 运行时基础
- [[Java]] — 主要支持语言
- [[SpringBoot]] — Spring AOT 生态配合
