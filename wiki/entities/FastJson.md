---
title: "FastJson"
type: entity
tags: [JSON, Java, 阿里巴巴]
sources: []
last_updated: 2026-05-29
---

## 定义
FastJson 是阿里巴巴开源的高性能 JSON 处理库，以解析速度快著称，但历史上存在多次安全漏洞（反序列化漏洞），新项目推荐使用 Jackson。

## 关键信息
- 核心 API：`JSON.toJSONString()`（序列化）、`JSON.parseObject()`（反序列化）
- 安全隐患：历史上多次反序列化漏洞（CVE），需升级到安全版本
- autoType：反序列化时自动识别类型，存在安全风险
- 与 Jackson 对比：FastJson 性能略优但安全性差，Jackson 更稳定可靠
- 建议：新项目优先使用 Jackson，存量项目升级到 Fastjson2

## 关联连接
- [[Jackson]] — 竞品（推荐替代）
- [[Java]] — 所属语言生态
- [[SpringBoot]] — 默认使用 Jackson
