---
title: "摘要-为什么越来越多人用gRPC"
type: source
tags: [来源, gRPC, Protobuf, HTTP/2, Spring Boot 4.1, 微服务通信]
sources: [raw/01-articles/2026-08-25 - 为什么越来越多人用gRPC？.md]
last_updated: 2026-08-25
---

## 核心摘要
苏三深度解析 gRPC 为何成为微服务间通信的默认选择。REST API + JSON 在高并发下四大瓶颈：HTTP/1.1 一请求一连接、JSON 文本协议又大又慢、序列化反序列化开销大、无连接复用。gRPC 凭借 HTTP/2 多路复用（一次握手多次使用）+ Protobuf 二进制序列化（比 JSON 小 60%-80%、快 3-5 倍）解决这些痛点，实测 QPS 翻近 3 倍、响应时间降至三分之一。Spring Boot 4.1.0 提供官方 gRPC starter（spring-boot-starter-grpc-server/client），@GrpcService/@ImportGrpcClients/@GrpcClient/@GrpcAdvice 注解编程模型。gRPC 支持 Unary/Server Streaming/Client Streaming/Bidirectional Streaming 四种通信模式，跨语言一份 Proto 走天下。短板：浏览器需 gRPC-Web 代理、调试难度高、学习曲线、K8s 负载均衡需 Headless Service + 客户端轮询。

## 关键信息
- **REST 四大慢点**：HTTP/1.1 一请求一连接（3RTT）、JSON 文本协议字段名重复传输、序列化文本解析慢、无连接复用
- **gRPC 两大核心技术**：
  - HTTP/2：多路复用（一个 TCP 连接同时处理成百上千请求互不阻塞）、二进制帧、1RTT 握手、服务端推送
  - Protobuf：二进制只传字段编号和值，体积比 JSON 减少 60%-80%，序列化速度提升 3-5 倍
- **性能对比**：REST 8-12ms 延迟/450 req/s vs gRPC 2-3ms 延迟/1200 req/s；2026 基准测试 gRPC 吞吐量高 107%、延迟降 48%
- **四种通信模式**：Unary（一问一答）、Server Streaming（实时日志/事件推送）、Client Streaming（文件上传/批量提交）、Bidirectional Streaming（实时聊天/AI 流式对话）
- **Spring Boot 4.1 官方支持**：
  - 四个 starter：spring-boot-starter-grpc-server/client/server-test/client-test
  - spring-grpc 项目提供 @GrpcService、@ImportGrpcClients、GrpcChannelFactory
  - @GrpcService 注册服务端 Bean（类似 @RestController）
  - @ImportGrpcClients 触发 stub 自动创建
  - @GrpcClient("channel-name") 注入 stub
  - @GrpcExceptionHandlerAdvice + @GrpcAdvice 集中异常处理
  - 配置：spring.grpc.server.port=9090；spring.grpc.client.channel.<name>.target=static://host:port
- **配置属性变化（4.0→4.1）**：channels→channel、address→target、host:port 拆为 address+port、health.actuator.*→health.*
- **Gradle 注意**：4.1 Gradle 插件不再自动配置 gRPC，需 Protobuf 插件被应用才触发；Maven 不受影响
- **跨语言**：protoc 生成 Java/Go/Python/C++/Node.js/C# 代码，底层通信一致
- **Proto 契约**：接口即文档，强类型契约，修改 Proto 重新生成代码即可发现不兼容
- **四大短板**：浏览器兼容性（需 gRPC-Web）、调试难度（需 grpcurl/BloomRPC）、学习曲线、K8s 负载均衡（长连接粘滞，需 Headless Service + 客户端轮询或 Service Mesh）
- **适用场景**：微服务间通信✅✅✅、多语言团队✅✅✅、流式数据✅✅✅、AI Agent 实时通信✅✅✅；对外 API⚠️、简单 CRUD⚠️、前端直接调用❌

## 关联连接
- [[gRPC]] — Google 开源高性能 RPC 框架
- [[Protobuf]] — Protocol Buffers 二进制序列化协议
- [[HTTP2]] — gRPC 底层传输协议
- [[SpringBoot]] — 4.1.0 提供官方 gRPC starter
- [[苏三]] — 公众号「苏三说技术」作者
- [[REST]] — gRPC 的对比对象
