---
title: "LocalDateTime"
type: entity
tags: [Java类, 日期时间, java.time]
sources: [raw/01-articles/公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！.md]
last_updated: 2026-09-03
---

## 定义
java.time包中表示没有时区信息的日期和时间的类，是Date类的主要替代品之一。

## 关键信息
- **核心特性**：不可变性、线程安全、无时区信息
- **适用场景**：表示日期和时间，不需要时区信息
- **创建方式**：LocalDateTime.now()、LocalDateTime.of()、LocalDateTime.parse()
- **常用方法**：plusSeconds/Minutes/Hours/Days/Months/Years、with()、format()
- **转换方法**：toLocalDate()、toLocalTime()、atZone()、atInstant()

## 关联连接
- [[摘要-公司空降一个cto禁止在项目中使用date类]] — 来源
- [[java.time]] — 所属包
- [[Date]] — 替代目标
- [[LocalDate]] — 相关类
- [[LocalTime]] — 相关类