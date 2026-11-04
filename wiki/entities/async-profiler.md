---
title: "async-profiler"
type: entity
tags: [Java诊断, profiling, JVM, 火焰图]
sources: [raw/09-archive/2026-11-01 - 为什么越来越多人用Arthas 4 ？.md]
last_updated: 2026-11-02
---

## 定义

async-profiler 是一个低开销的动态采样 profiling 工具，专为 HotSpot/OpenJDK 虚拟机设计。它通过 JVMTI 接口进行异步采样，无需 Safepoint，开销极小，是 Arthas `profiler` 命令的底层引擎，也是生成火焰图的核心工具。

## 关键信息

- **在 Arthas 中的集成**：Arthas 4 内置 async-profiler 升级到 **4.4 版本**；`profiler` 命令生成 SVG 火焰图
- **CPU 采样**：`profiler start` / `profiler stop --file /tmp/cpu-flame.svg`，宽度代表占用时间
- **墙钟时间采样（4.0.2 起）**：`profiler start --wall`，暴露锁等待、网络 IO 阻塞、数据库连接池耗尽等「线程在等、不耗 CPU」的等待时间
- **采样原理**：异步采样（JVMTI），无需 Safepoint，相比 JFR 等同步采样开销更低
- **典型用途**：线上排查 CPU 飙高、接口变慢但 CPU 不高、线程阻塞等问题

## 关联连接
- [[Arthas]] — 集成该工具的诊断框架
- JFR — 另一 JVM 性能采集机制（对比）
- 火焰图 — 输出可视化形式（待建）
- [[苏三]] — 文章作者
