---
title: "FastThreadLocal"
type: entity
tags: [Java, 并发, Netty, 性能, 类]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义
Netty 自定义的线程本地变量实现，用数组下标访问替代 JDK [[ThreadLocal]] 的 hash 查找，从而避免 hash 冲突对查找效率的影响。必须与 [[FastThreadLocalThread]] 配合使用才能发挥全部性能，否则退化回 JDK 实现。

## 关键信息

### 为什么快
- JDK ThreadLocalMap 用线性探测解决 hash 冲突：找不到空闲 slot 就不断往后尝试，冲突频繁时影响效率
- FastThreadLocal 直接用数组：每个实例创建时分配一个下标 index，get() 时等价于 return array[index]，彻底避免 hash 冲突

### index 分配
```java
private final int index;

public FastThreadLocal() {
    index = InternalThreadLocalMap.nextVariableIndex();
}
```
nextVariableIndex() 基于 AtomicInteger 以步长 1 递增，index 转负时 decrementAndGet 回滚并抛 IllegalStateException("too many thread-local indexed variables")。步长固定为 1 保证了数组长度不会突增。

### get() 四步
```java
public final V get() {
    InternalThreadLocalMap threadLocalMap = InternalThreadLocalMap.get();  // 1
    Object v = threadLocalMap.indexedVariable(index);                        // 2
    if (v != InternalThreadLocalMap.UNSET) return (V) v;
    V value = initialize(threadLocalMap);   // 3
    registerCleaner(threadLocalMap);        // 4
    return value;
}
```
1. **取 Map**：InternalThreadLocalMap.get() 判断当前线程类型，FastThreadLocalThread 走 fastGet（直接取线程上的 threadLocalMap，为空则新建并 set 回线程），普通线程走 slowGet
2. **下标取值**：indexedVariable(index) 判断 index < lookup.length ? lookup[index] : UNSET
3. **首次初始化**：调用 initialValue()，成功则 setIndexedVariable 写回数组（长度不够则扩充），同时 addToVariablesToRemove 把 ftl 实例登记到 threadLocalMap 内部数组第 0 个元素的 Set 中
4. **注册清理**：registerCleaner 先判断 FastThreadLocalThread.willCleanupFastThreadLocals(current) 与 threadLocalMap.isCleanerFlagSet(index)，两者之一为真则直接返回；否则 setCleanerFlag(index) 防止重复注册

### 三种回收机制
- **自动**：使用 ftlt 执行一个被 FastThreadLocalRunnable wrap 的 Runnable 任务，任务执行完毕后自动清理
- **手动**：ftl 与 InternalThreadLocalMap 都提供 remove 方法；普通线程的线程池使用 ftl 时必须手动调用
- **Cleaner**：为当前线程的每一个 ftl 注册 Cleaner，线程对象不强可达时回收。Netty 官方推荐能用前两种就不用第三种——需另起线程、耗费资源，多线程下会造成资源竞争。netty-4.1.34 中 ObjectCleaner.register 的调用已被注释掉

### 关键提醒
保存的是变量值本身而非 entry，这是与 JDK ThreadLocal 的重要差异。

## 关联连接
- [[InternalThreadLocalMap]] — 底层数组存储
- [[FastThreadLocalThread]] — 必须搭配使用的线程类
- [[PoolThreadLocalCache]] — netty 中最重要的 ftl 用法
- [[Netty]] — 所属框架
- [[ThreadLocal]] — 被对照的 JDK 实现
- [[线性探测]] — JDK 侧的冲突解决策略
- [[摘要-fastthreadlocal为啥快]] — 来源
