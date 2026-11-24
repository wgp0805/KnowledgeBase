---
title: "RestClient"
type: entity
tags: [Spring, HTTP, Java]
sources: ["raw/09-archive/SpringBoot4.2正式发布，人麻了！.md"]
last_updated: 2026-11-24
---

## 定义
Spring 6.1+/Spring Boot 3.2+ 引入的现代 HTTP 客户端，替代老旧的 RestTemplate，提供流畅的 API 设计和更好的类型安全。

## 关键信息
- Spring Framework 6.1+ 官方推荐的 HTTP 客户端
- 流畅 API 设计，支持链式调用
- 支持同步和异步请求
- 底层可切换实现：JDK HttpClient、Apache HttpClient、OkHttp
- 与 RestTemplate 相比：不可变配置、更简洁的 API、原生支持泛型
- **Spring Boot 4.2 起成为官方指定迁移目标**：[[RestTemplate]] 及其整套基础设施（Builder/Configurer/Customizer/Observation、以及测试用的 `TestRestTemplate`）在 4.2 被弃用，官方替代为 RestClient 与 `RestTestClient`；弃用原因是 RestTemplate 基于阻塞式 I/O，在[[虚拟线程]]与 WebFlux 普及后资源利用率吃亏（详见 [[摘要-springboot4-2发布]]）
- 迁移成本提示：新代码应直接用 RestClient；老项目里散落在多个 Service 的 RestTemplate 调用建议分批迁移

## 关联连接
- [[Spring]] — 所属框架
- [[SpringBoot]] — 集成使用（4.2 起正式推荐迁移）
- [[RestTemplate]] — 被替代的旧客户端
- [[摘要-springboot4-2发布]] — 来源（弃用与迁移示例）
- [[agent-skill-java-spring-framework]] — 强制使用 RestClient 替代 RestTemplate 的 Skill
