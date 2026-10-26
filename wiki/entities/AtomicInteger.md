---
title: "AtomicInteger"
type: entity
tags: [Java, 并发, Atomic, JDK]
sources: [raw/09-archive/2026-09-27-并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ.md]
last_updated: 2026-09-28
---

## 定义

`AtomicInteger` 是 Java `java.util.concurrent.atomic` 包中基于 CAS 的原子整数类，提供原子更新、可见性与有序性保证，用于替代 `counter++` 这类存在丢失更新的普通自增。

## 关键信息

### 语言层三性质保证（来源：[[摘要-atomic语言层三性质]]）
- **原子性**：`incrementAndGet()` 按官方文档是"Atomically increments the current value"——读旧值、加一、写回是一次不可分割的 Atomic RMW，不会出现两个线程都读到 0、最后都写回 1 的丢失更新
- **可见性**：内存效果由 `VarHandle.getAndAdd` 定义，写入具备 `setVolatile(Object...)` 的内存语义，读取（`get()`）使用 `VarHandle.getVolatile` 读语义；JLS §17.4.4 规定 volatile 写 "synchronizes-with all subsequent reads of v by any thread"，因此 Atomic 更新之前的普通写（如 `ready = true`）对读到该更新的线程可见
- **有序性**：JLS §17.4.5 happens-before "If one action happens-before another, then the first is visible to and ordered before the second"；结合 program order + synchronizes-with + 传递性，可推出 `A1 happens-before B2`，排除 `counter == 1 && ready == false` 这种状态

### 对照
- Go：`atomic.Int64.Add` + Go Memory Model 的 synchronized-before / 顺序一致序列
- Python：应用层没有对称的通用整数 Atomic API

## 关联连接

- [[原子性-可见性-有序性]] — 三性质概念
- [[Java]] — 所属语言
- [[Golang]] — 对照语言
- [[Python]] — 无对称 API 的对照
- [[摘要-atomic语言层三性质]] — 来源
