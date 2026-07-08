---
title: "Logback"
type: entity
tags: [Java, 日志框架, SLF4J, SpringBoot默认]
sources: [raw/01-articles/logback VS log4j2：一倍左右的性能差异，是时候注意了！.md]
last_updated: 2026-07-08
---

## 定义

Logback 是一个 Java 日志框架，作为 [[SLF4J]] 接口的原生实现，是 [[SpringBoot]] 的默认日志框架。

## 关键信息

- **定位**：[[SLF4J]] 的原生实现，由 SLF4J 同一作者开发
- **SpringBoot 默认**：[[SpringBoot]] 开箱即用 Logback，无需额外配置
- **配置文件**：`logback.xml`，放置于 `src/main/resource/`
- **核心组件**：`ConsoleAppender`（控制台）、`RollingFileAppender`（滚动文件）、`FixedWindowRollingPolicy`、`SizeBasedTriggeringPolicy`
- **性能**：性能约为 [[Log4j2]] 的一半，在高并发日志场景下劣势明显
- **测试版本**：1.4.14（基准测试所用版本）
- **性能瓶颈**：日志输出能力不随线程数线性增长，打印方法名和行号会显著降低效率

## 关联连接

- [[Log4j2]]
- [[SLF4J]]
- [[日志框架]]
- [[SpringBoot]]
- [[Lombok]]
- [[Java]]
- [[摘要-logback-vs-log4j2]]
