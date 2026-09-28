---
title: "并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ"
source: "博客园"
url: "https://www.cnblogs.com/ThinkerQAQ/p/23115900"
date: "2026-09-27T11:42:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/ThinkerQAQ/p/23115900  
> **抓取日期**: 2026-09-27  
> **相关性评分**: 0.7

## 目录

  * 0\. 从上一篇继续
  * 1\. 三种语言的 Atomic 规则分别保证什么？
    * 1.1 Java：AtomicInteger
    * 1.2 Go：sync/atomic
    * 1.3 CPython：应用层没有对称的 Atomic API
  * 2\. 下一篇：Atomic 是怎么实现的？



* * *

## 0\. 从上一篇继续

这一篇直接从语言内存模型层的规则讨论 Atomic。

* * *

## 1\. 三种语言的 Atomic 规则分别保证什么？

### 1.1 Java：AtomicInteger

#### 1.1.1 Atomicity

[`AtomicInteger.incrementAndGet()`](<https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/atomic/AtomicInteger.html#incrementAndGet\(\)>) 原文：

> **“Atomically increments the current value, with memory effects as specified by`VarHandle.getAndAdd`.”**

这句话直接说明：`incrementAndGet()` 是一次**原子加一** 。读取旧值、加一、写回不是三个可以被其他线程插入的步骤，而是一次不可分割的 Atomic RMW。

例如：
    
    
    AtomicInteger counter = new AtomicInteger(0);
    
    // Thread A
    counter.incrementAndGet();
    
    // Thread B
    counter.incrementAndGet();
    

两次更新会依次作用在同一个值上：
    
    
    Thread A                    Thread B
    
    incrementAndGet()           incrementAndGet()
            │                           │
            ▼                           ▼
          0 → 1                       1 → 2
    

因此不会出现普通 `counter++` 中两个线程都读到 `0`，最后都写回 `1` 的丢失更新。

#### 1.1.2 Visibility

`incrementAndGet()` 的内存效果由 `VarHandle.getAndAdd` 定义。[VarHandle.getAndAdd](<https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/invoke/VarHandle.html#getAndAdd\(java.lang.Object...\)>) 对写入的描述是：

> **“with the memory semantics of`setVolatile(Object...)`”**

而 [`AtomicInteger.get()`](<https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/atomic/AtomicInteger.html#get\(\)>) 使用的是 `VarHandle.getVolatile` 的读语义。

[JLS §17.4.4 Synchronization Order](<https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.4.4>) 对 volatile 的规则是：

> **“synchronizes-with all subsequent reads of v by any thread”**

意思是：Atomic 更新中的 volatile 写，与另一个线程后续的 volatile 读之间可以建立 **synchronizes-with** 关系。

放回前面的例子：
    
    
    AtomicInteger counter = new AtomicInteger(0);
    boolean ready = false;
    
    // Thread A
    ready = true;                 // A1
    counter.incrementAndGet();    // A2
    
    // Thread B
    if (counter.get() == 1) {     // B1
        System.out.println(ready); // B2
    }
    

假设 B 的 `counter.get()` 读到的 `1` 就是 A 这次更新产生的结果，那么：
    
    
    Thread A                              Thread B
    
    A1  ready = true
            │
            │ program order
            ▼
    A2  counter.incrementAndGet()
            │
            │ synchronizes-with
            │ JLS §17.4.4
            └──────────────────────────► B1  counter.get() == 1
                                            │
                                            │ program order
                                            ▼
                                        B2  read ready
    

因此，A 在 Atomic 更新之前已经完成的 `ready = true`，对 B 后续的读取可见。这就是这里的 **Visibility** 。

#### 1.1.3 Ordering

[JLS §17.4.5 Happens-before Order](<https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html#jls-17.4.5>) 原文：

> **“If one action happens-before another, then the first is visible to and ordered before the second.”**

意思是：happens-before 不只说明“能看见”，还规定了两个操作之间必须遵守的先后关系。

上面的例子可以直接推成：
    
    
    A1 ready = true
        ↓ program order
    A2 counter.incrementAndGet()
        ↓ synchronizes-with
    B1 counter.get() == 1
        ↓ program order
    B2 read ready
    

也就是：
    
    
    A1 happens-before A2
    A2 happens-before B1
    B1 happens-before B2
    
            ↓ transitivity
    
    A1 happens-before B2
    

所以 B 一旦已经通过 `counter.get()` 观察到 A 的更新，就不能再出现：
    
    
    counter == 1
    ready == false
    

这就是这里的 **Ordering** 。

### 1.2 Go：sync/atomic

#### 1.2.1 Atomicity

[`atomic.Int64.Add`](<https://pkg.go.dev/sync/atomic#Int64.Add>) 原文：

> **“Add atomically adds delta to x and returns the new value.”**

意思很直接：`Add(1)` 把读取、加一和写回作为一次原子更新。

例如：
    
    
    var counter atomic.Int64
    
    // Goroutine A
    counter.Add(1)
    
    // Goroutine B
    counter.Add(1)
    

两次更新不会丢掉其中一次：
    
    
    Goroutine A                 Goroutine B
    
    Add(1)                      Add(1)
      │                           │
      ▼                           ▼
    0 → 1                       1 → 2
    

这就是 **Atomicity** 。

#### 1.2.2 Visibility

[The Go Memory Model - Atomic Values](<https://go.dev/ref/mem#atomic>) 原文：

> **“If the effect of an atomic operation A is observed by atomic operation B, then A is synchronized before B.”**

意思是：如果 B 的 Atomic 操作观察到了 A 的 Atomic 更新，那么 A 和 B 之间就建立了 **synchronized-before** 关系。

继续使用 `ready + counter`：
    
    
    var counter atomic.Int64
    var ready bool
    
    // Goroutine A
    ready = true          // A1
    counter.Add(1)        // A2
    
    // Goroutine B
    if counter.Load() == 1 { // B1
        fmt.Println(ready)    // B2
    }
    

假设 B 的 `counter.Load()` 读到的 `1` 就是 A 的 `Add(1)` 产生的结果：
    
    
    Goroutine A                           Goroutine B
    
    A1  ready = true
            │
            │ sequenced-before
            ▼
    A2  counter.Add(1)
            │
            │ synchronized-before
            │ Go Memory Model
            └──────────────────────────► B1  counter.Load() == 1
                                            │
                                            │ sequenced-before
                                            ▼
                                        B2  read ready
    

因此，A 在 Atomic 更新之前写入的 `ready = true`，对 B 后续的读取可见。这就是 **Visibility** 。

#### 1.2.3 Ordering

同一节还规定，所有 Atomic 操作表现得像处在：

> **“some sequentially consistent order”**

Go Memory Model 又把 happens-before 定义为 `sequenced-before` 和 `synchronized-before` 的传递闭包。

因此上面的关系可以直接推成：
    
    
    A1 ready = true
        ↓ sequenced-before
    A2 counter.Add(1)
        ↓ synchronized-before
    B1 counter.Load() == 1
        ↓ sequenced-before
    B2 read ready
    

也就是：
    
    
    A1 happens-before A2
    A2 happens-before B1
    B1 happens-before B2
    
            ↓ transitivity
    
    A1 happens-before B2
    

所以 B 已经观察到 `counter == 1` 后，不能仍然把 A 在此之前的 `ready = true` 当作没有发生。这就是 **Ordering** 。

### 1.3 CPython：应用层没有对称的 Atomic API

Python 标准库目前没有与 Java `AtomicInteger`、Go `atomic.Int64` 对称的通用整数 Atomic API。

因此，Python 应用代码没有一组可以像 Java、Go 那样直接引用的 Atomic 规则。普通的 `counter += 1` 不是 Python 语言层定义的 Atomic API；也不能因为某个 CPython 配置存在 GIL，或者 Runtime 内部使用 `_Py_atomic_*`，就把它当作应用层可以依赖的跨实现 Atomicity、Visibility 或 Ordering 保证。

CPython Runtime 确实需要 Atomic 来同步自己的共享状态。它如何把 `_Py_atomic_*` 落到编译器和 CPU，是下一篇的实现问题，而不是 Python 应用层公开语义的一部分。

* * *

## 2\. 下一篇：Atomic 是怎么实现的？

这一篇停在语言层：Java 和 Go 分别通过公开 Atomic API 与内存模型定义 Atomicity、Visibility 和 Ordering；Python 应用层则没有对称的通用 Atomic API。

下一篇会把这些语言层规则转换成实现层真正需要解决的问题，分别沿着 Java `AtomicInteger`、Go `sync/atomic` 和 CPython Runtime 内部的 `_Py_atomic_*`，从 Runtime 一直看到 CPU。

* * *

> 本文首发于 [ThinkerQAQ 的个人博客](<https://thinkerqaq.github.io/articles/concurrency-series-05-atomic-cas/?utm_source=cnblogs&utm_medium=referral&utm_campaign=article_syndication>)，由作者本人同步发布。原文可能持续修订，最新版本请以个人博客为准。


---
> 原文链接: https://www.cnblogs.com/ThinkerQAQ/p/23115900