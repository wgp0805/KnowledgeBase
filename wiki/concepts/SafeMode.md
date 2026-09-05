---
title: "SafeMode"
type: concept
tags: [JSON, 安全, FastJson]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 定义
SafeMode 是 FastJson/FastJson2 提供的安全对抗模式，开启后进一步限制反序列化行为，降低 AutoType 相关风险。

## 关键信息
- FastJson2：AutoType 默认关闭 + SafeMode 双层安全防护
- FastJson 1.x：可通过 `ParserConfig.getGlobalInstance().setSafeMode(true)` 开启
- 命令行参数：`-Dfastjson2.parser.safeMode=true`
- 安全实践：确需使用 FastJson2 时，务必开启 SafeMode + 禁止全局 AutoType

## 关联连接
- [[FastJson]] — SafeMode 所属库
- [[FastJson2]] — SafeMode 默认集成
- [[AutoType]] — SafeMode 要对抗的风险
- [[摘要-spring-boot-json-security]] — 来源
