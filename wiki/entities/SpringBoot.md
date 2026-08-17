---
title: "SpringBoot"
type: entity
tags: [框架, Java, Spring]
sources:
  - raw/09-archive/springboot整合mybatisPlus.md
  - raw/09-archive/springboot整合redis.md
  - raw/09-archive/springboot整合RocketMq.md
  - raw/09-archive/SpringBoot-Aop的使用.md
  - raw/09-archive/SpringBoot接收参数的几种常用方式.md
  - raw/09-archive/SpringBoot优雅的加载配置文件的几种方式.md
  - raw/09-archive/SpringBoot整合SpringSecurity及框架的简单使用.md
  - raw/09-archive/理解Spring中的ApplicationListener与ApplicationRunner区别及使用场景.md
  - raw/09-archive/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md
  - raw/09-archive/springboot3.pdf
  - raw/09-archive/Spring Cloud Alibaba笔记.pdf
  - raw/09-archive/得物二面：SpringBoot 内部的启动流程是怎样的？我：没研究过.md
  - raw/09-archive/Spring Boot 4.1.0 震撼发布！新特性，惊爆了！.md
  - raw/09-archive/SpringBoot4 新特性：模块化架构.md
  - raw/09-archive/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md
  - raw/01-articles/优雅使用 Enum 提升 SpringBoot 配置管理效率！.md
last_updated: 2026-08-17
---

## 定义
Spring Boot 是 Spring 框架的自动配置扩展，简化了 Spring 应用的初始搭建和开发过程，遵循"约定优于配置"原则。

## 关键信息
- 提供 Starter 依赖管理简化 Maven/Gradle 配置
- 内置嵌入式 Tomcat/Jetty/Undertow 服务器
- 自动配置（Auto-Configuration）机制根据 classpath 依赖自动配置 Bean
- 提供 @SpringBootApplication 组合注解
- 支持 application.yml/properties 多层次配置
- 通过 @ConfigurationProperties 绑定配置到 POJO（支持 Enum/Map/List/嵌套类型，见 [[ConfigurationProperties]]）
- 支持 profile 多环境切换

### SpringBoot 4 新特性
- 基于 Spring Framework 7 和 Java 21+
- 强制依赖 **Servlet 6.1 规范**
- **移除 Undertow 嵌入式容器支持**（Undertow 未适配 Servlet 6.1）
- 嵌入式容器仅保留 Tomcat 11（Servlet 6.1）和 Jetty 12.1（Servlet 6.1）
- 声明式 HTTP 客户端（@HttpExchange）
- 结构化并发支持
- 虚拟线程支持（I/O 密集型场景性能提升）
- 启动速度提升 30%

### SpringBoot 4 模块化架构
Spring Boot 4 将原先单体式的 `spring-boot-autoconfigure` 拆分为多个独立模块，每个模块职责单一、依赖明确：

**核心模块拆分示例：**
| 模块名称 | 功能描述 |
| --- | --- |
| `spring-boot-webmvc` | 传统 Servlet Web 应用 |
| `spring-boot-webflux` | 响应式 Web 应用 |
| `spring-boot-data-jdbc` | JDBC 数据访问 |
| `spring-boot-flyway` | 数据库迁移管理 |
| `spring-boot-webclient` | 独立 WebClient 支持 |

**测试 Starter 模块化：**
`spring-boot-data-jdbc-test`、`spring-boot-starter-webmvc-test`、`spring-boot-starter-security-test`、`spring-boot-starter-flyway-test` 等，确保测试依赖与生产依赖一致且精简。

**模块化带来的好处：**
1. 可维护性更高：模块边界清晰，IDE 提供更精准的代码提示
2. 启动更快、内存占用更小：只加载所需模块，减少类路径扫描
3. 配置更精准：例如只想用 WebClient 时引入 `spring-boot-webclient` 即可，无需关闭 Web 服务器自动配置
4. 支持灵活用例：Micrometer 监控模块可独立使用，无需引入完整 Actuator 依赖链

**迁移指南：** 从 Spring Boot 3 迁移时，可先用 `spring-boot-starter-classic`（自动引入所有模块自动配置）过渡，再逐步精简为独立模块。包路径调整为 `org.springframework.boot.`。

### SpringBoot 4.1.0（2026-06-10 发布）
口号"更好写、更安全、更好观测"，关键特性：

| 方向 | 代表特性 |
| --- | --- |
| 微服务通信 | 内置 `spring-boot-starter-grpc-server`，gRPC 服务端/客户端自动配置（默认 9090 端口） |
| 安全加固 | `InetAddressFilter` 防 SSRF，限制 HTTP 客户端可访问的 IP 段，阻塞与响应式客户端都支持 |
| 性能优化 | `spring.datasource.connection-fetch=lazy` 延迟借出 JDBC 连接，事务方法未执行 SQL 时不占池 |
| 开发体验 | `@RedisListener` 自动配置（无需手写 `RedisMessageListenerContainer`）、Jackson 配置统一前缀 |
| 可观测性 | OpenTelemetry 自动跨 `@Async` 传播上下文、OTLP gzip 压缩、`/actuator/info` 新增进程信息 |
| 配置 | `spring.config.import` 支持 `[encoding=utf-8]` 解决中文乱码 |
| 批处理 | 新增 `spring-boot-batch-data-mongo`，Spring Batch 支持 MongoDB 后端 |
| 日志 | Log4j 支持按大小/时间/Cron 多策略轮转 |
| Kotlin | 基线升至 2.3，支持 Java 25 |

升级提醒：4.0 已废弃 API 被移除；Apache Derby 集成被废弃；Maven `-DskipTests` 不再跳过 AOT，需改用 `-Dmaven.test.skip=true`。

## 关联连接
- [[Spring]] — 基础框架
- [[SpringMVC]] — Web MVC 框架
- [[MyBatisPlus]] — ORM 整合
- [[Redis]] — 缓存整合
- [[RocketMQ]] — 消息队列整合
- [[SpringSecurity]] — 安全框架整合
- [[AOP]] — 面向切面编程
- [[frontend-backend-separation]] — 前后端分离架构
- [[microservices]] — 微服务架构
- [[摘要-springboot4-security7-vue3-best-practice]] — SpringBoot 4 最佳实践
- [[摘要-springboot3]] — Spring Boot 3 教程
- [[摘要-spring-cloud-alibaba]] — Spring Cloud Alibaba 笔记
- [[摘要-springboot-startup-flow]] — Spring Boot 启动流程源码解析
- [[摘要-spring-boot-4.1-发布]] — Spring Boot 4.1.0 新特性详解
- [[摘要-springboot获取真实客户端ip]] — SpringBoot 获取真实客户端 IP 方案
- [[摘要-总结一次线上事故的惨痛教训]] — 接口类型变更导致P0事故教训
- [[摘要-企业智能招聘系统]] — 来源（Spring Boot 4.1 + Java 25 虚拟线程微服务实战）
- [[虚拟线程]] — Java 25 高并发 IO 利器
- [[ConfigurationProperties]] — 配置绑定注解（支持 Enum 类型字段）
- [[摘要-优雅使用Enum提升SpringBoot配置管理效率]] — Enum + @ConfigurationProperties 配置管理实战
