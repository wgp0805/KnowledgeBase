---
title: "OpenAPI规范"
type: concept
tags: [API文档, 规范, RESTful]
sources: [raw/09-archive/2026-11-01 - 告别Swagger UI！一款更适合 SpringBoot 的API文档新选择.md]
last_updated: 2026-11-02
---

## 定义

OpenAPI 是 API 描述的开放规范，定义了统一的格式来描述 RESTful API（接口路径、请求方法、数据类型、参数说明等），使人类和机器都能理解和使用 API 文档。

## 关键信息

- **前身**：Swagger 2.0 规范，演进为 OpenAPI 3.0
- **核心价值**：提供统一标准，确保不同工具（Swagger UI、Swagger Editor、SpringDoc、SpringFox 等）生成的文档互相兼容
- **在 Spring 生态中的位置**：SpringDoc 原生生成 OpenAPI 3 JSON，SpringFox 生成 Swagger 2.0 / OpenAPI 3.0 JSON，两者都用 Swagger UI 渲染
- **规范内容**：接口路径、请求方法、参数、请求/响应体结构、错误码、安全方案等
- **工具链**：Swagger UI（展示）、Swagger Editor（编辑验证）、Swagger Codegen（代码生成）

## 关联连接
- [[Swagger]] — 前身与展示工具
- [[SpringDoc]] — Spring 生态中的实现
- SpringFox — 早期 Spring 生态中的实现
