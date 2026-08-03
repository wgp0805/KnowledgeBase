---
title: "Gson"
type: entity
tags: [JSON, Java, Google]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
Gson 是 Google 开源的轻量级 Java JSON 处理库，以功能简洁、攻击面可控著称，适合普通 JSON 转换和小型项目。

## 关键信息
- 主动禁止反序列化 `java.lang.Class`，安全性较好
- 2022 年出现 1 项高危反序列化问题，主要影响为 DoS
- 缺点：已进入维护模式，在 Spring Boot 中的扩展能力不如 Jackson
- 定位：简单工具类项目首选，Spring Boot 项目推荐仍用 Jackson

## 关联连接
- [[Jackson]] — 竞品，Spring Boot 默认方案
- [[FastJson]] — 竞品，阿里 JSON 库
- [[程序汪]] — 来源作者
- [[摘要-spring-boot-json-security]] — 来源
