---
title: "Hook机制"
type: concept
tags: [概念, Agent, 钩子, 扩展]
sources: [raw/01-articles/2026-09-19 - MiniMax 版 Claude Code 开源，夯。.md]
last_updated: 2026-09-20
---

## 定义
Hook 机制是 Agent 在生命周期事件（SessionStart/UserPromptSubmit/PreToolUse/PostToolUse/PermissionRequest/Stop/PreCompact 等）上挂载自定义逻辑的扩展机制，是 Turn Loop 的核心组成部分。

## 关键信息
- **核心思想**：在 Agent 循环各阶段注入自定义逻辑
- **生命周期事件**：SessionStart/UserPromptSubmit/PreToolUse/PostToolUse/PermissionRequest/Stop/PreCompact 等
- **应用**：通知、自动格式化、拦截危险命令和敏感文件
- **与扩展注册表关系**：Hook 是扩展的一种，扩展系统建在工具系统之上

## 关联连接
- [[摘要-minimax-code-cli开源]] — 来源
- [[Turn Loop]] — 核心循环
- [[扩展注册表]] — 扩展系统
- [[MiniMaxCode]] — 应用
- [[Agent]] — 核心概念