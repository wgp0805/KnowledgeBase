---
title: "Jackson"
type: entity
tags: [JSON, Java, 序列化]
sources: []
last_updated: 2026-05-29
---

## 定义
Jackson 是 Java 生态中最流行的 JSON 处理库，Spring Boot 默认的 JSON 序列化/反序列化引擎，支持 JSON、XML、YAML 等多种格式。

## 关键信息
- 核心模块：jackson-databind（数据绑定）、jackson-core（流式 API）、jackson-annotations（注解）
- ObjectMapper：核心类，用于 JSON 与 Java 对象互转
- 常用注解：@JsonProperty、@JsonIgnore、@JsonFormat、@JsonInclude
- Spring Boot 默认使用：自动配置 ObjectMapper Bean
- 性能：比 FastJson 更安全，比 Gson 更快

## 关联连接
- [[SpringBoot]] — 默认 JSON 处理器
- [[FastJson]] — 竞品（阿里开源）
- [[Java]] — 所属语言生态
