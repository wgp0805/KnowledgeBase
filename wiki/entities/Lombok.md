---
title: "Lombok"
type: entity
tags: [Java, 开发工具, 注解]
sources: []
last_updated: 2026-05-29
---

## 定义
Lombok 是一个 Java 编译时注解处理器，通过注解自动生成 getter/setter/构造器/toString/equals/hashCode 等样板代码，减少冗余代码编写。

## 关键信息
- `@Data`：自动生成 getter/setter/toString/equals/hashCode
- `@Builder`：建造者模式
- `@Slf4j`：自动生成日志对象
- `@AllArgsConstructor` / `@NoArgsConstructor`：全参/无参构造器
- `@Value`：不可变对象（所有字段 private final）
- 编译时处理：不增加运行时开销
- IDE 支持：需安装 Lombok 插件

## 关联连接
- [[Java]] — 所属语言生态
- [[SpringBoot]] — 常配合使用
- [[设计模式]] — Builder 模式实现
