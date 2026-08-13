---
title: "JavaBean规范"
type: concept
tags: [Java, JavaBean, 规范, 序列化]
sources:
  - wiki/sources/摘要-java-boolean-is-serialization-pitfall.md
last_updated: 2026-08-13
---

## 定义
JavaBean 规范是 Java 可重用组件的编码约定，定义了类的标准结构，使组件能被反射、序列化、依赖注入框架（Spring/MyBatis/JSP）统一处理。

## 关键信息
- **无参构造器**：必须提供 public 无参构造，供反射实例化
- **属性私有 + 公共访问器**：字段 private，通过 `getXxx()` / `setXxx()` 访问，boolean 用 `isXxx()`
- **可序列化**：实现 `java.io.Serializable`，提供 `serialVersionUID`
- **事件机制**（完整 Bean）：支持 PropertyChange/VetoableChange 监听
- **序列化陷阱**：boolean 字段命名以 `is` 开头时，反射框架按 `isXxx`/`getXxx` 推断 getter 易错位（见来源），需注意

## 关联连接
- [[摘要-java-boolean-is-serialization-pitfall]] — 引用本规范的序列化陷阱来源
