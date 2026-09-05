---
title: "AOT编译"
type: concept
tags: [Java, JVM, 编译器, 性能优化]
sources: [raw/01-articles/面试官：什么是 AOT 编译？和 JIT 有什么区别？.md]
last_updated: 2026-07-08
---

## 定义
AOT（Ahead-Of-Time，提前编译）是在程序运行之前，将字节码（或源码）编译成目标机器本地机器码的编译方式，编译发生在构建阶段。

## 关键信息
- **编译时机**：构建时（Build Time），程序运行之前
- **编译基础**：无运行时信息，静态编译
- **核心流程**（以 [[GraalVM]] Native Image 为代表）：
  1. 静态分析阶段：从 `main` 方法出发，通过可达性分析找出所有被用到的类和方法，未引用代码直接剔除（死代码消除）
  2. 编译优化阶段：对保留代码做内联、逃逸分析、常量折叠等静态优化（无运行时 profiling 数据）
  3. 产物生成：输出平台相关原生二进制，启动时不需要 [[JVM]]，由操作系统直接加载
- **优势**：启动速度快（毫秒级）、内存占用低、产物体积小
- **劣势**：峰值性能略低（缺乏运行时 profiling 无法做激进优化）；跨平台需针对不同平台分别编译
- **动态特性限制**：反射、动态代理、JNI、动态类加载需通过配置文件显式声明（如 `reflect-config.json`）
- **PGO 优化**：Profile-Guided Optimization，先用 [[JIT编译]] 跑一遍收集 profiling 数据再用于 AOT，缩小性能差距
- **适用场景**：Serverless/函数计算、CLI 工具、云原生微服务（容器快速弹性扩缩容）
- **生态**：[[SpringBoot]] 3 的 Spring AOT 构建时处理（bean 注册、属性注入前移），配合 GraalVM 实现毫秒级启动

## 关联连接
- [[摘要-aot-vs-jit编译]] — 来源
- [[JIT编译]] — 对比概念
- [[GraalVM]] — 代表技术
- [[HotSpot]] — 对比的 JIT 实现
- [[JVM]] — 运行环境
- [[Java]] — 所属语言
- [[SpringBoot]] — Spring AOT 生态
