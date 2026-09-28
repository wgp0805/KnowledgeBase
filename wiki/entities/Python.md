---
title: "Python"
type: entity
tags:
  - 语言
  - 生态
sources: [raw/01-articles/2026-09-27-并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ.md]
last_updated: 2026-09-28
---

## 定义
通用解释型编程语言，AI 生态的主导语言；requests、aiohttp、httpx 等库的 SOCKS5 代理兼容性差异是常见坑。

## 关键信息
- **应用层没有对称的 Atomic API**（来源：[[摘要-atomic语言层三性质]]）：Python 标准库目前没有与 Java `AtomicInteger`、Go `atomic.Int64` 对称的通用整数 Atomic API；`counter += 1` 不是语言层定义的 Atomic 操作，也不能因某个 CPython 配置存在 GIL、或 Runtime 内部使用 `_Py_atomic_*`，就把它当作应用层可依赖的跨实现 Atomicity/Visibility/Ordering 保证
- `_Py_atomic_*` 如何落到编译器与 CPU 属于 Runtime 实现细节，不是 Python 应用层公开语义的一部分

## 关联连接
- [[FastAPI]]
- [[SOCKS5]]
- [[摘要-socks5代理认证兼容性问题]]
- [[原子性-可见性-有序性]] — 三语言 Atomic 对照中的 Python 结论
- [[AtomicInteger]] — Java 侧对照
- [[Golang]] — Go 侧对照
- [[摘要-atomic语言层三性质]] — 来源
