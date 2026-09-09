---
title: "摘要-fastthreadlocal为啥快"
type: source
tags: [来源, 原始文件, Java, 并发, Netty, 性能]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 核心摘要
文章（转译自 CSDN，netty-4.1.34 版本）解释 FastThreadLocal（ftl）为何比 JDK ThreadLocal 快：JDK 每个线程持有一个 ThreadLocalMap，用线性探测解决 hash 冲突，未找到空闲 slot 就向后尝试，冲突频繁时效率受损；ftl 直接改用数组，每个实例创建时通过 AtomicInteger 分配一个不重复下标 index，get() 时等价于 return array[index]，彻底避免冲突。实现自底向上分为三块——InternalThreadLocalMap 用 newIndexedVariableTable() 创建长度为 32 并以 UNSET 填充的 indexedVariables 数组，存的是变量值本身而非 entry，另有 BitSet cleanerFlags 防止对同一 ftl 多次启动清理线程；FastThreadLocalThread（ftlt）继承 java.lang.Thread 并聚合自己的 InternalThreadLocalMap；FastThreadLocal 在构造函数里调用 nextVariableIndex() 以步长 1 递增取 index，index 转负时回滚并抛 IllegalStateException。get() 流程是 InternalThreadLocalMap.get() → 判断当前线程类型走 fastGet 或 slowGet → indexedVariable(index) 直接下标取值 → 若为 UNSET 则 initialize()（调用 initialValue() 并写回数组，同时 addToVariablesToRemove 把 ftl 实例登记进数组第 0 个元素的 Set）→ registerCleaner()（netty-4.1.34 已注释掉 ObjectCleaner.register 调用）。关键退化点：普通线程不含 InternalThreadLocalMap 结构，只能走 slowGet()，从 UnpaddedInternalThreadLocalMap.slowThreadLocalMap 这个 JDK ThreadLocal 里取 InternalThreadLocalMap 再取数组下标，性能退回 JDK 实现。ftl 提供三种回收机制：自动（ftlt 执行被 FastThreadLocalRunnable wrap 的任务结束后自动清理）、手动（ftl 与 InternalThreadLocalMap 的 remove，普通线程的线程池必须手动）、Cleaner（为每个 ftl 注册，线程不强可达时回收，但需另起线程且有多线程竞争，netty 官方不推荐）。在 netty 中最重要的用法是 ByteBuf 分配：PoolByteBufAllocator 的内部类 PoolThreadLocalCache 继承 FastThreadLocal<PoolThreadCache>，initialValue() 里用 leastUsedArena 为每个线程挑选堆 Arena 与直接内存 Arena，useCacheForAllThreads 或非 ftlt 线程则全部缓存大小传 0 不启用缓存。

## 关联连接
- [[FastThreadLocal]] — 主体实现
- [[InternalThreadLocalMap]] — 数组式线程本地存储
- [[FastThreadLocalThread]] — 聚合 InternalThreadLocalMap 的线程
- [[PoolThreadLocalCache]] — netty 内存池缓存的用法
- [[Netty]] — 所属框架
- [[ThreadLocal]] — JDK 对照实现
- [[线性探测]] — JDK ThreadLocalMap 的冲突策略
- [[内存池化]] — ByteBuf 分配的池化思想
- [[摘要-java-concurrency]] — Java 并发编程手册
