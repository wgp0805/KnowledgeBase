---
title: "RestTemplate"
type: entity
tags: [Spring, HTTP, Java, 弃用]
sources: ["raw/09-archive/SpringBoot4.2正式发布，人麻了！.md"]
last_updated: 2026-11-24
---

## 定义
RestTemplate 是 Spring 自 2009 年起提供的同步 HTTP 客户端，长期是 Java 项目调用外部接口的事实标准；在 Spring Framework 7.1 被标记为"即将移除"，Spring Boot 4.2 起整套支持基础设施被弃用（**弃用不等于移除**，代码仍能编译运行，只是有 warning）。

## 关键信息
- **4.2 中被弃用的清单**：`RestTemplateAutoConfiguration`、`RestTemplateObservationAutoConfiguration`、`RestTemplateBuilder`、`RestTemplateBuilderConfigurer`、`RestTemplateCustomizer`，以及测试用的 `TestRestTemplate`
- **被弃用的技术原因**：基于阻塞式 I/O，线程调远程接口就卡住等待；在虚拟线程与 WebFlux 普及后资源利用率吃亏。官方替代是 [[RestClient]]（流式/链式 API，请求构建、拦截器、错误处理可组合）与 `RestTestClient`
- **现实成本**：老项目 HTTP 调用散落在多个 Service，迁一个不难，迁几十个是体力活 → 建议分批：新代码先迁，老代码排期
- **迁移示意**：
  - GET：`restTemplate.getForObject("/users/{id}", User.class, id)` → `restClient.get().uri("/users/{id}", id).retrieve().body(User.class)`
  - POST：`restClient.post().uri("/users").body(user).retrieve().body(User.class)`
  - 错误处理：`.retrieve().onStatus(HttpStatusCode::is4xxClientError, (req, res) -> { throw new UserNotFoundException(id); })`
  - 测试：`TestRestTemplate` → `RestTestClient`（`exchange().expectStatus().isOk().expectBody(...)`）
- **时间线**：Spring Boot 4.1.x 开源支持到 2027-07-31，"先不升"有保质期

## 关联连接
- [[RestClient]] — 官方替代方案
- [[SpringBoot]] — 4.2 弃用决策所在版本
- [[Spring]] — 所属框架
- [[虚拟线程]] — 弃用的技术背景
- [[摘要-springboot4-2发布]] — 来源
