---
title: "JVM"
type: entity
tags: [Java, 虚拟机]
sources: [raw/01-articles/jvm参数解释.md]
last_updated: 2026-05-19
---

## 定义
JVM（Java Virtual Machine）是 Java 程序的运行环境，负责将 Java 字节码转换为机器码执行，是 Java 跨平台特性的基础。

## 关键信息
- 堆内存：-Xms（初始堆）、-Xmx（最大堆）、-Xmn（年轻代）
- 垃圾收集器：G1（默认）、CMS（低延迟）、ZGC（超大堆低延迟）、Parallel（高吞吐）
- 非堆内存：-XX:MetaspaceSize、-XX:MaxMetaspaceSize
- 栈配置：-Xss（线程栈大小）
- JIT 编译：-XX:+PrintCompilation 查看编译日志
- 常用监控参数：-XX:+PrintGCDetails、-XX:+HeapDumpOnOutOfMemoryError

## 关联连接
- [[Java]] — 编程语言
- G1 GC — G1 垃圾收集器（JVM 默认）
- ZGC — 超大堆低延迟垃圾收集器
