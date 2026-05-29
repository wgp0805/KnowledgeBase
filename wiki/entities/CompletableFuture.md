---
title: "CompletableFuture"
type: entity
tags: [Java, 异步编程, 并发]
sources: []
last_updated: 2026-05-29
---

## 定义
CompletableFuture 是 Java 8 引入的异步编程工具，实现了 Future 和 CompletionStage 接口，支持链式调用、组合、异常处理等高级异步操作。

## 关键信息
- 创建：`supplyAsync()`（有返回值）、`runAsync()`（无返回值）
- 链式调用：`thenApply()`（转换）、`thenAccept()`（消费）、`thenRun()`（执行）
- 组合：`thenCompose()`（扁平化）、`thenCombine()`（合并两个结果）
- 异常处理：`exceptionally()`、`handle()`、`whenComplete()`
- 并行执行：`allOf()`（等待全部）、`anyOf()`（任一完成）
- 线程池：默认使用 ForkJoinPool.commonPool()，建议自定义线程池

## 关联连接
- [[Java]] — 所属语言
- [[摘要-CompletableFuture的使用]] — 来源
