---
title: "REST"
type: concept
tags: [API, REST, HTTP, 对比]
sources: [raw/01-articles/2026-08-25 - 为什么越来越多人用gRPC？.md]
last_updated: 2026-08-25
---

## 定义
REST（Representational State Transfer）是基于 HTTP/1.1 的 API 设计风格，通常使用 JSON 文本格式传输数据。是 gRPC 的主要对比对象，在低并发场景几乎无感，但高并发下四大瓶颈被无限放大。

## 关键信息
- **四大慢点**（高并发下）：
  1. HTTP/1.1 一请求一连接限制（每请求建新 TCP 连接，3 次握手）
  2. JSON 文本协议又大又慢（字段名重复传输，10 个字段每请求都重传）
  3. 序列化/反序列化开销大（文本解析：拆 Token → 构建对象树 → 映射 Java 对象）
  4. 没有连接复用（每请求独立，无法一个连接同时处理多请求）
- **性能基准**（对比 gRPC）：
  - 数据体积：基准（gRPC 减少 60%-80%）
  - 序列化速度：基准（gRPC 提升 3-5 倍）
  - 连接建立：3RTT（gRPC 1RTT）
  - 请求延迟：8-12ms（gRPC 2-3ms）
  - 吞吐量：450 req/s（gRPC 1200 req/s）
- **适用场景**：对外公开 API、简单 CRUD 应用、前端直接调用
- **不适用场景**：微服务间高频通信、多语言混合团队、流式数据交互、AI Agent 实时通信
- **定位**：gRPC 不是来取代 REST 的，而是 REST 在内部服务间通信场景下的替代方案

## 关联连接
- [[摘要-为什么越来越多人用gRPC]] — 来源
- [[gRPC]] — REST 的对比与替代方案
- [[HTTP2]] — gRPC 底层协议（REST 通常用 HTTP/1.1）
