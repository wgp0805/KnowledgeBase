---
title: "RestClient"
type: entity
tags: [Spring, HTTP, Java]
sources: []
last_updated: 2026-06-02
---

## 定义
Spring 6.1+/Spring Boot 3.2+ 引入的现代 HTTP 客户端，替代老旧的 RestTemplate，提供流畅的 API 设计和更好的类型安全。

## 关键信息
- Spring Framework 6.1+ 官方推荐的 HTTP 客户端
- 流畅 API 设计，支持链式调用
- 支持同步和异步请求
- 底层可切换实现：JDK HttpClient、Apache HttpClient、OkHttp
- 与 RestTemplate 相比：不可变配置、更简洁的 API、原生支持泛型

## 关联连接
- [[Spring]] — 所属框架
- [[SpringBoot]] — 集成使用
- [[agent-skill-java-spring-framework]] — 强制使用 RestClient 替代 RestTemplate 的 Skill
