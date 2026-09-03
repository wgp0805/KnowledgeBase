---
title: "Jackson"
type: entity
tags: [JSON, Java, 序列化]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md, raw/01-articles/MyBatis-Plus 3.5.15 已全面支持 Spring Boot 4.0 及 Jackson 3.0.md]
last_updated: 2026-09-03
---

## 定义
Jackson 是 Java 生态中最流行的 JSON 处理库，Spring Boot 默认的 JSON 序列化/反序列化引擎，支持 JSON、XML、YAML 等多种格式。

## 关键信息
- 核心模块：jackson-databind（数据绑定）、jackson-core（流式 API）、jackson-annotations（注解）
- ObjectMapper：核心类，用于 JSON 与 Java 对象互转
- 常用注解：@JsonProperty、@JsonIgnore、@JsonFormat、@JsonInclude
- Spring Boot 默认使用：自动配置 ObjectMapper Bean
- 性能：比 FastJson 更安全，比 Gson 更快
- Spring Boot 4 已将 Jackson 3 作为首选默认库
- 2026 年又披露两项类型校验绕过漏洞（需主动开启多态反序列化才会进入危险路径）

### Jackson 3.0（2026）
- 核心包从 `com.fasterxml.jackson` 迁移到 `tools.jackson`
- 对应 MyBatis-Plus 新增 `Jackson3TypeHandler` 类型处理器
- 使用时注意 import 路径：`tools.jackson.databind.ObjectMapper`

## 关联连接
- [[SpringBoot]] — 默认 JSON 处理器
- [[FastJson]] — 竞品（阿里开源）
- [[Java]] — 所属语言生态
- [[摘要-springboot整合RocketMq]] — Spring Boot 整合 RocketMQ 的完整方案，…
- [[摘要-spring-boot-json-security]] — JSON 库安全性排行
- [[Gson]] — 竞品（Google）
- [[JSON-B]] — Jakarta 标准方案
- [[AutoType]] — 反序列化安全风险
- [[多态反序列化]] — 历史漏洞核心原因
