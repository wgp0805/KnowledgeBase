---
title: "autoResultMap"
type: concept
tags: [MyBatisPlus, 配置]
sources: [raw/01-articles/MyBatis-Plus 3.5.15 已全面支持 Spring Boot 4.0 及 Jackson 3.0.md]
last_updated: 2026-09-03
---

## 定义
autoResultMap 是 MyBatis-Plus 的 `@TableName` 注解属性，设为 `true` 时会自动应用 ResultMap，使得使用了 TypeHandler 的字段能正确反序列化。

## 关键信息
- 必须设置为 `true`，否则使用了 TypeHandler 的字段查询出来可能是空或原始字符串
- 语法：`@TableName(value = "t_user", autoResultMap = true)`
- 常用于 JSON 列的实体映射场景

## 关联连接
- [[MyBatisPlus]] — 增强工具
- [[TypeHandler]] — 类型处理器
- [[摘要-mybatis-plus-3515-springboot4-jackson3]] — 来源
