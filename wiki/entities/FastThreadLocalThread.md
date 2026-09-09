---
title: "FastThreadLocalThread"
type: entity
tags: [Java, 并发, Netty, 线程, 类]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义
Netty 提供的线程类（下文简称 ftlt），继承 java.lang.Thread 并聚合自己的 [[InternalThreadLocalMap]]。是发挥 [[FastThreadLocal]] 性能优势的必要前提。

## 关键信息
```java
public class FastThreadLocalThread extends Thread {
    // This will be set to true if we have a chance to wrap the Runnable.
    private final boolean cleanupFastThreadLocals;

    private InternalThreadLocalMap threadLocalMap;

    public final InternalThreadLocalMap threadLocalMap() {
        return threadLocalMap;
    }

    public final void setThreadLocalMap(InternalThreadLocalMap threadLocalMap) {
        this.threadLocalMap = threadLocalMap;
    }
}
```
- **诀窍**在 threadLocalMap 属性：继承 Thread 后聚合自己的 InternalThreadLocalMap，之后访问 ftl 变量时，对 ftlt 线程都直接从 InternalThreadLocalMap 获取变量值
- **普通线程会退化**：普通线程不包含 InternalThreadLocalMap 这样的数据结构，只能走 slowGet()，从一个 JDK ThreadLocal 变量中获取 InternalThreadLocalMap，再从其中获取指定下标，性能退回 JDK 实现
- cleanupFastThreadLocals 表示是否有机会 wrap Runnable，配合自动清理机制
- 实践中 Netty 的线程池（如 DefaultThreadFactory 创建的线程）会自动创建 ftlt

## 关联连接
- [[FastThreadLocal]] — 依赖本类才能获得数组下标访问性能
- [[InternalThreadLocalMap]] — 聚合的存储结构
- [[PoolThreadLocalCache]] — 判断 current instanceof FastThreadLocalThread 决定是否启用缓存
- [[Netty]] — 所属框架
- [[摘要-fastthreadlocal为啥快]] — 来源
