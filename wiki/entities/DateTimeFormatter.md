---
title: "DateTimeFormatter"
type: entity
tags: [Java类, 日期格式化, java.time]
sources: [raw/01-articles/公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！.md]
last_updated: 2026-09-03
---

## 定义
java.time包中用于日期时间格式化和解析的类，是SimpleDateFormat的现代替代品。

## 关键信息
- **核心优势**：不可变性、线程安全、预定义格式、自定义格式
- **预定义格式**：ISO_LOCAL_DATE、ISO_LOCAL_TIME、ISO_LOCAL_DATE_TIME等
- **创建方式**：DateTimeFormatter.ofPattern()、DateTimeFormatter.ISO_LOCAL_DATE等
- **常用方法**：format()、parse()、withLocale()、withZone()
- **线程安全**：DateTimeFormatter实例是线程安全的，可以被多个线程共享

## 关联连接
- [[摘要-公司空降一个cto禁止在项目中使用date类]] — 来源
- [[java.time]] — 所属包
- [[SimpleDateFormat]] — 替代目标
- [[LocalDateTime]] — 配合使用
- [[API迁移]] — 应用场景