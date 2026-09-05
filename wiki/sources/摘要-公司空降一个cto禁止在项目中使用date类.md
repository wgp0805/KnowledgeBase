---
title: "摘要-公司空降一个cto禁止在项目中使用date类"
type: source
tags: [来源, 原始文件, Java, 日期时间]
sources: [raw/01-articles/公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！.md]
last_updated: 2026-09-03
---

## 核心摘要
本文介绍了Java中Date类的设计缺陷，包括名称误导性、非最终类、可变性、隐式时区使用、从0开始的月份编号等问题。文章解释了为什么要迁移到java.time包（代码缺陷扫描规则强制要求），并详细展示了如何将Date类的各种方法改造为java.time包的现代API，包括日期格式化、日期加减、获取星期几、获取一天开始/结束时间等。

## 关联连接
- [[Date]] — 需要废弃的类
- [[java.time]] — 现代API包
- [[LocalDateTime]] — 核心类
- [[Instant]] — 时间戳类
- [[DateTimeFormatter]] — 格式化类
- [[API迁移]] — 核心概念
- [[不可变性]] — 设计原则
- [[时区处理]] — 技术要点