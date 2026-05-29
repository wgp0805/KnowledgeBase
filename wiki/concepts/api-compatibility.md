---
title: "api-compatibility"
type: concept
tags: [API, 版本管理, 兼容性]
sources: []
last_updated: 2026-05-29
---

## 定义
API 兼容性是指 API 在版本演进过程中保持向后兼容的能力，确保现有客户端在 API 升级后仍能正常工作，是微服务架构中的重要质量属性。

## 关键信息
- 向后兼容：新版本 API 不破坏现有客户端的行为
- 兼容性变更：新增可选字段、新增端点、新增可选参数
- 破坏性变更：删除字段、修改字段类型、改变语义、修改必填参数
- 版本策略：URL 版本（/v1/）、Header 版本（Accept-Version）
- 契约测试：Pact 等工具验证 API 兼容性

## 关联连接
- [[microservices]] — 微服务架构中的 API 管理
- [[incident-severity-classification]] — 兼容性问题可能导致事故
- [[CI-CD]] — 自动化兼容性检查
