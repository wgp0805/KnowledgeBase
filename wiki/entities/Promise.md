---
title: "Promise"
type: entity
tags: [JavaScript, 异步编程]
sources: [raw/01-articles/理解JavaScript的async-await.md, raw/01-articles/VUE3基础-async-await.md]
last_updated: 2026-05-19
---

## 定义
Promise 是 JavaScript 中用于处理异步操作的对象，代表一个尚未完成但预计在未来完成的操作的结果。

## 关键信息
- 三种状态：pending（进行中）、fulfilled（已完成）、rejected（已拒绝）
- 链式调用：then() 接收结果、catch() 处理错误、finally() 最终执行
- 静态方法：Promise.all()（全部完成）、Promise.race()（竞速）、Promise.allSettled()
- async/await 基于 Promise 的语法糖

## 关联连接
- [[JavaScript]] — 编程语言
- [[async-await]] — 异步编程语法糖
