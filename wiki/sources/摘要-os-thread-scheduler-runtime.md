---
title: "摘要-os-thread-scheduler-runtime"
type: source
tags: [来源, 原始文件, 并发编程, 线程调度, 操作系统, Runtime]
sources: [raw/09-archive/2026-10-11-并发编程（1.5）：操作系统层——Thread、Scheduler 与 Runtime 调度 - ThinkerQAQ.md]
last_updated: 2026-10-12
---

## 核心摘要

本文是并发编程系列第 1.5 篇，回答核心问题：Java Thread、Go Goroutine、CPython Thread 这些语言执行单元如何通过 Runtime 与操作系统最终在 CPU 上执行，分三个环节展开——执行映射、调度分工、等待与恢复。Java 侧从 1:1 平台线程演进为 Platform Thread + Virtual Thread 双模型（虚拟线程由 JVM Scheduler 分派到 Carrier Thread，等待时可卸载释放载体）；Go 侧从 G-M 演进为 G-M-P（P 持有 Local Run Queue 降低全局竞争，M 必须持有 P 才能执行 Go 代码，配合 Work Stealing、阻塞系统调用时解绑 P、异步抢占）；CPython 侧 threading.Thread 仍 1:1 映射 OS Thread，但默认构建需同时满足"OS Thread 获得 CPU"与"持有 GIL"两个条件才能执行 Python 字节码，Free-Threaded 构建则改用细粒度同步。最后提炼语言无关的共同套路：执行单元与 OS Thread 的承载关系可以解耦复用，Runtime 任务分派与 OS 线程调度是两层独立选择（Runnable ≠ Running），唤醒只重新获得调度机会而非立即执行。

## 关联连接

- [[G-M-P调度]] — Go 调度模型概念
- [[GIL]] — CPython 执行约束概念
- [[虚拟线程]] — Java 轻量级线程概念
- [[Golang]] — G-M-P 模型所属语言
- [[Python]] — GIL 所属语言生态
- [[CFS调度器]] — OS 层公平调度的既有概念
- [[任务调度]] — 上层调度概念
- [[摘要-时间片-调度]] — 同系列 OS 调度主题摘要
- [[摘要-虚拟线程vs传统线程池]] — 虚拟线程实测对比摘要
