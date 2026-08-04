---
title: "Dubbo"
type: entity
tags: [Java, RPC, 微服务, 序列化]
sources: [raw/01-articles/Java 布尔属性 is 命名序列化大坑｜阿里面试真题文档.md]
last_updated: 2026-08-04
---

## 定义
Dubbo 是阿里巴巴开源的高性能 Java RPC 框架，用于微服务间的远程过程调用。RPC 通信依赖 JavaBean 规范进行序列化，属性名与 getter 不匹配会导致跨服务传输字段丢失、反序列化失败。

## 关键信息
- **核心作用**：跨服务 RPC 通信，依赖 JavaBean 反射进行序列化/反序列化
- **序列化陷阱**：当 POJO 布尔属性命名为 `isXxx` 时，JavaBean 规范导致 getter 名错位（boolean 基础类型生成 `isXxx()`、Boolean 包装类型生成 `getXxx()`），RPC 传输时字段名丢失 `is` 前缀
- **影响范围**：所有依赖 JavaBean 反射的组件（[[Jackson]]、[[FastJson]]、[[MyBatis]]、Dubbo）均受影响

## 关联连接
- [[javabean-boolean-is-pitfall]] - 布尔属性 is 命名序列化陷阱
- [[摘要-java-boolean-is-naming-pitfall]] - 来源
- [[Jackson]] - JSON 序列化框架，同类陷阱
- [[MyBatis]] - ORM 框架，同类映射陷阱
- [[microservices]] - 微服务架构，Dubbo 的应用场景
