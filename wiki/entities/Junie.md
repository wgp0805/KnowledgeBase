---
title: "Junie"
type: entity
tags: [AI, JetBrains, coding-agent, ACP, CLI]
sources: []
last_updated: 2026-07-08
---

## 定义
Junie 是 JetBrains 出品的 AI coding agent（AI 编程智能体），定位"LLM 无关"——可自带模型（Anthropic / OpenAI / Google / xAI / OpenRouter / Copilot），也可用 JetBrains 账号或 Junie API Key。能自主完成多步骤任务：修 bug、实现功能、重构代码、审查 PR、写测试。官网 https://junie.jetbrains.com ，GitHub 仓库 JetBrains/junie。

## 关键信息

### 三条运行通道
- **终端 CLI**：独立 `junie` 命令，交互式输入任务
- **IDE 内集成**：[[IntelliJIDEA]] 等 JetBrains IDE 的 AI Assistant agent mode
- **CI/CD pipeline**：通过 GitHub Action 接入，自动响应 issue / PR / CI 失败

### ACP 注册表（IDE「AI agents」选项的本质）
Junie 是 ACP（Agent Client Protocol）host，IDE 中「AI agents」选项即 ACP 注册表，可挂载各路 coding agent（通过 `command + args` 拉起进程、stdio 通信）。注册表收录的国产模型 agent：
- **GLM Agent**（智谱，glm-5.1 / 5-turbo / 5v-turbo / 4.7 / 4.5-air）
- **Kimi CLI**（月之暗面 [[Kimi]]）
- **Qwen Code**（阿里通义 [[Qwen]]）
- **Codebuddy Code**（腾讯云）

### 认证方式
- JetBrains 账号 OAuth
- Junie API Key
- BYOK（自带模型密钥）：Anthropic / OpenAI / Google / xAI / OpenRouter / Copilot

### 安装
```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex (irm 'https://junie.jetbrains.com/install.ps1')"
# 或 npm
npm install -g @jetbrains/junie
```

### 频道切换（一次性试其它构建）
```bash
junie --eap            # 最新 EAP，仅本次
junie --nightly        # 最新 nightly
junie --experimental
junie --release
junie --channel=eap --use-version=122.1   # 钉版本
```

### GitHub 集成
agent 内执行 `/install-github-action`，可让 Junie 自动响应 issue、PR 和 CI 失败。

## 关联连接
- [[IntelliJIDEA]] — IDE 集成宿主
- [[Codex]] — 对比（OpenAI 桌面端 agent）
- [[ClaudeCode]] — 对比（Anthropic 终端 agent）
- [[OpenCode]] — 对比（开源终端 agent）
- [[GLM]] — ACP 注册表收录的国产模型
- [[Qwen]] — ACP 注册表收录的国产模型
- [[Kimi]] — ACP 注册表收录的国产模型
- [[junie-国产模型配置指南]] — 在 IDEA 中配置国产模型操作步骤
