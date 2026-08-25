---
title: "gRPC"
type: concept
tags: [RPC, 通信, Google]
sources: ["raw/01-articles/使用 Shadcn UI 构建 Java 桌面应用.md", "raw/01-articles/2026-08-25 - 为什么越来越多人用gRPC？.md"]
last_updated: 2026-08-25
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

## 性能基准（2026-08，详见 [[摘要-为什么越来越多人用gRPC]]）

REST vs gRPC 实测对比（高并发场景）：
| 维度 | REST | gRPC |
| --- | --- | --- |
| 数据体积 | 基准 | 减少 60%-80% |
| 序列化速度 | 基准 | 提升 3-5 倍 |
| 连接建立 | 3RTT | 1RTT |
| 请求延迟 | 8-12ms | 2-3ms |
| 吞吐量 | 450 req/s | 1200 req/s |

### REST 高并发四大慢点
1. HTTP/1.1 一请求一连接限制（3 次握手）
2. JSON 文本协议又大又慢（字段名重复传输）
3. 序列化/反序列化开销大（文本解析三步走）
4. 没有连接复用（每请求独立）

### gRPC 四大优势
1. HTTP/2 多路复用（一个 TCP 连接并行处理成百上千请求）
2. Protobuf 二进制序列化（体积小 60%-80%，速度快 3-5 倍）
3. 强类型契约（.proto 文件生成多语言代码）
4. 双向流式通信（支持 Server/Client/Bidirectional Streaming）

### Spring Boot 4.1 官方支持
- 内置 `spring-boot-starter-grpc-server`，gRPC 服务端/客户端自动配置（默认 9090 端口）
- 详见 [[SpringBoot]] 4.1.0 新特性

### 选型定位
gRPC 不是来取代 REST 的，而是 REST 在内部服务间通信场景下的替代方案：
- **gRPC 适用**：微服务间高频通信、多语言混合团队、流式数据交互、AI Agent 实时通信
- **REST 适用**：对外公开 API、简单 CRUD 应用、前端直接调用

## 关联连接
- [[Protobuf]] — 序列化协议
- [[HTTP2]] — 底层协议
- [[REST]] — 对比方案
- [[同步RPC]] — 同步通信模式下的二进制选型
- [[进程间通信]] — 所属大类
- [[JxBrowser]] — gRPC 在桌面应用中的使用
- [[摘要-ShadcnUI构建Java桌面应用]] — 来源
- [[摘要-微服务架构-进程间通信]] — REST vs gRPC 选型来源
- [[摘要-为什么越来越多人用gRPC]] — 来源（性能基准与四大慢点）
