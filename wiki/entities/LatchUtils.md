---
title: "LatchUtils"
type: entity
tags: [Java, 并发, 工具类, 异步编程]
sources: ["raw/09-archive/2026-10-25 - LatchUtils：简化 Java 异步任务同步的利器.md"]
last_updated: 2026-10-26
---

## 定义
LatchUtils 是作者（[[小哈]]）封装的轻量级 Java 工具类，用"多次提交，一次等待"模式简化批量异步任务的同步等待，解决手动使用 CountDownLatch / CompletableFuture 时的重复胶水代码问题。

## 关键信息
- **API 仅两个静态方法**：
  - `submitTask(Executor executor, Runnable runnable)`：将任务与其执行线程池配对登记（暂不执行）
  - `waitFor(long timeout, TimeUnit timeUnit)`：触发全部已登记任务执行并阻塞等待，全部限时完成返回 true，超时返回 false；等待后自动清理任务列表，可重复使用
- **实现机制**：`ThreadLocal<List<TaskInfo>>`（LinkedList）暂存 TaskInfo（executor + runnable 对）；`waitFor` 内 popTask() 取出并 `remove()` 清理，`new CountDownLatch(size)`，逐个 `executor.execute(() -> { runnable.run(); finally latch.countDown(); })`，再 `latch.await(timeout, unit)`
- **隐含约束与注意点**：
  - submitTask 与 waitFor 必须在同一线程调用（ThreadLocal 决定）
  - 任务延迟执行：提交后到 waitFor 前不会运行（与 CompletableFuture.runAsync 即时提交不同）
  - `waitFor` 内 `catch (Exception ignored)` 静默吞掉 InterruptedException，属代码坏味道
  - 仅支持 Runnable，无返回值收集与任务编排能力
- **实战示例**：聚合服务并行调用用户(1000ms)/订单(1500ms)/商品(500ms)服务，`newFixedThreadPool(3)`，`waitFor(5, SECONDS)`
- **对比结论**（vs 手动 CountDownLatch / CompletableFuture.allOf，五维度）：代码简洁性极高、状态管理自动、错误处理简化、关注点分离优秀、几乎零学习成本

## 关联连接
- [[摘要-latchutils异步任务同步]] — 来源
- [[多次提交一次等待]] — 设计哲学
- [[CountDownLatch]] — 底层实现机制
- [[CompletableFuture]] — 对比方案
- [[ThreadLocal]] — 实现所依赖的线程本地存储
- [[小哈]] — 作者
