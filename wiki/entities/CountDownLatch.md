---
title: "CountDownLatch"
type: entity
tags: [Java, 并发, JDK, 同步工具]
sources: ["raw/09-archive/2026-10-25 - LatchUtils：简化 Java 异步任务同步的利器.md"]
last_updated: 2026-10-26
---

## 定义
JDK 并发倒数门闩：计数归零前阻塞等待线程，是 [[LatchUtils]] 的底层实现机制。

## 关键信息
- **用法**：`new CountDownLatch(n)`，每个任务完成时调用 `countDown()` 减一，主线程 `await(timeout, unit)` 阻塞至计数归零或超时，返回 boolean
- **手动管理三大痛点**（文章视角）：
  - 必须在每个业务 Runnable 的 `finally` 块中嵌入 `countDown()`，并发控制侵入业务代码、易忘记
  - 主线程 `await()` 需显式处理 InterruptedException
  - 生命周期需自己创建、维护、传递实例
- **关键细节**：`finally` 中 countDown 保证即使任务抛异常也能减一，避免主流程永久挂起；LatchUtils 正是把这套模板下沉到工具类内部
- 本篇为其在 wiki 中的首次入库（此前无任何页面提及）

## 关联连接
- [[摘要-latchutils异步任务同步]] — 来源
- [[LatchUtils]] — 封装它的工具类
- [[多次提交一次等待]] — 基于它的封装模式
- [[Java]] — 所属语言
