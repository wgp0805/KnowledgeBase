---
title: "Protobuf"
type: concept
tags: [序列化, Google, 高性能]
sources: ["raw/01-articles/使用 Shadcn UI 构建 Java 桌面应用.md", "raw/01-articles/2026-08-25 - 为什么越来越多人用gRPC？.md"]
last_updated: 2026-08-25
---

## 定义

Protocol Buffers（Protobuf）是 Google 开发的语言无关、平台无关的序列化机制，通过 `.proto` 文件定义数据结构，编译生成多语言代码，实现高效二进制序列化。

## 关键信息

- **核心优势**：体积小（二进制）、速度快（编解码）、强类型（Schema 定义）
- **工作流程**：编写 .proto 文件 → protoc 编译 → 生成 Java/Python/Go 等代码
- **版本兼容**：通过字段编号实现向后兼容，新增字段不影响旧版
- **应用场景**：gRPC 通信底层协议、Java ↔ Web 跨进程通信、配置文件序列化
- **与 JSON 对比**：Protobuf 体积约为 JSON 的 1/10，序列化速度快 5-100 倍

## 关联连接
- [[gRPC]] — 基于 Protobuf 的 RPC 框架
- [[JxBrowser]] — Java ↔ Web 通信场景
- [[摘要-ShadcnUI构建Java桌面应用]] — 来源
- [[摘要-为什么越来越多人用gRPC]] — 来源（性能对比）
- [[HTTP2]] — gRPC 底层协议
