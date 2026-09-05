---
title: "摘要-spring-boot-json-security"
type: source
tags: [JSON, Spring Boot, 安全]
sources: [raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md]
last_updated: 2026-07-31
---

## 核心摘要
程序汪从安全性角度对 Spring Boot 项目常用 JSON 库进行排行：Jackson（推荐）> Gson（推荐）> JSON-B（一般）> FastJson2（不推荐）> FastJson 1.x（应淘汰）。核心观点是"不存在零漏洞的 JSON 库"，真正的安全不在于选对库，而在于固定 DTO、禁止全局多态、限制请求大小、及时升级依赖。Spring Boot 4 已将 Jackson 3 作为首选默认库。Jackson 历史漏洞虽多但需主动开启多态类型，正常固定 DTO 使用安全；FastJson2 虽然 AutoType 默认关闭且支持 SafeMode，但类型解析路径仍在持续加固；FastJson 1.x 因多轮 RCE 风险不应再用。

## 关联连接
- [[Jackson]] — 第一名，Spring Boot 默认 JSON 引擎
- [[Gson]] — 第二名，适合小型项目
- [[FastJson]] — 第五名，应淘汰
- [[FastJson2]] — 第四名，不推荐新项目使用
- [[JSON-B]] — 第三名，Jakarta 标准方案
- [[程序汪]] — 来源作者
- [[AutoType]] — 反序列化安全风险根源
- [[SafeMode]] — FastJson 安全模式
- [[多态反序列化]] — Jackson 历史漏洞核心原因
