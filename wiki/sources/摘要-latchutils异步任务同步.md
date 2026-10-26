---
title: "摘要-latchutils异步任务同步"
type: source
tags: [来源, 原始文件]
sources: ["raw/09-archive/2026-10-25 - LatchUtils：简化 Java 异步任务同步的利器.md"]
last_updated: 2026-10-26
---

## 核心摘要
文章介绍了作者（小哈）为解决"并行分发耗时任务后等待全部完成"场景中 `CountDownLatch`/`CompletableFuture` 重复胶水代码问题而封装的轻量工具类 **LatchUtils**。其设计哲学是"多次提交，一次等待"：主流程通过 `submitTask(Executor, Runnable)` 注册若干任务（暂不执行），再调用一次 `waitFor(timeout, TimeUnit)` 统一触发执行并阻塞等待，返回 boolean 表示是否全部按时完成。内部用 `ThreadLocal<List<TaskInfo>>` 暂存当前线程提交的任务对，`waitFor` 时取出队列、创建 `CountDownLatch(任务数)`，每个任务包一层 `finally countDown()` 后提交线程池执行。文章以聚合服务并行调用用户/订单/商品服务的完整示例，与"手动 CountDownLatch"和"CompletableFuture.allOf"两种传统写法逐项对比（简洁性、状态管理、错误处理、关注点分离、易用性），结论是该封装在"无返回值、任务间无依赖、只需全部完成"的常见模式下显著提升可读性与可维护性。

## 关联连接
- [[LatchUtils]] — 文章主角工具类（含完整源码与实现机制）
- [[多次提交一次等待]] — 提炼的设计哲学/模式
- [[CountDownLatch]] — 提炼实体（底层同步原语）
- [[CompletableFuture]] — 对比方案（allOf 批量等待）
- [[Java]] — 所属语言
- [[小哈]] — 文章作者（「小哈学Java」公众号）
- [[虚拟线程]] — ThreadLocal 使用注意事项的交叉参考
- [[摘要-java-concurrency]] — Java 并发编程手册（既有的并发总览来源）
- [[摘要-CompletableFuture的使用]] — 同主题既有来源，互补阅读
