---
title: "G1 GC"
type: concept
tags: [Garbage Collection, JDK, 2026]
sources: [raw/01-articles/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
G1 (Garbage First) 垃圾回收器，在JDK 9及以后版本中作为服务器环境的默认GC。JDK 27的JEP 523将其扩展为 **所有环境** 的默认GC，包括小容器、嵌入式设备和命令行工具。

## 核心概念
- **默认行为变更**：JDK 27中G1不再区分服务器和受限环境，取代Serial GC
- **吞吐量优化**：JEP 522减少G1的同步开销，吞吐量已接近Serial GC
- **延迟优势**：G1使用增量老年代回收，最大延迟持续优于Serial GC的全量回收
- **原生内存优化**：G1的原生内存占用降至与Serial GC相当的水平
- **启动时间优化**：小堆场景下G1的启动开销已优化为不明显

## 关联连接
- [[JDK27]] — JDK 27的默认GC
- Serial GC — 被替代的传统单线程GC
- [[Compressed OOP]] — 与G1配合使用的对象压缩技术
- Heap Usage — 内存占用相关概念