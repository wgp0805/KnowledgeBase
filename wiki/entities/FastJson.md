---
title: "FastJson"
type: entity
tags: [JSON, Java, 阿里巴巴]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
FastJson 是阿里巴巴开源的高性能 JSON 处理库，以解析速度快著称，但历史上存在多次安全漏洞（反序列化漏洞），新项目推荐使用 Jackson。

## 关键信息
- 核心 API：`JSON.toJSONString()`（序列化）、`JSON.parseObject()`（反序列化）
- 安全隐患：历史上多次反序列化漏洞（CVE），需升级到安全版本
- autoType：反序列化时自动识别类型，存在安全风险
- 与 Jackson 对比：FastJson 性能略优但安全性差，Jackson 更稳定可靠
- 建议：新项目优先使用 Jackson，FastJson 1.x 应尽快退出
- 历史 CVE：2017、2020、2022、2026 多轮反序列化/RCE 风险
- 同系产品：FastJson2 为后继版本，安全性有改进但仍在加固中

## 关联连接
- [[Jackson]] — 竞品（推荐替代）
- [[FastJson2]] — 后继版本
- [[Java]] — 所属语言生态
- [[SpringBoot]] — 默认使用 Jackson
- [[AutoType]] — 反序列化 RCE 核心根源
- [[SafeMode]] — 安全对抗模式
- [[摘要-jsonpath解析复杂json]] — 介绍 JSONPath 语法规则及其在 Java 中使用 F…
- [[摘要-spring-boot-json-security]] — JSON 库安全性排行
