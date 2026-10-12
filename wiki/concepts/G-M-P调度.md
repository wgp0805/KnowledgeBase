---
title: "G-M-P调度"
type: concept
tags: [Go, 并发, 调度器, Runtime]
sources: [raw/01-articles/2026-10-11-并发编程（1.5）：操作系统层——Thread、Scheduler 与 Runtime 调度 - ThinkerQAQ.md]
last_updated: 2026-10-12
---

## 定义

G-M-P 是 Go Runtime 的用户态两级调度模型：**G**（Goroutine）是 Runtime 管理的逻辑执行单元，保存栈、PC/调度器上下文与调度状态；**M**（Machine）对应一个真实 OS Thread，由 OS Scheduler 调度到 CPU；**P**（Processor）是执行 User Go Code 所需的 Runtime 资源与执行资格（含 Local Run Queue 与 runnext）。核心约束：**M 必须持有 P 才能执行 Go 代码**，P 的数量由 `GOMAXPROCS` 决定。

## 关键信息

- **模型演进**：从"G 直接对应 OS Thread"到"G-M + 全局 Run Queue"（多 M 竞争全局队列、局部性差），再到引入 P + Local Run Queue 分散调度状态与竞争
- **Work Stealing**：Local Run Queue 分散竞争带来负载不均，持有空闲 P 的 M 会从其他 P 的队列偷取 Runnable G；`findRunnable()` 还会结合 Timer、Network Poller 等来源
- **阻塞系统调用**：持有 P 的 M 被 OS 阻塞时，P 可解绑交给其他 M 继续跑 G；M 从系统调用返回后需重新获取 P 才能执行 Go 代码
- **Preemption 抢占**：长时间运行的 G 会被抢占（含异步抢占）重新参与调度，但抢占不构成严格的公平性保证
- **两级调度分工**：Go Scheduler 选任务（交给持有 P 的 M），OS Scheduler 选线程（让 M 的 OS Thread 获得 CPU）；同一 M 上切换 G 不要求发生 OS 级上下文切换
- **关键函数**：`go f()` 创建 G；`gopark()` 挂起 G 但 M 可继续跑其他 G；`goready()` 使 G 重新入队；每个 M 带有使用系统栈的特殊 g0 执行调度、栈管理等底层工作
- **与 Java 虚拟线程的对照**：两者都是"逻辑执行单元与 OS Thread 解耦 + 用户态调度器"的思路，Java 侧是 JVM Scheduler + Carrier Thread，Go 侧是 P + Local Run Queue；CPython 则没有用户态线程复用

## 关联连接

- [[Golang]] — 所属语言
- [[摘要-os-thread-scheduler-runtime]] — 来源
- [[虚拟线程]] — Java 侧同类机制
- [[GIL]] — CPython 侧的对照概念（执行约束而非调度器）
- [[CFS调度器]] — OS 层的线程调度算法
- [[任务调度]] — 上层调度概念
