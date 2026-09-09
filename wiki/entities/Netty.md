---
title: "Netty"
type: entity
tags: [网络框架, TCP, Java]
sources: [raw/09-archive/程序汪4万20天接的肉鸽类小游戏，二期项目.md, raw/09-archive/吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？.md]
last_updated: 2026-09-09
---

## 定义

Java 高性能异步事件驱动网络通信框架，基于 NIO 实现，广泛用于 TCP/HTTP 协议的高并发场景。

## 关键信息

- **协议支持**：主要使用 TCP 协议通信
- **使用场景**：在线街机项目中用于硬件设备通信和服务端网络层
- **特点**：异步非阻塞、零拷贝、线程模型可配置（Reactor 多线程模型）

### FastThreadLocal 与内存池化

Netty 核心性能设计之一是 [[FastThreadLocal]]（ftl）。JDK [[ThreadLocal]] 的 ThreadLocalMap 用[[线性探测]]解决 hash 冲突——找不到空闲 slot 就不断往后尝试，冲突频繁时影响效率；ftl 直接改用数组，每个实例通过 AtomicInteger 分配一个不重复的下标 index，get() 等价于 return array[index]，从设计上消灭冲突环节。

三块实现：[[InternalThreadLocalMap]] 用长度为 32 并填充 UNSET 的 indexedVariables 数组存储变量值本身（而非 entry）；[[FastThreadLocalThread]] 继承 Thread 并聚合自己的 InternalThreadLocalMap；[[FastThreadLocal]] 构造函数调用 nextVariableIndex() 以步长 1 递增取 index。关键退化点：普通线程不含该结构，只能走 slowGet() 从 slowThreadLocalMap 这个 JDK ThreadLocal 里取 InternalThreadLocalMap，性能退回 JDK 实现。ftl 提供自动、手动、Cleaner 三种回收机制，官方推荐能用前两种就不用 Cleaner（需另起线程且有多线程竞争，netty-4.1.34 已注释掉 ObjectCleaner.register 调用）。

在 netty 中最重要的用法是 ByteBuf 分配：[[PoolThreadLocalCache]] 继承 FastThreadLocal<PoolThreadCache>，initialValue() 用 leastUsedArena 为每个线程挑选堆 Arena 与直接内存 Arena，线程优先从自己的 PoolArena 分配、失败才走全局分配——即[[内存池化]]。详见 [[摘要-fastthreadlocal为啥快]]。

## 关联连接

- [[摘要-程序汪-肉鸽小游戏二期]] — 来源
- [[摘要-fastthreadlocal为啥快]] — 来源（FastThreadLocal 源码级分析）
- [[SpringBoot]] — 项目后端框架
- [[Java]] — 编程语言基础
- [[FastThreadLocal]] — Netty 的线程本地变量实现
- [[InternalThreadLocalMap]] — 数组式线程本地存储
- [[FastThreadLocalThread]] — 聚合 InternalThreadLocalMap 的线程
- [[PoolThreadLocalCache]] — ByteBuf 分配的线程私有池缓存
- [[ThreadLocal]] — 被对照的 JDK 实现
- [[线性探测]] — JDK 侧的冲突解决策略
- [[内存池化]] — 线程私有内存池设计思想
