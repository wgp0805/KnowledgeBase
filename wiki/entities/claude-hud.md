---
title: "claude-hud"
type: entity
tags: [工具, Claude Code, 状态栏, 终端]
sources: [raw/01-articles/给 Claude Code 装上这个超酷的状态栏，逼格瞬间拉满！.md]
last_updated: 2026-07-17
---

## 定义

claude-hud 是一款开源的 Claude Code 状态栏工具（HUD = Heads-Up Display），功能与 ccstatusline 类似，可以通过插件方式安装，配置通过自然语言与大模型交互完成。

## 关键信息

- **GitHub 仓库**：https://github.com/jarrodwatts/claude-hud
- **安装方式**：
  1. 添加市场：`/plugin marketplace add jarrodwatts/claude-hud`
  2. 安装插件：`/plugin install claude-hud`
  3. 重新加载：`/reload-plugins`
- **配置方式**：
  - 命令：`/claude-hud:setup`
  - 通过自然语言与大模型交互配置（速度较慢）
- **配置文件**：`~/.claude/plugins/claude-hud/config.json`
- **显示元素**：project、context、usage、addedDirs、promptCache、memory、environment、tools、skills、mcp、agents、todos、sessionTime
- **临时禁用**：`CLAUDE_HUD_DISABLE=1 claude`
- **卸载方式**：`/plugin uninstall claude-hud` 或删除 `settings.json` 中的 `statusLine`

## 关联连接

- [[摘要-claude-code-statusline]] — 来源：Claude Code 状态栏工具介绍
- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[ccstatusline]] — 另一款类似的状态栏工具
