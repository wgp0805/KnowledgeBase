---
title: "SpringDoc"
type: entity
tags: [SpringBoot, OpenAPI, API文档, Swagger]
sources: [raw/09-archive/2026-11-01 - 告别Swagger UI！一款更适合 SpringBoot 的API文档新选择.md]
last_updated: 2026-11-02
---

## 定义

SpringDoc 是专为 Spring Boot 应用设计的库，自动生成符合 OpenAPI 3 规范的 API 文档。通过扫描项目中的控制器、方法注解及配置，动态生成 JSON/YAML/HTML 格式文档，并提供交互式界面（Swagger UI）供查看和测试。

## 关键信息

### 与 Swagger 的关系

Swagger 是 OpenAPI 规范的前身，贡献了 API 设计理念并推动标准化；Swagger UI 用于展示交互式文档。SpringDoc 是 OpenAPI 3 规范的实现工具，天然集成 Swagger UI 作为展示界面——**不是 Swagger 的替代品**，而是 SpringFox 的替代者。

### 与 SpringFox 的对比

| 维度 | SpringFox | SpringDoc |
|------|-----------|-----------|
| 维护状态 | 2020 年后基本停止 | 活跃维护 |
| Spring Boot 兼容 | 不支持 2.6+ 及 3.x | 支持 2.6+ 及 3.x（含 JDK 17+） |
| 注解体系 | 专属注解（`@ApiModel` 等） | JSR-303 规范注解（`@Schema`、`@Parameter`） |
| 配置复杂度 | 高 | 多数场景零配置 |
| OpenAPI 规范 | Swagger 2.0 / OpenAPI 3.0 | 原生 OpenAPI 3 |

### 最小化配置（四步）

1. 引入 `org.springdoc:springdoc-openapi-starter-webmvc-ui:2.5.0`
2. 配置 `packages-to-scan`、`swagger-ui.path`、`api-docs.path`
3. `@OpenAPIDefinition(info = @Info(...))` 设标题版本描述
4. Controller 加 `@Tag`、方法加 `@Operation`、参数加 `@Parameter`

### 分组配置

两种方式：编程式（`GroupedOpenApi.builder()`）与声明式（`springdoc.group-configs`）。

**重要**：一旦配了分组，配置文件的 `packages-to-scan` 就失效；未被分组覆盖的接口不显示，需要加默认分组。

### 环境适配

- 重写 `WebMvcConfigurer.addResourceHandlers` → 需手动补 `/swagger-ui/**` 映射
- 引入 SpringSecurity → 需放行 `/swagger-ui/**`、`/*/api-docs/**`、`/swagger-resources/**`、`/webjars/**` 等路径

## 关联连接
- [[摘要-springdoc-api文档]] — 来源
- [[OpenAPI规范]] — 所实现的规范
- [[Swagger]] — 规范前身与 UI 展示
- SpringFox — 被替代的前代方案
- [[SpringBoot]] — 宿主框架
- [[小哈]] — 文章作者
