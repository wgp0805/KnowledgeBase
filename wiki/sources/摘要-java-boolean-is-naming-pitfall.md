---
title: "摘要-java-boolean-is-naming-pitfall"
type: source
tags: [Java, JavaBean, 序列化, 面试题, 避坑]
sources: [raw/01-articles/Java 布尔属性 is 命名序列化大坑｜阿里面试真题文档.md]
last_updated: 2026-08-04
---

## 核心摘要
阿里二面真题：DBA 要求数据库布尔字段带 `is_` 前缀（如 `is_deleted`），但 Java POJO 中不能直接定义 `Boolean isDeleted`。依据 JavaBean 规范，IDE 生成 getter/setter 会造成名称错位（boolean 基础类型生成 `isDeleted()`、Boolean 包装类型生成 `getDeleted()`），导致 [[Jackson]]/[[FastJson]] 序列化后字段丢失 `is` 前缀（输出 `{"deleted":true}`），并引发 [[MyBatis]] 字段映射异常、[[Dubbo]] RPC 传输字段丢失。最佳实践：实体属性命名 `deleted`、数据库保留 `is_deleted` 靠驼峰映射；对外接口必须返回 `isDeleted` 时用 `@JsonProperty` 注解。

## 关联连接
- [[javabean-boolean-is-pitfall]] - 核心概念
- [[Jackson]] - 序列化框架
- [[FastJson]] - 序列化框架
- [[MyBatis]] - ORM 映射异常
- [[Dubbo]] - RPC 序列化问题
- [[Java]] - 所属语言
