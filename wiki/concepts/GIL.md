---
title: "GIL"
type: concept
tags: [Python, CPython, 并发, 同步机制]
sources: [raw/09-archive/2026-10-11-并发编程（1.5）：操作系统层——Thread、Scheduler 与 Runtime 调度 - ThinkerQAQ.md]
last_updated: 2026-10-12
---

## 定义

GIL（Global Interpreter Lock，全局解释器锁）是默认 GIL-enabled CPython 中保护解释器共享 Runtime State（对象状态、引用计数、解释器自身数据结构）的全局锁：线程必须持有 GIL 才能执行受保护的 Python 解释器代码。它是**执行约束，而不是第二套线程调度器**——OS Scheduler 管"OS Thread → CPU"，GIL 管"Thread → Python Interpreter Execution"，两者职责独立。

## 关键信息

- **双重执行条件**：一个线程要执行 Python 字节码，需同时满足"其 OS Thread 获得 CPU"与"该线程获得 GIL"；另一线程持 GIL 时，其余线程在 acquire 处等待，GIL 释放后重新竞争
- **线程模型**：CPython 的 `threading.Thread` 经 `_thread` 直接创建 OS Thread，1:1 映射，**没有** Go G-M-P 或 Java Virtual Thread 那样的用户态线程复用
- **PyThreadState**：保存 Python 线程在解释器内的 Runtime State，"OS Thread + PyThreadState" 共同构成该线程在 CPython Runtime 中的执行上下文
- **等待与恢复**：阻塞 I/O、Lock、Condition 等待会挂起 OS Thread；默认构建的可释放 GIL 路径会让出解释器执行权，恢复时需重新取得 GIL
- **Free-Threaded CPython**：新执行模型不再把 GIL 作为正常执行路径上的全局互斥门槛，改用更细粒度的 Runtime 同步机制让多线程并行执行 Python 代码；但某些不兼容扩展仍可能让运行时重新启用 GIL
- **本质**：Free-Threaded 改变的是解释器的并发约束（同步方式），而非线程的执行载体（仍 1:1 映射 OS Thread）

## 关联连接

- [[Python]] — 所属语言生态
- [[摘要-os-thread-scheduler-runtime]] — 来源
- [[G-M-P调度]] — Go 侧用户态调度的对照概念
- [[虚拟线程]] — Java 侧线程复用的对照概念
