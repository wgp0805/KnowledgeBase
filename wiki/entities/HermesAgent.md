---
title: "HermesAgent"
type: entity
tags: [AI, Agent, 开源, 自学, NousResearch]
sources: [raw/09-archive/OpenClaw vs Hermes：万字深入讲解两大通用 Agent.md]
last_updated: 2026-06-08
---

# Hermes Agent

Hermes Agent 是由 [[NousResearch]] 开发的开源通用 AI Agent 系统，定位为 **self-improving AI agent**（自我进化的 AI 智能体）。它是唯一内置闭环学习循环（closed learning loop）的 Agent 框架——能从每次任务中学习，自动创建技能文档，在使用中改进技能，并在会话间持久化记忆。

## 核心定位

> Hermes 的核心资产是**学习型执行循环**。它强调 self-improving agent、closed learning loop、自动创建和修补 skills、FTS5 会话搜索、Honcho 用户建模，以及六种执行后端。——《OpenClaw vs Hermes 对比》

与 [[OpenClaw]] 的对比：
- OpenClaw 管**入口和秩序**（多渠道 Gateway、控制面）
- Hermes 管**执行和经验**（学习循环、技能沉淀、经验复用）

## 核心功能

- **闭环学习循环** — Agent 管理的记忆 + 定期提示 + 自主技能创建
- **自动技能创建** — 复杂任务完成后自动沉淀为可复用技能（procedural memory）
- **FTS5 全文检索** — SQLite + FTS5 存储会话，支持跨会话搜索
- **Honcho 用户建模** — 跨会话构建用户画像，深化个性化
- **200+ 模型支持** — OpenRouter、Anthropic、OpenAI、智谱、Kimi、MiniMax 等
- **70+ 内置工具** — 网页搜索、浏览器、图像生成、TTS、文件操作等
- **6 种执行后端** — Local、Docker、SSH、Daytona、Singularity、Modal
- **消息网关** — CLI + Telegram / Discord / Slack / WhatsApp / Signal / Email
- **MCP 集成** — 连接任意 MCP 服务器扩展能力
- **Cron 调度** — 定时自动任务，结果投递到指定平台
- **语音模式** — CLI / Telegram / Discord 实时语音交互

## 技术栈

- **语言**: Python 3.11
- **后端**: uv 包管理，支持 venv 虚拟环境
- **搜索**: SQLite + FTS5 全文检索
- **安全**: Tirith 安全模块（命令审批 + 容器隔离 + 凭据过滤 + 注入扫描）
- **协议**: 支持 OpenAI API 兼容格式，Chrome DevTools Protocol 调试

## 架构

Hermes 的系统分为五大模块：

1. **Agent Loop** (`run_agent.py`) — 完整的 tool calling conversation loop
2. **工具系统** (`model_tools.py`) — 工具发现和分发
3. **技能管理器** (`skill_manager_tool.py`) — 创建/更新/删除 skills，即 Agent 的 procedural memory
4. **状态管理** (`hermes_state.py`) — SQLite + FTS5 会话存储和全文检索
5. **安全模块** (Tirith) — 纵深防御体系

## 优势

- 安装极简：一行命令 60 秒完成
- 成本低廉：$5/月 VPS 即可流畅运行
- 经验积累：Agent 越用越聪明，重复任务速度提升约 40%
- 模型自由：200+ 模型一键切换，不改代码
- 安全可靠：纵深防御体系，零公开 CVE（截至 2026）

## 局限

- Skill 自动沉淀需要复看和修剪，否则可能累积"惯性错误"
- 消息网关的渠道覆盖（6 个）不及 OpenClaw 的 25+
- 原生 Windows 支持为早期测试版，推荐 WSL2

## 关联连接

- [[NousResearch]] — Hermes 背后的团队
- [[OpenClaw]] — 通用 Agent 对标项目
- [[MCP]] — 模型上下文协议集成
- [[ClaudeCode]] — 终端 AI Agent（互补工具）
- [[Ollama]] — 本地模型运行方案
- [[Agent]] — AI Agent 核心概念
- [[hermes-agent-tutorial]] — 完整安装使用教程

- [[摘要-HermesAgent小白入门指南]] — 核心摘要
