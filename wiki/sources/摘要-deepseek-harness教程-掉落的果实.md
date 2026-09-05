---
title: "摘要-deepseek-harness教程-掉落的果实"
type: source
tags: [来源, AI编程, Agent, DeepSeekHarness, 教程]
sources: [raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md]
last_updated: 2026-08-17
---

## 核心摘要
掉落的果实出品的 DeepSeek Harness（DSH）完整教程，覆盖安装、配置、四种运行模式、插件开发全流程。DSH 是 DeepSeek 官方自研的开源 Agent 框架，遵循 **Model + Harness = Agent** 设计理念，核心特色是"一切皆插件"——工具、技能、MCP 支持、记忆管理全部通过插件实现。**四种运行模式**：(1) **TUI 模式**（终端交互，默认）——`dsh` 启动，类似 Claude Code 的终端体验；(2) **Headless 模式**（无界面自动化）——`dsh --headless -p "任务描述"`，适合 CI/CD 集成和批处理；(3) **Web UI 模式**——`dsh --web`，浏览器访问，支持文件浏览、会话管理、可视化调试；(4) **SDK 模式**——作为库嵌入其他应用，`import { DSH } from '@deepseek/harness'`。**插件开发**：遵循 DSH 插件协议，定义 `name`、`version`、`tools`、`skills`、`hooks`；支持生命周期钩子（`onSessionStart`、`onToolCall`、`onSessionEnd`）；可通过 `dsh plugin create` 脚手架快速创建。**配置**：`dsh.config.json` 配置模型、插件、MCP 服务器、记忆策略。**记忆管理**：支持跨会话记忆持久化，KV Cache 智能复用，可通过插件自定义记忆策略。

## 关键信息
- **设计理念**：Model + Harness = Agent，模型负责推理，Harness 负责工具调用、记忆、上下文、MCP、Skills
- **四种运行模式**：TUI（默认终端）、Headless（自动化）、Web UI（浏览器）、SDK（嵌入式）
- **插件协议**：定义 name/version/tools/skills/hooks，支持生命周期钩子
- **插件脚手架**：`dsh plugin create <name>` 快速创建插件模板
- **配置文件**：`dsh.config.json` 管理模型、插件、MCP、记忆
- **核心特性**：跨会话记忆持久化、KV Cache 智能复用、Sub-agent 支持、MCP 协议原生支持
- **对标产品**：Claude Code、Codex、阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode

## 关联连接
- [[DeepSeekHarness]] — 核心实体
- [[掉落的果实]] — 来源作者
- [[DeepSeek]] — 所属公司
- [[崔添翼]] — DSH 团队负责人
- [[摘要-deepseek-harness必装10个插件]] — DSH 插件推荐
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — DSH 内测信息
- [[ClaudeCode]] — 对标产品
- [[Codex]] — 对标产品
- [[Harness]] — 通用概念
- [[AgentSkills]] — 插件技能机制
