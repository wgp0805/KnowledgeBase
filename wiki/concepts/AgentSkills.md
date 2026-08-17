---
title: "AgentSkills"
type: concept
tags: [AI编程, Agent, 扩展机制, 协议]
sources:
  - raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md
  - raw/01-articles/GitHub狂揽8.6万Star！为什么越来越多人用 Pi ？.md
last_updated: 2026-08-17
---

## 定义
Agent Skills 是 AI Agent 的可复用行为模块标准协议，通过将特定领域知识、工作流程、工具使用方法封装为"技能"，让 Agent 按需加载。遵循标准 Skills 协议的技能可在不同 Agent 框架间复用。[[Pi]]、[[ClaudeCode]]、[[DeepSeekHarness]] 均支持该协议。

## 关键信息

### 存放位置
- **项目级**：`项目目录/.agents/skills/`
- **全局级**：`~/.agents/skills/`
- Agent 自动扫描这两个目录加载技能

### 兼容性
- [[Pi]] 自动读取 `~/.agents/skills`，[[ClaudeCode]] 积累无缝迁移
- [[ClaudeCode]] 原生支持 Skills 协议
- [[DeepSeekHarness]] 通过插件支持 Skills
- 可从 SkillHub 检索社区技能

### 典型 Skills
- Playwright CLI 浏览器自动化
- Markdown Converter 文档转换
- TTS 技能（Edge TTS 零成本）
- 各领域定制工作流

### 与插件的区别
- **Skills**：声明式行为模块，描述"怎么做"，Agent 按需调用
- **插件**：命令式扩展，提供新工具和功能
- 两者互补，Skills 偏知识/流程，插件偏工具/能力

## 关联连接
- [[Pi]] — 支持 Skills 协议的 Agent
- [[ClaudeCode]] — 原生支持 Skills
- [[DeepSeekHarness]] — 通过插件支持 Skills
- [[AGENTS-md]] — 配套的项目上下文机制
- [[摘要-pi-agent-保姆级全攻略]] — 来源
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 来源
