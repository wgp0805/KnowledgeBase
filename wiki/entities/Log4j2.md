---
title: "Log4j2"
type: entity
tags: [Java, 日志框架, Apache, 高性能, 异步日志, SLF4J]
sources: [raw/01-articles/logback VS log4j2：一倍左右的性能差异，是时候注意了！.md]
last_updated: 2026-07-08
---

## 定义

Log4j2 是 Apache 基金会开发的高性能 Java 日志框架，支持异步日志（Async Logger），性能约为 [[Logback]] 的两倍。

## 关键信息

- **性能优势**：性能约为 [[Logback]] 的两倍，全面优于 Logback
- **异步日志**：基于 LMAX Disruptor 实现异步日志，高并发下吞吐显著领先
- **非 SpringBoot 默认**：需排除 [[SpringBoot]] 默认的 logback 依赖，手动引入
- **依赖组件**：`log4j-core`、`log4j-api`、`log4j-slf4j2-impl`（绑定 [[SLF4J]]）
- **配置文件**：`log4j2.xml`，放置于 `src/main/resource/`
- **核心组件**：`Console`（控制台）、`RollingFile`（滚动文件）、`PatternLayout`、`SizeBasedTriggeringPolicy`、`DefaultRolloverStrategy`
- **测试版本**：2.22.1（基准测试所用版本）
- **选型建议**：高并发、对日志性能敏感的场景推荐使用 Log4j2

## 关联连接

- [[Logback]]
- [[SLF4J]]
- [[日志框架]]
- [[SpringBoot]]
- [[Lombok]]
- [[Java]]
- [[摘要-logback-vs-log4j2]]
