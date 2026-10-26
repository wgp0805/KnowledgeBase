---
title: "摘要-面试官select-poll-epoll"
type: source
tags: [来源, 原始文件, Java, 面试, IO多路复用]
sources: [raw/09-archive/面试官：如何理解 select、poll、epoll？.md]
last_updated: 2026-09-28
---

## 核心摘要
select、poll、epoll 都是 IO 多路复用的实现方案，目标是让单个线程同时监听多个 socket，谁的内核数据就绪就处理谁，避免一连接一线程的干等开销。三者是演进关系：select 有 1024 个 fd 上限且每次调用全量拷贝 + 全量扫描（O(n)）；poll 用 pollfd 数组突破了数量上限、事件与结果分离，但没破 O(n)；epoll 通过 epoll_ctl 一次注册（内核红黑树长期维护）+ 事件回调 + 就绪链表，把开销降到只与活跃连接数相关，成为 Linux 高并发的基石。epoll 有 LT（水平触发，默认，可分次读写）与 ET（边缘触发，只通知一次，必须配合非阻塞 fd 循环读到 EAGAIN）两种模式，Nginx 用 ET、Redis 用 LT。该机制映射到 Java 体系即 NIO 的 Selector（JVM 按操作系统自动适配 epoll/select/kqueue）与 Netty 的 EpollEventLoopGroup；文中还辟谣"epoll 用 mmap 减少拷贝"是错误说法。

## 关联连接
- [[小哈]] — 来源作者（小哈学Java 公众号）
- [[IO多路复用]] — 核心概念
- [[Netty]] — 底层依赖 epoll 的网络框架
- [[Redis]] — 单线程 Reactor + epoll 的代表
- [[Nginx]] — 使用 epoll ET 模式的高并发服务器
- [[Linux]] — epoll 的运行平台
- [[Java]] — NIO Selector 的宿主语言
