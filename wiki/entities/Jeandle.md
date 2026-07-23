---
title: "Jeandle"
type: entity
tags: [Java, JVM, JIT, LLVM, 蚂蚁集团, 编译器]
sources: [raw/01-articles/蚂蚁又开源了一个顶级Java项目！.md]
last_updated: 2026-07-23
---

## 定义
Jeandle（筋斗云）是蚂蚁集团（Ant Group）开源的基于 LLVM 的 JVM JIT 编译器，基于 OpenJDK HotSpot JVM，利用 LLVM 进行编译优化与代码生成，将 LLVM 的性能优势和生态优势引入 JVM。

## 关键信息
- **全称**：Jeandle（筋斗云）
- **开源方**：蚂蚁集团（Ant Group）
- **技术路线**：基于 OpenJDK HotSpot JVM，使用 LLVM 作为编译后端
- **核心价值**：将 LLVM 业界顶尖的代码分析和优化能力引入 JVM
- **路线图**：
  - 2025 年底：实现全量 Bytecode 支持（Exception、GC、Synchronization 等）
  - 2026 年：性能优化（锁优化、逃逸分析、高级内联、Intrinsic、OSR、G1 GC 支持）
- **技术挑战**：完美支持 JVM 垃圾回收（GC）机制、为 Java 动态特性（如 synchronized）定制 LLVM 功能

## 关联连接
- [[摘要-jeandle-llvm-jit编译器]] — 来源
- [[蚂蚁集团]] — 开源方
- [[LLVM]] — 底层编译器基础设施
- [[JIT编译]] — 即时编译概念
- [[JVM]] — Java 虚拟机
- [[HotSpot]] — 代表实现
- [[OpenJDK]] — Java 平台开源实现