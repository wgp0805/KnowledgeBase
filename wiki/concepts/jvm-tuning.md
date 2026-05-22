---
title: "jvm-tuning"
type: concept
tags: [JVM, 性能优化]
sources:
  - raw/01-articles/jvm参数解释.md
  - raw/02-papers/java性能调优实战.pdf
last_updated: 2026-05-22
---

## 定义
JVM 调优是通过调整 JVM 参数来优化 Java 应用的内存使用、垃圾回收效率和运行性能的工程实践。

## 关键信息
- 堆内存配置：-Xms（初始堆）和 -Xmx（最大堆）设为相同值避免动态调整
- GC 选择：G1（通用默认）、CMS（低延迟）、ZGC（超大堆）、Parallel（高吞吐）
- GC 日志分析：-XX:+PrintGCDetails、-XX:+PrintGCTimeStamps
- OOM 诊断：-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath
- 元空间：-XX:MetaspaceSize（避免频繁 Full GC）
- JIT 编译监控：-XX:+PrintCompilation

## 关联连接
- [[JVM]] — Java 虚拟机
- [[Java]] — 编程语言
- [[摘要-java-performance-tuning]] — Java 性能调优实战
