---
title: "摘要-java-boolean-is-serialization-pitfall"
type: source
tags: [Java, 序列化, JavaBean, 面试]
sources: [raw/01-articles/Java 布尔属性 is 命名序列化大坑｜阿里面试真题文档.md]
last_updated: 2026-08-04
---

## 核心摘要
Java 布尔类型属性若以 `isXXX` 命名，会触发 JavaBean 规范与序列化框架之间的兼容性问题。IDE 根据 JavaBean 规范自动生成的 getter/setter 会导致 Jackson/FastJSON 序列化后的 JSON 字段名丢失 `is` 前缀，同时引发 MyBatis 驼峰映射异常和 RPC 传输字段丢失。标准解决方案：实体属性命名为 `deleted`（不用 `is` 前缀），数据库保留 `is_deleted`，通过 MyBatis 驼峰自动映射；若业务要求 JSON 返回 `isDeleted`，使用 `@JsonProperty` 注解显式指定。

## 关联连接
- [[JavaBean规范]] — 核心概念，getter/setter 生成规则
- [[Java]] — 所属语言生态
- [[Jackson]] — 序列化框架，@JsonProperty 注解
- [[MyBatis]] — ORM 框架，驼峰自动映射
- [[FastJson]] — 序列化框架，同样受影响