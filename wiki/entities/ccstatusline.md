---
title: "ccstatusline"
type: entity
tags: [工具, Claude Code, 状态栏, 终端]
sources: [raw/01-articles/给 Claude Code 装上这个超酷的状态栏，逼格瞬间拉满！.md]
last_updated: 2026-07-17
---

## 定义

ccstatusline 是一款开源的 Claude Code 状态栏工具，可以在终端底部常驻显示模型、Git 分支、上下文使用量、Token 用量等关键信息，安装配置简单，支持交互式 TUI 配置界面。

## 关键信息

- **GitHub 仓库**：https://github.com/sirmalloc/ccstatusline
- **安装方式**：
  - npx：`npx -y ccstatusline@latest`
  - bunx：`bunx -y ccstatusline@latest`
  - 全局安装：选择 `Pinned global install` 后直接运行 `ccstatusline`
- **配置方式**：
  - 交互式 TUI 界面配置（推荐）
  - 直接编辑 `~/.config/ccstatusline/settings.json`
- **功能特性**：
  - 实时指标：模型名称、Git 分支、Token 使用量、各模型每周用量
  - 高度可定制：自由选择显示内容，每个组件可单独自定义颜色
  - Powerline 支持：精美 Powerline 风格状态栏
  - 多行状态栏：最多 3 行独立状态栏
  - 智能宽度适配：自动适配终端宽度
- **推荐显示项**：模型、思考程度、Git 分支、上下文、用量
- **工作原理**：向 Claude Code 的 `settings.json` 写入 `statusLine` 配置，通过命令渲染状态栏

## 关联连接

- [[摘要-claude-code-statusline]] — 来源：Claude Code 状态栏工具介绍
- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[claude-hud]] — 另一款类似的状态栏工具
- [[Node.js]] — JavaScript 运行环境
