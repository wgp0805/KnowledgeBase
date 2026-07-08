---
title: "摘要-gsd-core-ai工作流"
type: source
tags: [来源, 原始文件, AI编程, 规范驱动, 上下文工程]
sources: [raw/01-articles/2.3k star 的新项目，用来指挥 Claude Code 和 Codex 干活！.md]
last_updated: 2026-07-08
---

## 核心摘要

[[GSDCore]] 是一个开源 AI 编码工作流项目（2.3k Star），核心定位是为 AI 编程工具提供元提示、[[ContextEngineering|上下文工程]]和 [[规范驱动开发]] 能力。它不是新编辑器，也不替代 [[ClaudeCode]] 或 [[Cursor]]，而是给这些 AI 编码助手加上一层"项目管理大脑"，引导 AI 先理解项目、再拆解阶段、按计划执行、最后检查结果。

典型工作流（以新增"文章草稿自动保存"为例）：`/gsd-map-codebase` 分析现有代码库 → `/gsd-new-project` 创建项目上下文 → `/gsd-discuss-phase 1` 进入需求讨论 → `/gsd-plan-phase 1` 生成执行计划 → `/gsd-execute-phase 1` 执行 → `/gsd-verify-work 1` 验证本阶段工作。让 AI 写代码从"想到哪改到哪"变成有上下文、有计划、有检查地推进。

支持 macOS/Windows/Linux，通过 `npx @opengsd/gsd-core@latest` 安装（`--minimal` 为最小模式），安装时引导选择接入 Claude Code、Codex、Gemini CLI、Cursor、Windsurf 等环境。项目地址：<https://github.com/open-gsd/gsd-core>（注意是 `open-gsd/gsd-core`，勿与其他同名旧仓库混淆）。

## 关联连接

- [[GSDCore]] — 核心实体
- [[规范驱动开发]] — 上层方法论
- [[ContextEngineering]] — 上下文工程能力
- [[ClaudeCode]] — 支持平台
- [[Codex]] — 支持平台
- [[Cursor]] — 支持平台
- [[Gemini]] — Gemini CLI 支持
- [[GitHub]] — 代码托管
- [[AICoding]] — AI 辅助编程范式
