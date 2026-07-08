---
title: "SLF4J"
type: entity
tags: [Java, 日志门面, 接口, 抽象层]
sources: [raw/01-articles/logback VS log4j2：一倍左右的性能差异，是时候注意了！.md]
last_updated: 2026-07-08
---

## 定义

SLF4J（Simple Logging Facade for Java）是 Java 日志门面接口，为各种日志框架（[[Logback]]、[[Log4j2]] 等）提供统一的抽象层，使应用代码与具体日志实现解耦。

## 关键信息

- **定位**：日志门面（Facade），仅定义接口，不提供实现
- **核心 API**：`Logger`、`LoggerFactory.getLogger()`，推荐声明为 `private static final`
- **实现绑定**：通过绑定模块将接口桥接到具体实现
  - `logback-classic`：[[Logback]] 原生实现 SLF4J
  - `log4j-slf4j2-impl`：将 [[Log4j2]] 绑定到 SLF4J
- **易用性**：配合 [[Lombok]] 的 `@Slf4j` 注解，可省去手动声明 Logger，代码最简洁（推荐方式）
- **抽象价值**：应用代码只依赖 SLF4J 接口，切换日志框架只需更换绑定依赖，无需修改业务代码
- **与 Log4j 的关系**：log4j 是早期的日志实现，SLF4J 后来成为统一门面标准

## 关联连接

- [[Logback]]
- [[Log4j2]]
- [[日志框架]]
- [[Lombok]]
- [[SpringBoot]]
- [[Java]]
- [[摘要-logback-vs-log4j2]]
