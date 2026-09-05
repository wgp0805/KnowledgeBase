---
title: "JSON-B"
type: entity
tags: [JSON, JakartaEE, Java]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
JSON-B（JSON Binding，参考实现 Yasson）是 Jakarta EE 官方标准 JSON 绑定方案，规则清晰，适合偏规范化的企业级项目。

## 关键信息
- Jakarta 标准方案，规范清晰
- 暂未查到公开的同等级 RCE 或高危反序列化记录
- 缺点：国内资料、组件生态和排错经验较少
- 定位：适合规范化企业项目，普通 Spring Boot 项目推荐仍用 Jackson

## 关联连接
- [[Jackson]] — 竞品
- [[JakartaEE]] — 所属规范体系
- [[摘要-spring-boot-json-security]] — 来源
