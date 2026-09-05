---
title: "DynamicImplementationSwitching"
type: concept
tags: [Spring, 依赖注入, SPI, 动态代理, 运行时切换]
sources: [raw/01-articles/Spring-Smart-DI 动态切换实现类，很不错！.md]
last_updated: 2026-09-01
---

## 定义
动态切换实现类是指在运行时根据配置点（环境变量、数据库、配置中心等）动态决定接口的具体实现类，且配置变更即时生效无需重启应用。`spring-smart-di` 通过注入代理对象实现该模式：每次方法调用前实时读取配置点中的实现类标识，再路由执行对应 Bean。

## 关键信息
- **核心机制**：代理对象拦截调用 → 实时读取配置点 → 路由到对应实现类 → 执行业务逻辑
- **配置点来源**：环境变量（`@EnvironmentProxySPI`）、Nacos/Apollo 等配置中心、数据库（自定义 `@ProxySPI` + `AnnotationProxyFactory`）
- **实现类标识**：支持 `@BeanAliasName` 别名、Spring `@Component` 值、全限定类名
- **典型场景**：多短信服务商切换、多支付通道切换、规避单点服务商故障、按成本灵活切换
- **优势**：零侵入业务代码、配置即时生效、无需重启、兼容 Spring 原生 `@Autowired` 语义

## 关联连接
- [[SpringSmartDI]] — 实现该模式的开源库
- [[摘要-spring-smart-di-动态切换实现类]] — 来源
- [[Spring]] — 所属生态
- [[SpringBoot]] — 应用场景
- [[Nacos]] — 常用配置点
- [[Autowired]] — 被扩展的注解
- [[SPI]] — 服务提供商接口模式