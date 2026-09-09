---
title: "ThreadLocal"
type: entity
tags: [Java, 并发, JDK, 类]
sources: [raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义
JDK 提供的线程本地变量类。每个使用它的线程持有一个 ThreadLocalMap 实例变量——不使用 ThreadLocal 时不会创建该 Map，线程第一次访问某个 ThreadLocal 变量时才创建。

## 关键信息
- **查找机制**：ThreadLocalMap 使用[[线性探测]]解决 hash 冲突，没找到空闲 slot 就不断往后尝试，直到找到空闲位置插入 entry
- **性能瓶颈**：经常遇到 hash 冲突时影响效率，这是 [[FastThreadLocal]] 被造出来的直接原因
- **存储结构**：存的是 entry（ThreadLocal 到 value 的键值对），与 InternalThreadLocalMap 直接存变量值不同
- **典型内存泄漏路径**：ThreadLocalMap 的 key 是对 ThreadLocal 的弱引用，value 是强引用；线程长期存活且不 remove 会导致 value 无法回收——这正是 netty 为 ftl 提供三种回收机制的动因
- **在 netty 中的退化角色**：UnpaddedInternalThreadLocalMap.slowThreadLocalMap 就是一个 JDK ThreadLocal，普通线程走 slowGet() 时先从它取 InternalThreadLocalMap，再取数组下标

## 关联连接
- [[FastThreadLocal]] — netty 的替代实现
- [[InternalThreadLocalMap]] — netty 的替代存储
- [[线性探测]] — 其冲突解决策略
- [[摘要-fastthreadlocal为啥快]] — 来源
- [[摘要-java-concurrency]] — Java 并发编程手册
