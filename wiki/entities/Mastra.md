---
title: "Mastra"
type: entity
tags: [实体, 框架, Agent, TypeScript]
sources: [raw/09-archive/开源项目｜Star16.3k一站式AI短剧生成平台.md]
last_updated: 2026-10-20
---

## 定义
Mastra 是 TypeScript AI Agent 框架，被火宝短剧（huobao-drama）用作后端 Agent 编排层，在该项目中承载 script_rewriter、extractor、storyboard_breaker、prompt_generator 四个分工明确的 Agent。

## 关键信息
- 在火宝短剧中的角色：backend/ 技术栈核心（Hono + Drizzle + Mastra + SQLite），`backend/workspace/skills/` 目录存放 Agent 技能
- 四个 Mastra Agent 按"剧本→资产→分镜→提示词"流水线分工，各管一段
- 属于"轻量后端框架 + 专职 Agent 编排"的组合选型，与 Spring AI、LangChain4j 等形成生态对照

## 关联连接
- [[HuobaoDrama]] — 使用该框架的开源项目
- [[摘要-huobao-drama-短剧平台]] — 来源
- [[Agent]] — 核心概念
