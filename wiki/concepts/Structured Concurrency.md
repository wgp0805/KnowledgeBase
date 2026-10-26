---
title: "Structured Concurrency"
type: concept
tags: [Concurrency, JDK 27]
sources: [raw/09-archive/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
结构化并发（Structured Concurrency），JDK 27的JEP 533（第七预览），将子任务的生命周期严格嵌套在父任务内，确保父任务失败时子任务全部取消，子任务失败时父任务感知并处理，消除线程泄漏和孤儿任务。

## 核心概念
- **生命周期绑定**：子任务生命周期严格嵌套在父任务内
- **自动取消**：父任务失败，所有子任务自动取消；子任务失败，父任务感知并抛出异常
- **无线程泄漏**：离开try块时，scope自动关闭，所有未完成的子任务取消
- **错误处理**：`scope.throwIfFailed()` 任一失败则抛出，简化异常处理
- **API使用**：`try (var scope = new StructuredTaskScope.ShutdownOnFailure()) { ... }`

## 关联连接
- [[JDK27]] — 包含该特性（需--enable-preview）
- [[摘要-jdk27-正式发布-人麻了]] — 来源文章
- Thread Pool — 线程池概念
- Future — 传统并发Future概念
- Thread Leak — 线程泄漏问题
- Task Cancellation — 任务取消概念