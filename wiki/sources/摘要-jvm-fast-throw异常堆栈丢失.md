---
title: "摘要-jvm-fast-throw异常堆栈丢失"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/2026-09-17-java服务异常日志只打印异常类型，没有堆栈定位分析 - 未来AI笔记.md]
last_updated: 2026-09-18
---

## 核心摘要
HotSpot JVM 的 Fast Throw（快速抛出）性能优化机制：当同一异常在同一位置被反复抛出后，JIT C2 编译器会将其替换为预分配的不含堆栈信息的"空壳"异常单例，大幅提升抛出性能（100万次 NPE 从 28 秒降至 6 秒）。代价是日志只剩 `NullPointerException: null` 无行号信息。解决方案：向前追溯历史日志找到优化前的完整堆栈；临时用 `-XX:-OmitStackTraceInFastThrow` 关闭（不建议生产长期使用）；根本方案是修复 NPE bug。

## 关联连接
- [[FastThrow]] — 核心概念
- [[JVM]] — Java 虚拟机
- [[JIT编译]] — 即时编译
- [[异常堆栈]] — 排查线索
