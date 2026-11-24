---
title: "摘要-springboot4-2发布"
type: source
tags: [来源, SpringBoot, 发布, 迁移]
sources: ["raw/09-archive/SpringBoot4.2正式发布，人麻了！.md"]
last_updated: 2026-11-24
---

## 核心摘要
苏三 2026-11-24 解读 2026-11-19 发布的 Spring Boot 4.2.0。作者的情绪落点是"新功能不多，但用惯了的东西突然被打上弃用标签，还有一批默认值被悄悄改了"。三类变更：

**弃用（有 warning，不是移除）**：①[[RestTemplate]] 全家桶——Spring Framework 7.1 把它标记为"即将移除"，Spring Boot 4.2 连带弃用 `RestTemplateAutoConfiguration`、`RestTemplateObservationAutoConfiguration`、`RestTemplateBuilder`、`RestTemplateBuilderConfigurer`、`RestTemplateCustomizer` 与测试用的 `TestRestTemplate`，替代方案是 [[RestClient]] 与 `RestTestClient`；原因是 RestTemplate 基于 2009 年的阻塞式 I/O，在虚拟线程与 WebFlux 普及后资源利用率吃亏，而 RestClient 提供可链式组合的流式 API。②Apache Pulsar 支持——Spring for Apache Pulsar 最终版为 **2.0.8**，此后不再发补丁，维护移交 Apache 的 "Apache Pulsar support for Spring"，升级 4.2 不会立刻炸但拿不到后续更新。③`KafkaProperties` 的 `buildConsumerProperties()` / `buildProducerProperties()` / `buildAdminProperties()` 改用 `KafkaConfigBuilder`（只影响手动调用者，自动配置不受影响）。

**静默变更（比弃用更危险，连 warning 都没有）**：①`server.tomcat.servlet.use-relative-redirects` 默认值 false → true，重定向 Location 从绝对 URL 变相对路径，依赖绝对 URL 解析的前端/网关会静默拿到不同的头；恢复旧行为需显式设 false。②`X-Forwarded-Prefix` 在 4.2 默认被忽略，`native` 策略下 `contextPath` 由 `/api` 变为空，生成链接会丢前缀；framework 策略可设 `spring.webflux.forwarded-headers.use-forwarded-prefix=true`，native（Reactor Netty）没有直接配置项只能换策略或写 `NettyServerCustomizer`，通用开关是 `server.request.header.forwarded.use-prefix=true`。③WebFlux multipart 的大小/数量限制行为被明确，接近阈值的上传会在运行时被拒而编译期无感。④Tomcat 属性从 `server.tomcat.*` 挪到 `server.tomcat.servlet.*`，旧配置仍可用但有弃用警告。

**移除**：Janino 依赖管理被删（Logback 移除对 Janino 的支持、Janino 项目已归档），以前 Spring Boot 代管版本，现在 `pom.xml` 里不写版本号就编译不过。

**两个值得关注的新能力**：①**AMQP 1.0 支持**——与 RabbitMQ 长期使用的 AMQP 0-9-1 是两套协议，1.0 是 OASIS 标准化协议，跨厂商跨语言一致性更好，适合 .NET/Go/Python 与 Java 共存的系统；两者可在 RabbitMQ 共存，纯 Java + 0-9-1 的老系统不会被强制迁移。②**可执行 jar 启动更快**——优化了 `java -jar` 场景的类加载与资源定位，对 Serverless/FaaS/K8s 频繁扩缩容、CI 频繁起测试容器有实打实收益；war 外部 Tomcat 与 Native Image 不受直接影响。

时间压力：Spring Boot 4.1.x 的开源支持到 **2027-07-31** 结束，"先不升"是有保质期的。操作清单：对照弃用清单标注改造点；RestTemplate 分批迁（新代码先迁）；检查 `application.yml` 里的 `use-relative-redirects` 与 `X-Forwarded-Prefix`；用 Janino 就补版本号；升级后重点回归重定向与转发头相关用例。

## 关联连接
- [[SpringBoot]] — 主角（已增量合并 4.2 内容）
- [[RestTemplate]] — 被弃用的旧 HTTP 客户端
- [[RestClient]] — 官方替代方案
- [[AMQP]] — 4.2 新增协议支持
- [[RabbitMQ]] — 0-9-1 与 1.0 共存的载体
- [[Pulsar]] — 支持被移交 Apache
- [[Kafka]] — KafkaProperties 构建方法弃用
- [[虚拟线程]] — RestTemplate 被弃用的技术背景
- [[SpringAI]] — 2.1 基于 4.2，两篇来源互为上下游
