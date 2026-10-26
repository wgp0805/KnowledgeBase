---
title: "摘要-sse-websocket服务端推送选型"
type: source
tags: [来源, 原始文件]
sources: ["raw/01-articles/2026-10-25 - 还用WebSocket？这才是实时消息推送的正确姿势！轻量好用.md"]
last_updated: 2026-10-26
---

## 核心摘要
文章系统对比服务端主动推送的三种方案——轮询、WebSocket、SSE，并给出明确选型结论：只需服务端单向推送（数据大屏实时数据、消息中心未读消息）就用轻量的 SSE；需要双向通讯（典型如聊天）才用更重的 WebSocket；轮询则是占用浏览器并发名额、每次都要走完整 HTTP 建连流程的下策，仅在浏览器极端不支持 WebSocket 与 SSE 时使用。文章引用 SSE 官方文档说明两者差异：WebSocket 全双工但需服务端额外支持、断线重连需自行部署；SSE 部署在 HTTP 之上、现有服务端都支持、默认支持断线重连、支持自定义发送的数据类型。实操部分给出可运行的全套 Demo：前端原生 HTML 用 `new EventSource()` 监听 open/message/error 三事件，后端 Node.js + Express 设置 `text/event-stream`、`Cache-Control: no-cache`、`Connection: keep-alive` 三个响应头后，以 setInterval 每秒写入 `data: <JSON>\n\n` 持续推送。另有两个易踩的兼容性坑：IE 不支持 SSE，小程序也不支持 SSE。

## 关联连接
- [[SSE]] — 核心推荐方案，浏览器 API 与选型视角的增量来源
- [[WebSocket]] — 对比方案（双向通讯、ws/wss 独立协议）
- [[轮询]] — 三方案中的下策（伪推送）
- [[长轮询]] — HTTP 半推送的近亲机制，需与普通轮询区分
- [[SSE流式输出]] — SSE 在 LLM 流式对话场景的延伸应用
- [[摘要-flutter-dio-deepseek-sse]] — SSE 流式实战姊妹篇（移动端 Dio 接入）
- [[Nginx]] — SSE 生产代理部署注意事项（proxy_buffering off）
- [[IT码徒]] — 作者
