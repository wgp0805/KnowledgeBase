---
title: "摘要-aot-vs-jit编译"
type: source
tags: [来源, 原始文件, Java, JVM, 编译, AOT, JIT, GraalVM]
sources: [raw/01-articles/面试官：什么是 AOT 编译？和 JIT 有什么区别？.md]
last_updated: 2026-07-08
---

## 核心摘要
AOT（Ahead-Of-Time，提前编译）在构建阶段将字节码编译为目标机器的本地机器码，编译发生在运行之前；JIT（Just-In-Time，即时编译）在程序运行过程中监控到热点代码后动态编译为机器码，编译发生在运行时。Java 代码的完整编译链路为：`javac` 前端编译（`.java`→`.class`）→ 运行阶段解释执行/JIT 编译/AOT 编译三选一。[[JIT编译]] 以 [[HotSpot]] 的分层编译为核心：第 0 层解释执行并统计方法调用频率，超过阈值（默认约 10000 次）触发 C1 简单优化，持续高频则由 C2 做激进优化（内联、逃逸分析、去虚化等），峰值性能更高但需预热。[[AOT编译]] 以 [[GraalVM]] Native Image 为代表：通过可达性分析做死代码消除，静态编译优化后输出平台相关原生二进制，毫秒级启动无需 JVM，但峰值性能略低且对反射/动态代理等动态特性支持受限（需 `reflect-config.json` 等配置）。选型建议：长期运行服务端用 JIT（预热后峰值高），Serverless/CLI/云原生微服务用 AOT（启动快即省钱）。Spring 6 / Spring Boot 3 引入 Spring AOT 构建时处理，配合 GraalVM 可实现毫秒级启动。

## 关联连接
- [[AOT编译]] — 本文提炼的核心概念
- [[JIT编译]] — 本文提炼的核心概念
- [[GraalVM]] — AOT 编译代表技术
- [[HotSpot]] — JIT 编译代表实现
- [[JVM]] — 编译运行环境
- [[Java]] — 编译链路所属语言
- [[SpringBoot]] — Spring AOT 构建时处理
- [[胖虎]] — 原文作者
