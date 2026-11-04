---
title: "Swagger"
type: entity
tags: [API文档, OpenAPI, 规范]
sources: [raw/09-archive/2026-11-01 - 告别Swagger UI！一款更适合 SpringBoot 的API文档新选择.md]
last_updated: 2026-11-02
---

## 定义

Swagger 是 API 描述规范的前身，为 OpenAPI 规范的标准化奠定了基础。它定义了统一的 API 描述格式（接口路径、请求方法、数据类型），并提供了 Swagger UI 作为交互式文档展示工具。

## 关键信息

- **角色**：OpenAPI 规范的前身，贡献了 API 设计理念并推动标准化
- **Swagger UI**：将 JSON/YAML 文档解析为交互式网页，提供接口列表、参数说明、请求示例，并支持在线测试 API
- **与 OpenAPI 的关系**：Swagger 2.0 规范演进为 OpenAPI 3.0，Swagger UI 仍是 OpenAPI 文档的常用展示界面
- **在 Spring 生态中的位置**：SpringFox 生成 Swagger 格式 JSON → Swagger UI 渲染展示；SpringDoc 则原生生成 OpenAPI 3 JSON → 同样用 Swagger UI 展示
- **工具链**：Swagger Editor（在线编辑验证）、Swagger Codegen（根据规范生成客户端/服务端代码）

## 关联连接
- [[OpenAPI规范]] — 演进后的规范
- [[SpringDoc]] — Spring 生态中生成 OpenAPI 3 文档的实现工具
- SpringFox — 早期 Spring 生态中的 Swagger 集成方案
- Swagger UI — 交互式文档展示界面（待建）
