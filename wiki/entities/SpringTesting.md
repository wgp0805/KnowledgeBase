---
title: "SpringTesting"
type: entity
tags: [Spring, 测试, JUnit]
sources: []
last_updated: 2026-05-29
---

## 定义
Spring Testing 是 Spring 框架提供的测试支持模块，通过 `spring-boot-starter-test` 提供单元测试和集成测试能力，内置 JUnit 5、Mockito、AssertJ 等测试工具。

## 关键信息
- @SpringBootTest：启动完整 Spring 容器进行集成测试
- @WebMvcTest：仅加载 MVC 层的切片测试
- @DataJpaTest：仅加载 JPA 层的切片测试
- MockMvc：模拟 HTTP 请求测试 Controller
- @MockBean：Mock Spring Bean
- TestRestTemplate / WebTestClient：集成测试 HTTP 客户端
- 测试切片（Test Slices）：按层加载，启动更快

## 关联连接
- [[SpringBoot]] — 测试框架基础
- [[Spring]] — 核心框架
- [[spring-testing-skills]] — AI 测试技能库
