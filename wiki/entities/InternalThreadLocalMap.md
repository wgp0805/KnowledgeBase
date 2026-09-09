---
title: "InternalThreadLocalMap"
type: entity
tags: [Java, 并发, Netty, 类]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义
Netty 中承载 [[FastThreadLocal]] 值的内部映射类。存储结构是一个以变量值本身为元素、按下标访问的 Object 数组，而非 JDK ThreadLocalMap 的 entry 结构。

## 关键信息

### 主要属性
```java
// UnpaddedInternalThreadLocalMap
static final ThreadLocal<InternalThreadLocalMap> slowThreadLocalMap = new ThreadLocal<>();
static final AtomicInteger nextIndex = new AtomicInteger();
Object[] indexedVariables;

// InternalThreadLocalMap
public static final Object UNSET = new Object();   // 标识槽位尚未使用
private BitSet cleanerFlags;                        // 防止对同一 ftl 多次启动清理线程
```
- indexedVariables 存 ftl 的 value，按下标直接访问
- nextIndex 在每个 ftl 实例创建时分底下标
- slowThreadLocalMap 在线程不是 ftlt 时使用
- cleanerFlags 用 BitSet 存 {index:boolean}，把 index 位设为 true 表示该 Map 已对该 FastThreadLocal 启动过清理线程

### 初始化
```java
private InternalThreadLocalMap() { super(newIndexedVariableTable()); }

private static Object[] newIndexedVariableTable() {
    Object[] array = new Object[32];
    Arrays.fill(array, UNSET);
    return array;
}
```
默认长度 32，全部填充 UNSET。

### 取值
```java
public Object indexedVariable(int index) {
    Object[] lookup = indexedVariables;
    return index < lookup.length ? lookup[index] : UNSET;
}
```

### 两种获取路径
- **fastGet(FastThreadLocalThread thread)**：直接从线程上的 threadLocalMap 属性取，为 null 则 new 一个并 set 回线程
- **slowGet()**：从 UnpaddedInternalThreadLocalMap.slowThreadLocalMap（一个 JDK ThreadLocal）取 InternalThreadLocalMap，为 null 则 new 并 set 进去

## 关联连接
- [[FastThreadLocal]] — 存储的变量类型
- [[FastThreadLocalThread]] — 持有本 Map 的线程
- [[线性探测]] — JDK 侧对照策略
- [[摘要-fastthreadlocal为啥快]] — 来源
