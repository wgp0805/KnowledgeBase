---
title: "SpringBoot"
type: entity
tags: [框架, Java, Spring]
sources:
  - raw/01-articles/springboot整合mybatisPlus.md
  - raw/01-articles/springboot整合redis.md
  - raw/01-articles/springboot整合RocketMq.md
  - raw/01-articles/SpringBoot-Aop的使用.md
  - raw/01-articles/SpringBoot接收参数的几种常用方式.md
  - raw/01-articles/SpringBoot优雅的加载配置文件的几种方式.md
  - raw/01-articles/SpringBoot整合SpringSecurity及框架的简单使用.md
  - raw/01-articles/理解Spring中的ApplicationListener与ApplicationRunner区别及使用场景.md
  - raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md
  - raw/02-papers/springboot3.pdf
  - raw/02-papers/Spring Cloud Alibaba笔记.pdf
last_updated: 2026-05-22
---

## 定义
Spring Boot 是 Spring 框架的自动配置扩展，简化了 Spring 应用的初始搭建和开发过程，遵循"约定优于配置"原则。

## 关键信息
- 提供 Starter 依赖管理简化 Maven/Gradle 配置
- 内置嵌入式 Tomcat/Jetty/Undertow 服务器
- 自动配置（Auto-Configuration）机制根据 classpath 依赖自动配置 Bean
- 提供 @SpringBootApplication 组合注解
- 支持 application.yml/properties 多层次配置
- 通过 @ConfigurationProperties 绑定配置到 POJO
- 支持 profile 多环境切换

### SpringBoot 4 新特性
- 基于 Spring Framework 7 和 Java 21+
- 声明式 HTTP 客户端（@HttpExchange）
- 结构化并发支持
- 虚拟线程支持（I/O 密集型场景性能提升）
- 启动速度提升 30%

## 关联连接
- [[Spring]] — 基础框架
- [[SpringMVC]] — Web MVC 框架
- [[MyBatisPlus]] — ORM 整合
- [[Redis]] — 缓存整合
- [[RocketMQ]] — 消息队列整合
- [[SpringSecurity]] — 安全框架整合
- [[AOP]] — 面向切面编程
- [[frontend-backend-separation]] — 前后端分离架构
- [[microservices]] — 微服务架构
- [[摘要-springboot4-security7-vue3-best-practice]] — SpringBoot 4 最佳实践
- [[摘要-springboot3]] — Spring Boot 3 教程
- [[摘要-spring-cloud-alibaba]] — Spring Cloud Alibaba 笔记
