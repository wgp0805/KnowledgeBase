---
title: "SSE"
type: entity
tags: [网络协议, 服务器推送, 实时通信]
sources: ["raw/09-archive/2026-08-20-装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux.md", "raw/09-archive/2026-10-25 - 还用WebSocket？这才是实时消息推送的正确姿势！轻量好用.md"]
last_updated: 2026-10-26
---

## 定义
Server-Sent Events（服务器发送事件），HTTP 协议上的单向服务器推送机制。服务器通过持久连接持续向客户端发送事件流，客户端通过 EventSource API 接收。常用于实时通知、流式 AI 响应等场景。

## 关键信息
- 在 [[RenoPit]] 生产环境中，Nginx 针对 SSE 关闭代理缓冲（`proxy_buffering off`）、启用分块传输，并把读取超时设为一小时
- 与 WebSocket 的区别：SSE 是单向（服务器→客户端），基于 HTTP，更简单；WebSocket 是双向，独立协议
- AI 流式输出（如 LLM 逐 token 返回）常用 SSE 实现

### 浏览器 API 与选型（2026-10-25 IT码徒 增量）
- 前端 API：`new EventSource(url)` 建连；`readyState` 三态——0 相当于常量 EventSource.CONNECTING（连接未建立或断线中）、1 相当于 EventSource.OPEN（已建立，可收数据）、2 相当于 EventSource.CLOSED（已断且不会重连）；三个事件回调 open / message / error（open 连接建立触发，message 收到数据触发，error 通信错误/连接中断触发）
- 服务端三头：`Content-Type: text/event-stream`、`Cache-Control: no-cache`、`Connection: keep-alive`；消息体格式 `data: <payload>\n\n`
- 默认支持断线重连（WebSocket 需额外部署）；支持自定义发送的数据类型
- 兼容性：现代浏览器支持良好；IE 不支持 SSE，小程序也不支持 SSE
- 适用场景：数据大屏实时数据、消息中心未读推送等只需服务端单向推送的需求；需双向通讯（如聊天）时才选更重的 WebSocket

## 关联连接
- [[摘要-renopit-demo-healthcheck-docker]] — 来源
- [[摘要-sse-websocket服务端推送选型]] — 来源（浏览器 API、三方案选型与 Express Demo）
- [[RenoPit]] — 应用项目
- [[Nginx]] — SSE 代理配置
- [[FastAPI]] — 后端 SSE 生产者
- [[WebSocket]] — 双向通讯对照方案
- [[轮询]] — 三方案中的下策
