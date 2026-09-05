---
title: "MapStruct"
type: entity
tags: [Java, 对象映射, 代码生成, 编译时, DTO转换]
sources: [raw/01-articles/如何搭建漂亮的 SpringBoot 脚手架？.md]
last_updated: 2026-07-08
---

## 定义

MapStruct 是一个 Java 对象映射代码生成库，在编译时基于注解处理器自动生成 DTO 与实体之间的转换代码，无需运行时反射。

## 关键信息

- **工作原理**：基于 JSR 269 注解处理器，在编译阶段生成类型安全、高性能的映射代码
- **核心优势**：编译时生成，无运行时反射开销；生成的代码可读、可调试
- **典型场景**：Entity ↔ DTO 转换、VO ↔ BO 转换、分层架构间的对象映射
- **官网**：https://mapstruct.org/
- **使用方式**：定义 Mapper 接口并标注 `@Mapper`，MapStruct 自动生成实现类
- **配合使用**：常与 [[Lombok]] 共同使用（需注意注解处理器顺序），是 [[SpringBoot]] 脚手架的常用组件

## 关联连接

- [[Java]]
- [[SpringBoot]]
- [[Lombok]]
- [[摘要-springboot脚手架搭建]]
