---
title: "claude-plugins-official"
type: entity
tags: [Anthropic, ClaudeCode, 插件市场]
sources: [raw/01-articles/Claude 又开源了一款新插件，让你的 Claude Code 满血复活！.md, raw/01-articles/直接让你的 Claude Code 效率拉满，Anthropic 官方神级插件开源了！-2026-06-02 09_14_35.md]
last_updated: 2026-06-24
---

## 定义
**claude-plugins-official** 是 [[Anthropic]] 官方维护的 [[ClaudeCode]] 插件应用商店，已内置在 Claude Code 中，通过 `/plugin install <name>@claude-plugins-official` 命令零配置安装；同时在桌面版可通过"Browse plugins"图形化浏览。

## 关键信息

### 已收录的官方插件
- [[claude-code-setup]] — 项目级一键自动化配置工具

### 三大类插件
- **LSP 语言服务**：TypeScript / Python / Java / Go / C++ 等语言支持
- **开发工作流**：feature-dev、code-review、commit-commands 等
- **外部工具集成**：GitHub、GitLab、Figma、Linear、Playwright、Vercel、Sentry 等

### 插件目录结构
- `.claude-plugin/plugin.json`（必填）
- 可选：`mcp.json`、`commands/`、`agents/`、`skills/`

### 安装方式
- CLI：`/plugin install <name>@claude-plugins-official`
- 浏览：`/plugin > Discover` 在列表中选择
- 桌面版：Code 面板 → Customize → Personal plugins → Browse plugins

## 关联连接
- [[摘要-claude-code-setup-plugin]] — 来源
- [[摘要-claude-code-plugins-official]] — 来源（市场总览）
- [[ClaudeCode]] — 宿主产品
- [[Anthropic]] — 维护方
- [[claude-code-setup]] — 旗下插件之一
