---
title: "FastThrow"
type: concept
tags: [JVM, 性能优化, 异常, JIT编译]
sources: [raw/01-articles/2026-09-17-java服务异常日志只打印异常类型，没有堆栈定位分析 - 未来AI笔记.md]
last_updated: 2026-09-18
---

## 定义
HotSpot JVM 中名为 Fast Throw（快速抛出）的性能优化机制。当同一异常在同一位置被反复抛出后，JIT C2 编译器会将其替换为预分配的不含堆栈信息的"空壳"异常单例，大幅提升抛出性能。

## 关键信息

### 工作原理
1. **初次发生**：JVM 正常构建完整异常对象，包含详细堆栈信息
2. **触发优化**：JIT 发现同一位置异常抛出次数达到"热点"阈值
3. **Fast Throw 生效**：方法重新编译后，直接抛出全局预分配的异常单例，message 和 stack trace 为空

### 性能收益
- 100 万次 NPE：开启 Fast Throw 约 6 秒，关闭后约 28 秒，性能差距超过 4 倍
- 避免遍历调用栈构建堆栈的昂贵操作
- 避免为新异常对象分配内存

### 代价
- 日志只剩 `java.lang.NullPointerException: null`，无行号和方法信息
- 线上问题定位变得非常困难

### 定位与诊断
1. **向前追溯日志**：Fast Throw 生效前的前几次异常带有完整堆栈
2. **临时关闭**：`-XX:-OmitStackTraceInFastThrow`（不建议生产长期使用，可能引发日志风暴）
3. **根本方案**：修复 NPE bug 本身

### 京东实践
- 618 大促期间通过追溯历史日志定位 Fast Throw 问题
- 向前搜索同一异常在更早时间点的完整堆栈

## 关联连接
- [[摘要-jvm-fast-throw异常堆栈丢失]] — 来源
- [[JVM]] — Java 虚拟机
- [[JIT编译]] — 即时编译优化
- [[异常堆栈]] — 排查线索
