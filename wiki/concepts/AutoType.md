---
title: "AutoType"
type: concept
tags: [JSON, 安全, 反序列化]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
AutoType 是 JSON 反序列化库（如 FastJson、Jackson）中自动类型解析机制，允许 JSON 字符串指定反序列化的 Java 类型，是反序列化 RCE 漏洞的核心根源。

## 关键信息
- FastJson：`@type` 字段指定类型，历史上多轮 RCE 漏洞根因
- FastJson2：AutoType 默认关闭，但仍需持续加固
- Jackson：多态反序列化（Polymorphic Type）的启用基于 `ObjectMapper.enableDefaultTyping()`，默认关闭
- 安全实践：禁止全局 AutoType，固定 DTO 避免外部控制类型

## 关联连接
- [[FastJson]] — AutoType 导致多轮 RCE
- [[FastJson2]] — AutoType 默认关闭
- [[Jackson]] — 多态反序列化
- [[SafeMode]] — FastJson 安全对抗模式
- [[多态反序列化]] — Jackson 中的对应概念
- [[摘要-spring-boot-json-security]] — 来源
