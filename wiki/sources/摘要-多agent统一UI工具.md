---
title: "摘要-多agent统一UI工具"
type: source
tags: [来源, 原始文件, AionUi, 多Agent桌面应用, 统一UI]
sources: [raw/01-articles/斩获14k+Star，把OpenClaw+Claude Code等多个Agent装进一个UI。.md]
last_updated: 2026-08-13
---

## 核心摘要
[[沉默王二]] 实测介绍了开源项目 [[AionUi]]：一个免费、开源、本地的多 AI [[Agent]] 桌面应用，一个月内即在 [[GitHub]] 斩获 14.2k+ Star，多次登上 GitHub Trending。其核心价值是把 [[OpenClaw]]、[[ClaudeCode]]、[[Codex]]、Qwen Code、Goose CLI、Gemini CLI 等主流命令行 AI 工具整合进同一图形界面统一管理，被作者视为 Anthropic 官方 Claude Cowork（仅支持 macOS + Claude 模型）的开源平替，且横跨 macOS / Windows / Linux 三大平台。

文章覆盖 AionUi 的七大能力：
1. **一键安装开箱即用**：Releases 下载或 `brew install aionui`，内存推荐 4GB+，首启内置 Gemini CLI；支持 Gemini / OpenAI / Claude / [[Qwen]] / [[DeepSeek]] / [[Ollama]] / LM Studio 等主流模型与 OpenRouter 路由。
2. **多 Agent 协同与多会话并行**：免去 CLI 参数记忆与终端切换，每个会话独立上下文互不干扰，适合 [[VibeCoding]] + 写教程并行多任务。
3. **WebUI 远程访问**：服务器部署后通过浏览器从手机/平板/电脑访问，支持局域网、跨网络、服务器部署，二维码或账号密码登录；并集成 Telegram、飞书、Slack 等聊天平台，构建 [[gateway-messaging]] 式的多端 AI 陪伴，理念与 [[OpenClaw]] 一致。
4. **9+ 格式实时预览**：PDF、Word、Excel、PPT、代码、Markdown、图片、HTML、Diff 即时预览，编辑器与预览智能同步，调试 AI 生成代码效率翻倍。
5. **定时任务自动化**：自然语言设定执行时间（每天/每周/每月），覆盖数据汇总、报告生成、文件整理、定时提醒，对应 [[automations]] 概念的桌面端落地。
6. **10+ 内置专业助手**：Cowork（自主任务执行）、PPTX Generator、PDF to PPT、UI/UX Pro Max（57 风格 95 配色）、Planning with Files、moltbook（零部署 AI Agent 社交）、Beautiful [[Mermaid]]（流程图/序列图）等。
7. **Skills 扩展**：助手能力不足时可通过 [[Skill]] 机制扩展边界，与 Claude Code/OpenClaw 的 Skill 生态理念同源。

作者结论：AionUi 已坐实「AI 办公 + 编程自动化最佳实践」，覆盖打工人几乎所有场景，且完全免费开源。它与 [[CherryStudio]]（同为本地多模型桌面客户端）属同类，但更聚焦「多 CLI Agent 统一编排 + 远程访问 + 助手生态」。

## 关联连接
- [[AionUi]] — 本文引入的核心产品实体
- [[OpenClaw]] — 被整合的 CLI Agent 之一，WebUI 远程访问理念同源
- [[ClaudeCode]] — 被整合的 CLI Agent 之一
- [[Codex]] — 被整合的 CLI Agent 之一
- [[HermesAgent]] — 同为开源 AI Agent，可作对比
- [[Agent]] — 多 Agent 统一编排的底层概念
- [[Skill]] — AionUi 助手扩展机制
- [[VibeCoding]] — 多会话并行场景的典型用法
- [[automations]] — 定时任务功能的对应概念
- [[CherryStudio]] — 同类本地多模型桌面客户端
- [[沉默王二]] — 文章作者
- [[GitHub]] — 项目托管平台
