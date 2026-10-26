---
title: "CnSharpStudio"
type: entity
tags: [开发者, 工作室, 开源, IDE插件]
sources: ["raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 定义
"Cn#工作室"（GitHub 用户 cnsharp，Visual Studio Marketplace 发布者 ID CnSharpStudio）是专注"把 AI Agent CLI 摁进 IDE"工具线的个人开发者/工作室，已发布 AI Agents Terminal 与 Agent YOLO 两代产品。

## 关键信息
- **身份标识**：博客园"Cn#工作室"，GitHub 用户 `cnsharp`；Visual Studio Marketplace 发布者 ID 为 `CnSharpStudio`（VS 端 item：CnSharpStudio.yolo）与 `cnsharp`（VSC 端 item：cnsharp.agentyolo）。
- **产品线**：2026-09 发布 **AI Agents Terminal**——VS Code 状态栏一键启动 AI CLI 助手（17 个内置 agent）；2026-10 升级推出 **Agent YOLO**——同一体验扩展到 IntelliJ / Visual Studio / VS Code 三端（repo：github.com/cnsharp/agent-yolo，IntelliJ 端上架 JetBrains Marketplace，插件 33442-agent-yolo）。
- **工程主张**：把 Agent CLI 摁进 IDE 侧边面板、在真实终端里拉起、输出直接点进去；对用户是"一套心智模型"，换 IDE 不用重学；对维护者靠共享 `Meta/` 做到改一处三端同步。
- **技术取舍**：JetBrains 端坚持只用公开 API（JediTerm + PTY4J）以通过市场审核，内部 API 方案只作实验分支；VS 端宁可手绘 ConPTY 也不用 WebView2。

## 关联连接
- [[摘要-agent-yolo-三端ide面板]] — 来源文章
- [[AgentYOLO]] — 代表作（三端）
- [[AIAgentsTerminal]] — 前作（VS Code 状态栏版）
- [[多端共享元数据]] — 其维护方法论
