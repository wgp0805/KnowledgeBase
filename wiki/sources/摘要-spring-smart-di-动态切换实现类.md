---
title: "摘要-spring-smart-di-动态切换实现类"
type: source
tags: [Spring, 依赖注入, 动态切换, SPI, 服务商切换]
sources: [raw/01-articles/Spring-Smart-DI 动态切换实现类，很不错！.md]
last_updated: 2026-09-01
---

## 核心摘要
`spring-smart-di` 是对 Spring `@Autowired` 注解的创新性扩展，允许用户自定义 Autowired 注入逻辑。其核心注解 `@AutowiredProxySPI` 通过注入代理对象实现"动态切换服务提供商"：每次执行时实时读取配置点（环境变量/数据库/Nacos）中的当前服务商标识，再路由到对应实现类，配置变更即时生效无需重启。配套的 `@EnvironmentProxySPI` 用于声明环境变量配置点，`@BeanAliasName` 为实现类定义别名；若需自定义配置来源（如数据库），可实现 `@ProxySPI` 注解 + `AnnotationProxyFactory` 掐口。

## 关键信息
- **依赖坐标**：`io.github.burukeyou:spring-smart-di-all:0.2.0`
- **启用方式**：配置类标注 `@EnableSmartDI`
- **核心注解**：
  - `@EnvironmentProxySPI("${sms.impl}")` — 标注接口，声明从环境变量取实现类标识
  - `@BeanAliasName("某腾短信服务")` — 标注实现类，定义可读别名
  - `@AutowiredProxySPI` — 标注字段，注入动态代理对象
- **配置值支持**：`@BeanAliasName` 值 / `@Component` 值 / 全路径类名
- **自定义配置点**：实现 `AnnotationProxyFactory<T>` 接口，通过 `@ProxySPI` 注解指定工厂类，可从数据库等任意数据源获取配置
- **运行机制**：注入的是代理对象，每次调用先实时获取当前实现类再执行，配置变更无需重启
- **典型场景**：多短信服务商切换、多支付通道切换、规避单点服务商故障、按成本灵活切换

## 关联连接
- [[SpringSmartDI]] — 本文介绍的开源库实体
- [[DynamicImplementationSwitching]] — 动态切换实现类的核心概念
- [[Spring]] — Spring 框架
- [[SpringBoot]] — Spring Boot 框架
- [[Nacos]] — 可作为配置点的配置中心
- [[Autowired]] — 被 spring-smart-di 扩展的注解
