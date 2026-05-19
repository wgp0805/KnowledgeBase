---
title: "async-await"
type: concept
tags: [JavaScript, 异步编程]
sources: [raw/01-articles/理解JavaScript的async-await.md, raw/01-articles/VUE3基础-async-await.md]
last_updated: 2026-05-19
---

## 定义
async/await 是 ECMAScript 2017 引入的异步编程语法糖，基于 Promise 实现，让异步代码以同步方式编写，显著提升可读性。

## 关键信息
- async 函数：始终返回一个 Promise 对象
- await 表达式：暂停 async 函数执行，等待 Promise 完成或拒绝
- 错误处理：使用 try/catch 捕获 await 中的异常
- 相比 Promise then 链：async/await 减少嵌套，代码更线型
- 可结合 Promise.all() 实现并行异步操作

## 关联连接
- [[JavaScript]] — 编程语言
- [[Promise]] — 异步编程模式
