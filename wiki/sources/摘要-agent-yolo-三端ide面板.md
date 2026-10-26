---
title: "摘要-agent-yolo-三端ide面板"
type: source
tags: [来源, 原始文件]
sources: ["raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 核心摘要
Cn#工作室（cnsharp）发布 **Agent YOLO**——一个把 AI Agent CLI"摁进 IDE 侧边面板"的扩展器，同时覆盖 IntelliJ（最低 2023.3）、Visual Studio（[17.0, 19.0)，含 VS2022/VS2026）、VS Code 三端。面板只列出本机 PATH 上已装的 Agent（Claude Code、Codex、Cursor、CodeBuddy、Kimi 等），一次点击即在 IDE 内**真实可交互 PTY 终端**拉起，输出中的文件路径、堆栈帧、类型名、成员引用、URL 全部可点击直达代码（如 `OrderService.cs:128` 直接跳行）。三端终端实现各异但体验同一套心智模型：IntelliJ 用 JediTerm+PTY4J 公开 API（可过市场审核）、VS 端手绘 ConPTY（WPF 自绘 VT/ANSI 解析，不用 WebView2，内置 51 个 Agent）、VS Code 用 node-pty+xterm.js（类型/成员链接依赖 LSP）。维护侧用共享 `Meta/` 目录（图标、i18n、链接正则）做到"改一处、三端齐发"；Y（跳过权限）/R（恢复会话）双开关按 Agent 独立定制、默认关闭且永不自动打开。

## 关联连接
- [[AgentYOLO]] — 本文核心产品实体
- [[CnSharpStudio]] — 作者工作室（cnsharp）
- [[AIAgentsTerminal]] — 同作者前作（VS Code 状态栏版）
- [[Agent输出链接化]] — 输出可点击的核心机制
- [[多端共享元数据]] — Meta/ 三端一致性策略
- [[YOLO模式]] — Y 开关（跳过权限）的理论基础
- [[Resume模式]] — R 开关（恢复会话）
- [[ClaudeCode]] — 支持的 Agent（`--dangerously-skip-permissions`）
- [[Codex]] — 支持的 Agent（`--yolo`）
- [[CodeBuddy]] — 支持的 Agent（`-y`）
- [[IntelliJIDEA]] — IntelliJ 端宿主平台
- [[VSCode扩展]] — VSC 端所属插件生态
- [[Marketplace]] — JetBrains / Visual Studio 两大发布渠道
