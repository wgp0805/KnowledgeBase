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

### REST vs gRPC 业务选型
| 维度 | REST | gRPC |
| --- | --- | --- |
| 数据格式 | JSON 文本（冗余大、序列化效率低） | Protobuf 强类型二进制 |
| 适用 | 对外接口、前后端、第三方对接、低频简单调用 | 服务内部高频调用、多语言集群、流式通信 |
| 不适用 | 高并发、高吞吐、低延迟的服务间高频调用 | 对外公开接口、简单低频调用（过重） |
| 常见坑 | 动词混用无法利缓存、多资源要多次请求 | 旧防火墙不支持 HTTP2、前端对接复杂、字段变更兼容性 |
| 实践 | OpenAPI(Swagger) 契约 + 缓存 | IDL 优先、Protobuf 字段标记保证向后兼容 |

## 关联连接
- [[Protobuf]] — 序列化协议
- [[同步RPC]] — 同步通信模式下的二进制选型
- [[进程间通信]] — 所属大类
- [[JxBrowser]] — gRPC 在桌面应用中的使用
- [[摘要-ShadcnUI构建Java桌面应用]] — 来源
- [[摘要-微服务架构-进程间通信]] — REST vs gRPC 选型来源
