---
title: "PoolThreadLocalCache"
type: entity
tags: [Netty, 内存池, ByteBuf, 类]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义
Netty PoolByteBufAllocator 的内部类，继承 [[FastThreadLocal]]<PoolThreadCache>，是每个线程持有的内存缓存封装。这是 FastThreadLocal 在 netty 中最重要的一处使用。

## 关键信息
```java
final class PoolThreadLocalCache extends FastThreadLocal<PoolThreadCache> {

    @Override
    protected synchronized PoolThreadCache initialValue() {
        final PoolArena<byte[]> heapArena = leastUsedArena(heapArenas);
        final PoolArena<ByteBuffer> directArena = leastUsedArena(directArenas);

        Thread current = Thread.currentThread();

        if (useCacheForAllThreads || current instanceof FastThreadLocalThread) {
            // PoolThreadCache 即为各个线程持有的内存块的封装
            return new PoolThreadCache(
                    heapArena, directArena, tinyCacheSize, smallCacheSize, normalCacheSize,
                    DEFAULT_MAX_CACHED_BUFFER_CAPACITY, DEFAULT_CACHE_TRIM_INTERVAL);
        }
        // No caching so just use 0 as sizes.
        return new PoolThreadCache(heapArena, directArena, 0, 0, 0, 0, 0);
    }
}
```
- **分配策略**：每个线程分配一块内存（PoolArena），需要分配 ByteBuf 时线程先从自己持有的 PoolArena 分配，自己无法分配时再采用全局分配
- 内存资源有限，仍会有多个线程持有同一块 PoolArena，但已最大限度减轻多线程资源竞争
- **缓存开关**：useCacheForAllThreads 为真或当前线程是 [[FastThreadLocalThread]] 时才启用真实缓存大小；否则 tiny/small/normalCacheSize 全部传 0，即不启用缓存——对应"普通线程用 ftl 会退化"的现象
- leastUsedArena 让初始 Arena 选择偏向当前使用最少者，天然形成负载均衡

## 关联连接
- [[FastThreadLocal]] — 基类
- [[FastThreadLocalThread]] — 缓存启用条件之一
- [[Netty]] — 所属框架
- [[内存池化]] — 该用法体现的设计思想
- [[摘要-fastthreadlocal为啥快]] — 来源
