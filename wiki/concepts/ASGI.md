---
title: "ASGI"
type: concept
tags: [Python, 异步, Web规范]
sources: [raw/01-articles/FastAPI 入门教程.md]
last_updated: 2026-06-29
---

## 定义
**ASGI（Asynchronous Server Gateway Interface）** 是 Python 异步 Web 应用与服务器之间的标准接口规范，是同步 WSGI 的异步升级版。它允许 Web 框架（如 [[FastAPI]]、Starlette、Django Channels）通过 `async/await` 处理 HTTP、WebSocket、HTTP/2 等多种协议。

## 关键信息

### WSGI vs ASGI

| 维度 | WSGI（同步） | ASGI（异步） |
|------|--------------|--------------|
| 协议支持 | 仅 HTTP/1 | HTTP、WebSocket、HTTP/2 |
| 并发模型 | 线程独占（同步阻塞） | 事件循环调度（异步非阻塞） |
| 代表框架 | Flask、Django（传统） | [[FastAPI]]、Starlette、Django Channels |
| 服务器 | Gunicorn、uWSGI | [[Uvicorn]]、Hypercorn、Daphne |
| 适用场景 | 简单 Web 应用 | 高并发 API、实时通信 |

### 餐厅比喻
- **WSGI（同步）**：每个服务员一次只能服务一桌客人，其他客人干等——每个请求独占线程，直到处理完才释放
- **ASGI（异步）**：同一个服务员可以同时服务多桌——点完 A 桌的菜趁厨房做菜的时间去给 B 桌点单。每个请求在事件循环中被调度，不独占线程资源

### 为什么 FastAPI 快
基于 ASGI 让 FastAPI 能轻松处理 **数千个并发连接**。在 [[async-await]] 函数中遇到 I/O 等待（数据库查询、外部 API、文件操作）时，事件循环会切换到其他请求，CPU 不空转。

### 混合场景处理
对于 CPU 密集型操作，应使用 `asyncio.to_thread()` 放到线程池执行，避免阻塞事件循环：
```python
result = await asyncio.to_thread(sync_heavy_work)
```

### 适用场景
- **I/O 密集型**：API 调用、数据库查询、文件操作 → ASGI 优势显著
- **CPU 密集型**：复杂算法、大数据计算 → 不如 [[Java]]（JIT + 线程池）

## 关联连接
- [[摘要-fastapi-入门教程]] — 来源
- [[FastAPI]] — ASGI 框架代表
- [[Uvicorn]] — ASGI 服务器
- [[async-await]] — 编程范式
- [[Pydantic]] — 配套数据校验
