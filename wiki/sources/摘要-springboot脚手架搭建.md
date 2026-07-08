---
title: "SpringBoot 脚手架搭建"
type: source
tags: [SpringBoot, 脚手架, 异常处理, AOP, 跨域, Swagger, 统一响应]
sources: [raw/01-articles/如何搭建漂亮的 SpringBoot 脚手架？.md]
last_updated: 2026-07-08
---

## 核心摘要

该资料介绍如何搭建一套规范、可复用的 [[SpringBoot]] 脚手架，涵盖项目初始化、版本管理与核心基础组件。文章强调环境搭建与版本依赖是开发中最大的痛点，并指出 [[Maven]] 在解决依赖冲突中的作用。

### 版本管理的教训

文章以 [[Kafka]] 为例说明版本适配陷阱：生产环境 kafka-server 为 0.11 版本，而客户端为 3.0.4 版本，虽与 [[SpringBoot]] 版本适配，却与 server 版本不适配，导致 `UnsupportedVersionException`。核心教训是测试环境与生产环境的 server 版本必须保持一致。

### 脚手架核心组件

1. **全局异常处理**：使用 `@RestControllerAdvice` + `@ExceptionHandler` 统一捕获 `MethodArgumentNotValidException` 等校验异常，封装为统一响应体返回，并设置 HTTP 状态码。
2. **日志 AOP**：通过 `@Aspect` 切面拦截 Controller 层，`@Before` 记录请求 URI 与参数，`@AfterReturning` 记录返回结果，排除 `MultipartFile`/`HttpServletRequest` 等非业务参数。
3. **跨域配置**：`GlobalCorsConfig` 通过 `CorsFilter` 允许所有域名、头信息、请求方法跨域，并允许携带 cookie。
4. **Swagger 配置**：`@EnableOpenApi` + `Docket`（OAS_30）配置接口文档，按 basePackage 扫描。
5. **统一响应体**：`ResponseResult<T>` 泛型包装类，包含 `code`/`message`/`data`，提供 `success()`/`failed()` 静态工厂方法。

### 推荐工具与中间件

- 内存版中间件（用于单元测试隔离）：embedded-redis、mariadb、spring-kafka starter
- [[Hutool]]：Java 工具类库
- [[MyBatisPlus]]：MyBatis 增强
- [[MapStruct]]：编译时对象映射
- [[Redisson]]：Redis 客户端
- [[Druid]]：数据库连接池

## 关联连接

- [[SpringBoot]]
- [[Maven]]
- [[Kafka]]
- [[Redis]]
- [[MySQL]]
- [[Hutool]]
- [[MyBatisPlus]]
- [[MapStruct]]
- [[Redisson]]
- [[Druid]]
- [[Java]]
