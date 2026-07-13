---
title: "gRPC"
type: concept
tags: [RPC, 通信, Google]
sources: ["raw/01-articles/使用 Shadcn UI 构建 Java 桌面应用.md"]
last_updated: 2026-07-13
---

## 定义

gRPC 是 Google 开源的高性能 RPC（远程过程调用）框架，基于 HTTP/2 协议和 Protobuf 序列化，支持双向流式通信，广泛用于微服务间通信和跨语言调用。

## 关键信息

- **协议基础**：HTTP/2 + Protobuf 序列化
- **通信模式**：Unary（一请求一响应）、Server Streaming、Client Streaming、Bidirectional Streaming
- **核心优势**：高性能（二进制序列化）、强类型（Proto 文件生成代码）、跨语言
- **应用场景**：微服务通信、Java ↔ Web 通信（如 JxBrowser Bridge）、移动端与后端通信
- **Java 实现**：grpc-java，Spring Cloud Alibaba 支持 gRPC 集成

## 关联连接
- [[Protobuf]] — 序列化协议
- [[JxBrowser]] — gRPC 在桌面应用中的使用
- [[摘要-ShadcnUI构建Java桌面应用]] — 来源
