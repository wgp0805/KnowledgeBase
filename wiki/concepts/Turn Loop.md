---
title: "Turn Loop"
type: concept
tags: [概念, Agent, 循环, 架构]
sources: [raw/01-articles/2026-09-19 - MiniMax 版 Claude Code 开源，夯。.md]
last_updated: 2026-09-20
---

## 定义
Turn Loop 是 Agent 的核心执行循环，每轮（Turn）状态隔离，通过钩子机制（Hook）在循环各阶段注入自定义逻辑。是 MiniMaxCode 等基于 Pi 框架的 Agent 的核心循环。

## 关键信息
- **核心思想**：每轮状态隔离 + 钩子机制
- **状态隔离**：每轮 Turn 有独立状态，避免上下文污染
- **钩子机制**：在循环各阶段（SessionStart/UserPromptSubmit/PreToolUse/PostToolUse 等）注入自定义逻辑
- **应用**：MiniMaxCode、Pi 框架

## 关联连接
- [[摘要-minimax-code-cli开源]] — 来源
- [[MiniMaxCode]] — 应用
- [[Pi]] — 底层框架
- [[Hook机制]] — 钩子机制
- [[Agent]] — 核心概念