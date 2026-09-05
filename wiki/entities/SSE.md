---
title: "SSE"
type: entity
tags: [网络协议, 服务器推送, 实时通信]
sources: [raw/01-articles/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md]
last_updated: 2026-08-21
---

## 定义
Server-Sent Events（服务器发送事件），HTTP 协议上的单向服务器推送机制。服务器通过持久连接持续向客户端发送事件流，客户端通过 EventSource API 接收。常用于实时通知、流式 AI 响应等场景。

## 关键信息
- 在 [[RenoPit]] 生产环境中，Nginx 针对 SSE 关闭代理缓冲（`proxy_buffering off`）、启用分块传输，并把读取超时设为一小时
- 与 WebSocket 的区别：SSE 是单向（服务器→客户端），基于 HTTP，更简单；WebSocket 是双向，独立协议
- AI 流式输出（如 LLM 逐 token 返回）常用 SSE 实现

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[RenoPit]] — 应用项目
- [[Nginx]] — SSE 代理配置
- [[FastAPI]] — 后端 SSE 生产者
