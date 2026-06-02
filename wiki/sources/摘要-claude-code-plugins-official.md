---
title: "摘要-claude-code-plugins-official"
type: source
tags: [Claude Code, 插件, Anthropic]
sources: [raw/01-articles/直接让你的 Claude Code 效率拉满，Anthropic 官方神级插件开源了！-2026-06-02 09_14_35.md]
last_updated: 2026-06-02
---

## 核心摘要
Anthropic 官方开源了 claude-plugins-official 项目（GitHub 近 3 万 Star），本质上就是 Claude Code 的插件应用商店源码。项目收录一百多款插件，分为三类：LSP 语言服务类（TypeScript/Python/Java/Go/C++ 等语言服务器）、开发工作流类（feature-dev 功能开发、code-review 代码审查、commit-commands 规范提交、security-guidance 安全引导）、外部工具集成类（GitHub、GitLab、Figma、Linear、Playwright、Vercel、Sentry、Terraform、Atlassian、Asana 等）。插件通过 `/plugin install` 命令零配置安装，每个插件遵循统一目录结构（.claude-plugin/plugin.json + 可选 mcp.json/commands/agents/skills）。

## 关联连接
- [[ClaudeCode]] — Claude Code 实体，插件系统的载体
- [[MCP]] — 插件可选集成的模型上下文协议
- [[Skill]] — 插件可封装的技能扩展
- [[GitHub]] — 代码托管平台，项目所在
- [[GitLab]] — 集成插件之一
