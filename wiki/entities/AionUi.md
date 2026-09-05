---
title: "AionUi"
type: entity
tags: [实体, AI Agent, 开源项目, 桌面应用, 统一UI]
sources: [raw/01-articles/斩获14k+Star，把OpenClaw+Claude Code等多个Agent装进一个UI。.md]
last_updated: 2026-08-13
---

## 定义
AionUi 是一个免费、开源、本地的多 AI Agent 桌面应用，由 iOfficeAI 团队维护。其核心定位是把 OpenClaw、Claude Code、Codex、Qwen Code、Goose CLI、Gemini CLI 等主流命令行 AI 工具整合进同一图形界面统一管理，被认为是 Anthropic 官方 Claude Cowork（仅支持 macOS + Claude 模型）的开源平替，且横跨 macOS / Windows / Linux 三大平台。

## 关键信息
- **GitHub**：[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)，一个月内斩获 14.2k+ Star，多次登上 GitHub Trending
- **安装方式**：
  - GitHub Releases 直接下载（macOS 10.15+ / Windows 10+ / Linux Ubuntu 18.04+，内存推荐 4GB+）
  - macOS Homebrew：`brew install aionui`
- **核心能力**：
  1. **多 Agent 统一 UI**：整合 [[OpenClaw]]、[[ClaudeCode]]、[[Codex]]、Qwen Code、Goose CLI、Gemini CLI 等命令行 AI 工具，免去 CLI 参数记忆与终端切换
  2. **多会话并行**：每个会话独立上下文记忆互不干扰
  3. **WebUI 远程访问**：服务器部署后通过浏览器从手机/平板/电脑访问，支持局域网/跨网络/服务器部署，二维码或账号密码登录；并集成 Telegram、飞书、Slack
  4. **9+ 格式实时预览**：PDF、Word、Excel、PPT、代码、Markdown、图片、HTML、Diff，编辑器与预览智能同步
  5. **定时任务自动化**：自然语言设定执行时间，覆盖数据汇总/报告生成/文件整理/定时提醒
  6. **10+ 内置专业助手**：Cowork、PPTX Generator、PDF to PPT、UI/UX Pro Max（57 风格 95 配色）、Planning with Files、moltbook、Beautiful Mermaid 等
  7. **Skills 扩展**：通过 [[Skill]] 机制扩展助手能力边界
- **模型支持**：Gemini（Google 登录或 API Key）、OpenAI、Claude、[[Qwen]]、[[DeepSeek]]、[[Ollama]]、LM Studio、OpenRouter 路由等
- **定位**：AI 办公 + 编程自动化一站式平台，免费开源
- **同类对比**：与 [[CherryStudio]] 同为本地多模型桌面客户端，但 AionUi 更聚焦「多 CLI Agent 统一编排 + WebUI 远程访问 + 助手生态」

## 关联连接
- [[摘要-多agent统一UI工具]] — 来源摘要
- [[OpenClaw]] — 被整合的 CLI Agent 之一，WebUI 远程访问理念同源
- [[ClaudeCode]] — 被整合的 CLI Agent 之一
- [[Codex]] — 被整合的 CLI Agent 之一
- [[HermesAgent]] — 同为开源 AI Agent，可作横向对比
- [[Agent]] — 多 Agent 统一编排的底层概念
- [[Skill]] — AionUi 助手扩展机制
- [[VibeCoding]] — 多会话并行场景的典型用法
- [[automations]] — 定时任务功能的对应概念
- [[gateway-messaging]] — Telegram/飞书/Slack 集成的多端消息层理念
- [[CherryStudio]] — 同类本地多模型桌面客户端
- [[GitHub]] — 项目托管平台
- [[DeepSeek]] — 支持的模型之一
- [[Qwen]] — 支持的模型之一
- [[Ollama]] — 支持的本地模型运行时
- [[沉默王二]] — 实测作者
