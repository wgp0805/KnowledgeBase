---
title: "摘要-jackson3升级详解"
type: source
tags: [来源, Jackson, Java, JSON, 升级]
sources: [raw/01-articles/2026-09-05 - 为什么越来越多人使用 Jackson 3 ？.md]
last_updated: 2026-09-05
---

## 核心摘要
Jackson 3.0 正式发布（2025年10月），距离上一次大版本跨越已13年。核心变化：最低要求 Java 17、包名换成 tools.jackson、Mapper 变成不可变的、异常不再强制 catch。与 2.x 可同时存在于 classpath，支持渐进式迁移。Spring 已公开 Jackson 3 支持，OpenRewrite 提供 2→3 迁移配方。3.1 是第一个 LTS 版本，日常痛点按住：Mapper 不可变、日期默认 ISO-8601、Record 和 java.time 开箱即用。

## 关联连接
- [[Jackson]] — Java JSON 处理库
- [[Jackson3]] — Jackson 3.x 版本
- [[不可变性]] — Mapper 不可变设计
- [[Java17]] — Jackson 3 最低要求
- [[SpringBoot]] — Spring Boot 集成
- [[Record]] — Java Record 类型
- [[java.time]] — Java 日期时间 API
- [[OpenRewrite]] — 自动化迁移工具
