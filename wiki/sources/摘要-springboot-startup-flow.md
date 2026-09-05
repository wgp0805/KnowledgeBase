---
title: "摘要-springboot-startup-flow"
type: source
tags: [SpringBoot, 启动流程, 源码, 面试]
sources: [raw/01-articles/得物二面：SpringBoot 内部的启动流程是怎样的？我：没研究过.md]
last_updated: 2026-05-25
---

## 核心摘要

本文深入解析Spring Boot内部启动流程的7个核心步骤。从`SpringApplication.run()`开始：创建SpringApplication对象→推断应用类型→加载ApplicationContextInitializer和ApplicationListener→创建ApplicationContext→执行BeanDefinition扫描→自动配置生效→执行CommandLineRunner。重点讲解了SPI机制加载扩展点、`@EnableAutoConfiguration`自动配置原理、`refresh()`方法的12个步骤（其中第9步onRefresh()启动内嵌Tomcat）。

## 关联连接
- [[SpringBoot]] — Spring 自动配置框架
- [[Spring]] — Java 企业级应用框架
- [[SpringMVC]] — Web MVC 框架
