---
title: "IO多路复用"
type: concept
tags: [Java, 网络, 面试, Linux, 并发]
sources: [raw/09-archive/面试官：如何理解 select、poll、epoll？.md]
last_updated: 2026-09-28
---

## 定义
IO 多路复用是让单个线程同时监听多个文件描述符（socket）的机制：内核在任一 fd 数据就绪时通知应用，避免为每个连接开一个线程阻塞等待。select、poll、epoll 是它的三代实现方案。

## 关键信息
### 三代演进
| 对比项 | select | poll | epoll |
| --- | --- | --- | --- |
| 发布 | 1983（4.2BSD） | 1986（System V） | 2002（Linux 2.5.44） |
| fd 上限 | FD_SETSIZE=1024 | 无硬限制（链表/数组） | 无硬限制 |
| fd 传递 | 每次全量拷贝进内核 | 每次全量拷贝 | epoll_ctl 注册一次，内核长期维护 |
| 检测方式 | 线性扫描 O(n) | 线性扫描 O(n) | 事件回调，就绪集合近似 O(1) |
| 适用 | 连接少、跨平台 | 连接中等 | 连接巨大、活跃比例低 |

- **select 三个致命伤**：1024 上限（glibc 用户态定义）、重复全量拷贝、两头线性扫描；且内核会改写 fd_set，每次调用前须 FD_ZERO 重建。
- **poll 的改进**：pollfd 数组突破数量上限，events/revents 分离免去重复设置，但 O(n) 本质未变，属过渡方案。
- **epoll 三板斧**：`epoll_create` 建实例、`epoll_ctl` 挂红黑树（增删改 O(log n)、天然去重）、`epoll_wait` 收就绪链表（rdllist）。工作量只与就绪 fd 数量相关。
- **常见误区**：epoll 并没有用 mmap 共享内存，epoll_wait 仍要把就绪事件从内核拷贝到用户空间，只是拷贝量从"全部 fd"降为"就绪 fd"。
- **并非永远更快**：连接数少且几乎全活跃时，红黑树与回调维护反而是额外开销，select/poll 不落下风。

### LT 与 ET 触发模式
- **LT（水平触发，默认）**：缓冲区还有数据就每次通知，可分次读写，编程简单。Redis（单线程 Reactor，10 万+ QPS）用 LT。
- **ET（边缘触发）**：仅在状态变化那一刻通知一次，必须搭配非阻塞 fd 循环 read 到 EAGAIN，否则残留数据永久丢失。Nginx 用 ET。

### 与 Java 体系的关系
- **Java NIO**：`Selector` 是 IO 多路复用的 JDK 封装，JVM 按操作系统选实现（Linux 用 epoll、Windows 用 select、macOS 用 kqueue）。
- **Netty**：`EpollEventLoopGroup` 通过 JNI 直调 Linux 原生 epoll，省掉 JDK 封装开销，还可用 SO_REUSEPORT，Linux 生产环境推荐。

## 关联连接
- [[摘要-面试官select-poll-epoll]] — 来源
- [[Netty]] — 使用 epoll 的网络框架
- [[Redis]] — LT 模式 + 单线程 Reactor 代表
- [[Nginx]] — ET 模式代表
- [[Linux]] — epoll 的运行平台
- [[上下文切换]] — 一连接一线程模型的主要开销
