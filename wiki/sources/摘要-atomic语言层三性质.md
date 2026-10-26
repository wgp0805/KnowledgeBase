---
title: "摘要-atomic语言层三性质"
type: source
tags: [来源, 原始文件, 并发编程, Atomic, 内存模型]
sources: [raw/09-archive/2026-09-27-并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ.md]
last_updated: 2026-09-28
---

## 核心摘要

本文从语言内存模型层规则讨论 Atomic，对比 Java、Go、CPython 三种语言的 Atomic 分别保证什么。Java 的 `AtomicInteger.incrementAndGet()` 是一次不可分割的 Atomic RMW（不会出现两个线程都读到 0 后都写回 1 的丢失更新），其可见性由 `VarHandle.getAndAdd` 的 `setVolatile` 写语义与 `get()` 的 `getVolatile` 读语义给出，配合 JLS §17.4.4 的 synchronizes-with 规则，使 Atomic 更新前的普通写对后续读可见；JLS §17.4.5 的 happens-before 既保证"能看见"又规定先后次序，借助传递性可推出 A1 happens-before B2，从而排除 `counter==1 && ready==false` 的反例。Go 的 `atomic.Int64.Add` 同样是原子更新，Go Memory Model 规定"若原子操作 B 观察到 A 的效果，则 A synchronized-before B"，且所有 Atomic 操作表现得像处于某个顺序一致序列，happens-before 是 sequenced-before 与 synchronized-before 的传递闭包。CPython/Python 应用层没有与之对称的通用整数 Atomic API——`counter += 1` 不是语言层 Atomic，也不能因某配置存在 GIL 或 Runtime 内部使用 `_Py_atomic_*` 就当作应用可依赖的跨实现保证；`_Py_atomic_*` 如何落到编译器与 CPU 属下一篇的实现问题。

## 关联连接

- [[原子性-可见性-有序性]] — 本文讨论的三性质概念
- [[AtomicInteger]] — Java 侧的 Atomic 类
- [[Java]] — JLS 内存模型
- [[Golang]] — Go 内存模型与 sync/atomic
- [[Python]] — 无对称 Atomic API 的应用层
- [[摘要-java-concurrency]] — 同系列并发主题来源
