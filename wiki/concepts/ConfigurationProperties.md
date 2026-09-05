---
title: "ConfigurationProperties"
type: concept
tags: [SpringBoot, 配置管理, 注解]
sources:
  - raw/01-articles/优雅使用 Enum 提升 SpringBoot 配置管理效率！.md
last_updated: 2026-08-17
---

## 定义
`@ConfigurationProperties` 是 Spring Boot 提供的配置绑定注解，用于将外部化配置（`application.yml`/`application.properties`）中以指定前缀开头的属性批量绑定到 Java POJO 的字段上，实现类型安全、结构化的配置管理。相比 `@Value` 单值注入，它支持整组属性、嵌套结构、`Map`/`List`/`Enum` 等复杂类型，并配合 `@Component` 注册为 Bean 在容器中复用。

## 关键信息
- **核心用法**：类上标注 `@ConfigurationProperties(prefix="app")`，字段名与配置 key 松散绑定（驼峰/下划线/kebab-case 互通）
- **类型转换**：Spring Boot 自动将 yml 字符串转换为字段类型，包括 `int`、`boolean`、`List`、`Map` 以及 **Enum**（按枚举常量名匹配）
- **嵌套结构**：通过静态内部类表达层级配置（如 `app.user-type.admin` → `AppConfig.UserType.admin`）
- **校验支持**：可配合 `spring-boot-starter-validation` + JSR-303 注解（`@NotNull`、`@Min` 等）做配置校验
- **常见搭配**：`@Data`（Lombok 自动生成 setter）、`@Component`（注册 Bean）

## 与 Enum 结合的配置模式
将 POJO 字段类型声明为枚举类型，yml 中填写枚举常量名，Spring Boot 自动完成字符串→枚举的转换。优势：
1. 配置值受枚举约束，非法值启动即失败（fail-fast）
2. 业务代码中拿到的是枚举实例，可直接调用其方法（如 `getDescription()`）
3. 避免魔法字符串在配置与代码间散落

## 关联连接
- [[SpringBoot]] — 所属框架
- [[Enum]] — 配合实现类型安全配置
- [[Lombok]] — `@Data` 简化 setter
- [[摘要-优雅使用Enum提升SpringBoot配置管理效率]] — 来源
- [[摘要-SpringBoot优雅的加载配置文件的几种方式]] — 配置加载方式综述
