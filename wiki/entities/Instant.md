---
title: "Instant"
type: entity
tags: [Java类, 时间戳, java.time]
sources: [raw/01-articles/公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！.md]
last_updated: 2026-09-03
---

## 定义
java.time包中表示时间戳（时间的一个瞬间）的类，是Date类的直接替代品。

## 关键信息
- **核心特性**：不可变性、线程安全、时区无关
- **适用场景**：表示时间戳，类似于Date的原始用途
- **创建方式**：Instant.now()、Instant.ofEpochMilli()、Instant.parse()
- **常用方法**：isAfter()、isBefore()、plus()、minus()、toEpochMilli()
- **转换方法**：Date.from()、LocalDateTime.atZone()、atOffset()

## 关联连接
- [[摘要-公司空降一个cto禁止在项目中使用date类]] — 来源
- [[java.time]] — 所属包
- [[Date]] — 替代目标
- [[LocalDateTime]] — 相关类
- [[ZonedDateTime]] — 相关类