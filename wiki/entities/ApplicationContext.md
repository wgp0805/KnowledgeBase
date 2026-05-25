---
title: "ApplicationContext"
type: entity
tags: [Spring, IoC, 工厂模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
ApplicationContext 是 BeanFactory 的超集，除了创建 Bean 外，还集成了国际化、事件发布、资源加载等企业级功能。我们平时用的 `@SpringBootApplication` 启动后拿到的就是它。

## 关键信息
- BeanFactory 的超集：包含 BeanFactory 的所有功能
- 企业级功能：国际化（i18n）、事件发布、资源加载、环境抽象等
- 常用实现：ClassPathXmlApplicationContext（XML配置）、AnnotationConfigApplicationContext（注解配置）
- Spring Boot 中的应用：SpringApplication.run() 返回的就是 ApplicationContext 实例
- 预加载：默认在启动时就创建所有单例 Bean（与 BeanFactory 的懒加载不同）

## 关联连接
- [[Spring]] — 所属框架
- [[BeanFactory]] — ApplicationContext 的父接口
- [[工厂模式]] — ApplicationContext 体现的设计模式
- [[ApplicationEvent]] — ApplicationContext 的事件发布功能
- [[摘要-spring-design-patterns]] — 来源文章