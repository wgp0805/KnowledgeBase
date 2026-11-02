---
title: "摘要-springdoc-api文档"
type: source
tags: [来源, SpringDoc, OpenAPI, Swagger, SpringBoot]
sources: [raw/01-articles/2026-11-01 - 告别Swagger UI！一款更适合 SpringBoot 的API文档新选择.md]
last_updated: 2026-11-02
---

## 核心摘要

「小哈学Java」介绍 Spring Boot API 文档新选择 **SpringDoc**。

**SpringDoc 是什么**：专为 Spring Boot 设计的库，自动生成符合 OpenAPI 3 规范的 API 文档。扫描项目中的控制器、方法注解及配置，动态生成 JSON/YAML/HTML 格式文档，并提供交互式界面（如 Swagger UI）。

**与 Swagger 的关系**：Swagger 是 OpenAPI 规范的前身，贡献了 API 设计理念并推动标准化；Swagger UI 用于展示交互式文档。SpringDoc 不是 Swagger 的替代品，而是基于 OpenAPI 3 规范的实现工具，天然集成 Swagger UI 作为展示界面。

**为什么要替代 SpringFox**：SpringFox 在 2020 年后基本停止维护，无法适配 Spring Boot 2.6+ 及 3.x（路径匹配失效、注解不兼容），配置复杂。SpringDoc 完美支持 Spring Boot 2.6+ 及 3.x（含 JDK 17+），原生支持 OpenAPI 3，多数场景零配置（引入一个依赖即可开箱即用），直接使用 JSR-303 规范注解（`@Schema`、`@Parameter`）替代 SpringFox 专属注解（`@ApiModel`）。

**最小化配置步骤**：

1. 引入依赖 `org.springdoc:springdoc-openapi-starter-webmvc-ui:2.5.0`
2. 配置文件设置 `springdoc.packages-to-scan`、`swagger-ui.path`（默认 `/swagger-ui/index.html`）、`api-docs.path`（默认 `/v3/api-docs`，注意 `swagger-ui.url` 要与 `api-docs.path` 保持一致）
3. 添加配置类用 `@OpenAPIDefinition(info = @Info(...))` 设置标题、版本、描述
4. 在 Controller 上加 `@Tag`、方法上加 `@Operation`、参数上加 `@Parameter`

**分组配置两种方式**：

- 编程式：定义 `GroupedOpenApi` Bean，用 `.group("名称")` + `.pathsToMatch("/api/product/**")` 或 `.packagesToScan("com.xxx.controller")`
- 声明式：配置文件里 `springdoc.group-configs` 列表

注意：一旦配了分组，配置文件的 `packages-to-scan` 失效（分组扫描优先级更高）；多分组路径重合时接口会在多个分组出现；未被任何分组覆盖的接口不显示，需要加一个默认分组（`.pathsToMatch("/**")`）。

**环境适配**：

- 重写了 `WebMvcConfigurer.addResourceHandlers` 后，需手动补上 `/swagger-ui/**` 的资源映射，否则静态资源指向全失效
- 引入 SpringSecurity 后，要在过滤器链里放行 `/swagger-ui/**`、`/*/api-docs/**`、`/swagger-resources/**`、`/webjars/**` 等路径

## 关联连接
- [[SpringDoc]] — 被介绍的工具
- [[OpenAPI]] / [[Swagger]] — 规范与前身
- [[SpringFox]] — 被替代的前代方案
- [[SpringBoot]] — 承载框架
- [[小哈]] — 文章作者
