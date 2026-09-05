---
title: "java.time"
type: entity
tags: [Java包, 日期时间, 现代API]
sources: [raw/01-articles/公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！.md]
last_updated: 2026-09-03
---

## 定义
Java 8引入的现代日期时间API包，提供了不可变、线程安全、时区友好的日期时间处理类。

## 关键信息
- **核心优势**：不可变性、线程安全、时区友好、命名清晰
- **核心类**：LocalDateTime（日期时间）、LocalDate（日期）、LocalTime（时间）、Instant（时间戳）、ZonedDateTime（带时区的日期时间）
- **工具类**：DateTimeFormatter（格式化）、Period（日期段）、Duration（时间段）
- **设计理念**：不可变性、明确的职责分离、清晰的命名

## 关联连接
- [[摘要-公司空降一个cto禁止在项目中使用date类]] — 来源
- [[Date]] — 替代目标
- [[LocalDateTime]] — 核心类
- [[Instant]] — 核心类
- [[API迁移]] — 应用场景