---
title: "SpringSmartDI"
type: entity
tags: [Spring, 依赖注入, 开源库, SPI]
sources: [raw/01-articles/Spring-Smart-DI 动态切换实现类，很不错！.md]
last_updated: 2026-09-01
---

## 定义
`spring-smart-di` 是一个扩展 Spring `@Autowired` 注入逻辑的开源库，由 `io.github.burukeyou` 发布。它通过代理对象机制实现"动态切换服务提供商"，让 `@Autowired` 注入的实现类可根据配置点（环境变量/数据库/Nacos）实时切换，配置变更即时生效无需重启。

## 关键信息
- **Maven 坐标**：`io.github.burukeyou:spring-smart-di-all:0.2.0`
- **启用注解**：`@EnableSmartDI`（标注在配置类上）
- **核心注解**：
  - `@SmartAutowired` — 自定义 Autowired 注入逻辑
  - `@AutowiredProxySPI` — 注入动态代理对象，按配置路由实现类
  - `@EnvironmentProxySPI` — 声明环境变量配置点
  - `@BeanAliasName` — 为 Bean 定义可读别名
  - `@ProxySPI` — 自定义 SPI 注解元注解，指定 `AnnotationProxyFactory`
- **扩展点**：实现 `AnnotationProxyFactory<T>` 接口可自定义配置来源（如数据库）
- **运行机制**：注入代理对象，每次调用实时读取配置 → 路由到对应实现类 → 执行
- **配置值支持**：`@BeanAliasName` 值 / `@Component` 值 / 全路径类名

## 关联连接
- [[摘要-spring-smart-di-动态切换实现类]] — 来源
- [[DynamicImplementationSwitching]] — 核心实现的概念
- [[Spring]] — 所属生态
- [[SpringBoot]] — 应用场景
- [[Nacos]] — 常用配置点
- [[Autowired]] — 被扩展的注解
