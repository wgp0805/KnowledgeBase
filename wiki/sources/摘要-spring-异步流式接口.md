---
title: "摘要-spring-异步流式接口"
type: source
tags: [来源, Spring, 异步流式, SSE, 苏三]
sources: [raw/09-archive/Spring 实现 3 种异步流式接口.md]
last_updated: 2026-11-09
---

## 核心摘要
苏三介绍 Spring 三种异步流式接口工具：`ResponseBodyEmitter`（动态生成内容并逐步发送，如文件上传进度、实时日志、GPT 式逐字输出）、`SseEmitter`（ResponseBodyEmitter 子类，服务器向客户端推送实时数据，服务端持久化发射器按 userId 推送）、`StreamingResponseBody`（处理大数据量/持续数据流，直接写 OutputStream，下载超大文件避免一次加载内存）。相比 Callable/WebAsyncTask/DeferredResult/CompletableFuture（只返回单个值），这些工具能在异步处理的同时持续向客户端响应处理结果，且执行耗时操作不阻塞 Servlet 请求线程。

## 关键信息
- **共同点**：接口直接返回对象或 `ResponseEntity<xxxx>` 即异步；耗时操作不阻塞 Servlet 请求线程
- **超时**：`new XxxEmitter(-1L)` 为 0 或 -1 表示连接不超时；不设置则到默认超时自动断开
- **ResponseBodyEmitter**：模拟每 2 秒 send 一次，页面数据动态生成，效果与 GPT 回答一致；异常时 `completeWithError(e)`
- **SseEmitter**：服务端为每个连接创建并持久化到 `ConcurrentHashMap<userId, SseEmitter>`，消息产生时取出调用 send；`SseEmitter.event().data().id().name()` 构建事件；`Content-Type: text/event-stream`；客户端 `new EventSource(url)`；服务端重启可自动重连
- **StreamingResponseBody**：返回 `ResponseEntity<StreamingResponseBody>`，`out.write().flush()` 每 flush 一次写一次；下载文件转成文件流同理
- **应用场景**：GPT 式流式输出、实时消息推送、状态更新、超大文件下载

## 关联连接
- [[SSE流式输出]] — 概念（LLM 流式输出语境）
- [[异步流式接口]] — 概念
- [[SSE]] — 实体（协议）
- [[苏三]] — 作者
- [[WebSocket]] — 双向通讯对照
- [[轮询]] — 三方案中的下策
