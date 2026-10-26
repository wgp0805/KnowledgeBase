---
title: "AIAgentsTerminal"
type: entity
tags: [VSCode, Agent, 终端, 开发工具]
sources: ["raw/09-archive/2026-09-04-AI Agents Terminal：在 VS Code 状态栏一键启动你所有的 AI 编程 Agent - Cn#工作室.md", "raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 定义
AI Agents Terminal 是一个 VS Code 扩展，把本机已安装的 AI CLI 编程助手统一收进状态栏按钮，解决多 agent 之间反复切换的摩擦问题。

## 关键信息
- 核心特性：只显示已安装 agent、YOLO模式、Resume模式、17个内置agent
- 内置 agent：Claude Code、Codex、Cline、CodeBuddy、Continue、Copilot、Cursor、Gemini、Goose、Hermes、Kilo、Kimi、OpenClaw、OpenCode、Pi、Qoder、Trae
- 每个 agent 各自配置 flag，不全局一刀切
- 扩展地址：github.com/cnsharp/ai-agents-terminal-vsc

## 增量补充（2026-10-26）
- 同作者 2026-10 推出后续产品 [[AgentYOLO]]：把同一套体验（只列已装 Agent、真实 PTY 终端、Y/R 开关、agents.json 数据驱动、多标签并行）从 VS Code 状态栏扩展为 IntelliJ / Visual Studio / VS Code 三端面板；VSC 端形态从状态栏按钮变为 Activity Bar 的 Agents 面板（node-pty + xterm.js），并新增输出链接化能力——前作核心是「启动」，后作补上「输出可点」。

## 关联连接
- [[摘要-ai-agents-terminal-vscode]] — 来源
- [[ClaudeCode]] — 支持的 agent
- [[Codex]] — 支持的 agent
- [[Cursor]] — 支持的 agent
- [[VSCode扩展]] — 插件生态
- [[YOLO模式]] — 自动放行
- [[Resume模式]] — 续会话
- [[AgentYOLO]] — 同作者后续三端版本
- [[CnSharpStudio]] — 作者
- [[摘要-agent-yolo-三端ide面板]] — 来源
