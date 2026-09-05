---
title: "Uvicorn"
type: entity
tags: [Python, ASGI, 服务器]
sources: [raw/01-articles/FastAPI 入门教程.md]
last_updated: 2026-06-29
---

## 定义
Python 生态中的高性能 [[ASGI]] 服务器，基于 uvloop 和 httptools 构建，是运行 [[FastAPI]] 等 ASGI 应用的默认推荐。

## 关键信息

### 角色定位
Uvicorn 在 Python 异步 Web 栈中的位置，相当于 Java 生态中的：
- Tomcat（Servlet 容器，传统）
- Netty（高性能 NIO 网络框架）

### 启动方式
```bash
# 开发模式（自动重启）
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 生产部署（通常配合 gunicorn 多 worker）
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 参数说明
- `main:app` — `main.py` 模块中的 `app` 实例
- `--reload` — 开发模式下文件变化自动重启（生产禁用）
- `--host` — 监听地址（`0.0.0.0` 监听所有网卡）
- `--port` — 端口号

### 安装
```bash
pip install uvicorn[standard]
```
`[standard]` 包含 uvloop（更快的事件循环）+ httptools（更快的 HTTP 解析）等加速依赖。

## 关联连接
- [[摘要-fastapi-入门教程]] — 来源
- [[FastAPI]] — 默认运行宿主
- [[ASGI]] — 实现的规范
- [[Tomcat]] — Java 同位概念
