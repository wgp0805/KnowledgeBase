---
title: "TypeHandler"
type: concept
tags: [MyBatis, 类型转换]
sources: [raw/01-articles/MyBatis-Plus 3.5.15 已全面支持 Spring Boot 4.0 及 Jackson 3.0.md]
last_updated: 2026-09-03
---

## 定义
TypeHandler 是 MyBatis 的类型处理器，负责 Java 类型与 JDBC 类型之间的双向转换。在 MyBatis-Plus 中，用于处理 JSON 列与 Java 对象的序列化/反序列化。

## 关键信息
- **JacksonTypeHandler**：Jackson 2 的类型处理器，核心包 `com.fasterxml.jackson`
- **Jackson3TypeHandler**：Jackson 3 的类型处理器，核心包 `tools.jackson`
- 使用方式：在实体字段上通过 `@TableField(typeHandler = Jackson3TypeHandler.class)` 指定
- 需配合 `@TableName(autoResultMap = true)` 才能正确反序列化

## 关联连接
- [[MyBatisPlus]] — 增强工具
- [[Jackson]] — JSON 处理库
- [[Jackson3TypeHandler]] — Jackson 3 具体实现
- [[autoResultMap]] — 配合使用的实体配置
- [[摘要-mybatis-plus-3515-springboot4-jackson3]] — 来源
