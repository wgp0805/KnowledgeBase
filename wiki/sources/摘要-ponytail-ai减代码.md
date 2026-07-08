---
title: "摘要-ponytail-ai减代码"
type: source
tags: [来源, 原始文件, AI编程, 减法思维]
sources: [raw/01-articles/20.9k Star 的开源项目，让你的 AI 少写点废代码.md]
last_updated: 2026-07-08
---

## 核心摘要

[[Ponytail]] 是一个开源 AI Agent 技能项目（20.9k Star），核心理念是"最好的代码，是你根本不用写的代码"。它面向 [[ClaudeCode]]、[[Codex]]、GitHub Copilot CLI、[[Gemini]] CLI、[[OpenCode]] 等 AI 编程工具，安装后给 AI 注入一套"懒但不敷衍"的开发规则：先判断需求是否真的存在，再看标准库、平台原生能力、已有依赖，最后才写最少可用代码。

典型场景：让 AI 做日期选择，普通 Agent 会引入 flatpickr 并写一堆封装，Ponytail 则优先使用浏览器原生 `<input type="date">`。它不是让 AI 更会"炫技"，而是让 AI 学会克制。

提供三档强度切换：`/ponytail lite`（温和）、`/ponytail full`（默认）、`/ponytail ultra`（针对已被过度设计折磨的代码库）。另有 `/ponytail-review` 命令专门检查 [[过度工程化]]，直接指出哪里能删、用什么替代、能减少多少行——例如单一实现的接口可删、日期格式化库可换 `Intl.DateTimeFormat`、手写循环可用标准库一行完成。

项目地址：<https://github.com/DietrichGebert/ponytail>

## 关联连接

- [[Ponytail]] — 核心实体
- [[过度工程化]] — 核心概念
- [[ClaudeCode]] — 支持平台
- [[Codex]] — 支持平台
- [[OpenCode]] — 支持平台
- [[Gemini]] — Gemini CLI 支持
- [[GitHub]] — 代码托管
- [[AICoding]] — AI 辅助编程范式
- [[ai-agent-skill]] — Agent 技能机制
- [[Skill]] — 技能扩展机制
