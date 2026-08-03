---
title: "FastJson2"
type: entity
tags: [JSON, Java, 阿里巴巴]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
FastJson2 是阿里巴巴推出的新一代 JSON 处理库，FastJson 的后继版本，在安全和性能上做了改进。

## 关键信息
- 性能优秀，AutoType 默认关闭，支持 SafeMode 安全模式
- 暂无正式公开 CVE，但 2026 年出现 AutoType 风险讨论，官方已合并校验加固
- 近期类型解析路径仍在持续加固
- 推荐：存量 FastJson 1.x 项目可以继续用 FastJson2，但新项目没有特殊性能需求不建议主动替换 Jackson
- 使用建议：禁止全局 AutoType，开启 `Dfastjson2.parser.safeMode=true`

## 关联连接
- [[FastJson]] — 前代版本，建议尽快退出
- [[Jackson]] — 竞品，推荐替代方案
- [[AutoType]] — 安全风险根源
- [[SafeMode]] — 安全模式
- [[摘要-spring-boot-json-security]] — 来源
