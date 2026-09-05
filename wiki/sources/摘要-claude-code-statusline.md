---
title: "摘要-claude-code-statusline"
type: source
tags: [来源, Claude Code, 状态栏, 终端工具]
sources: [raw/01-articles/给 Claude Code 装上这个超酷的状态栏，逼格瞬间拉满！.md]
last_updated: 2026-07-17
---

## 核心摘要

本文介绍两款开源的 Claude Code 状态栏工具：ccstatusline 和 claude-hud。这两款工具可以在终端底部常驻显示模型、Git 分支、上下文使用量、Token 用量等关键信息，避免用户频繁敲命令查看状态。ccstatusline 安装配置最简单，支持交互式 TUI 配置界面；claude-hud 功能类似但配置略复杂。

## 关键信息

- **ccstatusline**：https://github.com/sirmalloc/ccstatusline
  - 安装：`npx -y ccstatusline@latest` 或 `bunx -y ccstatusline@latest`
  - 特性：实时指标、高度可定制、Powerline 支持、多行状态栏、交互式 TUI
  - 配置文件：`~/.config/ccstatusline/settings.json`
  - 推荐显示项：模型、思考程度、Git 分支、上下文、用量

- **claude-hud**：https://github.com/jarrodwatts/claude-hud
  - 安装：`/plugin marketplace add jarrodwatts/claude-hud` → `/plugin install claude-hud`
  - 配置：`/claude-hud:setup`（通过自然语言与大模型交互配置）
  - 配置文件：`~/.claude/plugins/claude-hud/config.json`
  - 临时禁用：`CLAUDE_HUD_DISABLE=1 claude`

## 关联连接

- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[ccstatusline]] — 开源 Claude Code 状态栏工具（待创建）
- [[claude-hud]] — 开源 Claude Code 状态栏工具（待创建）
- [[Node.js]] — JavaScript 运行环境
