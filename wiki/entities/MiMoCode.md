---
title: "MiMoCode"
type: entity
tags: [AI, 编程助手, 开源, 小米]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 定义
小米基于 OpenCode 构建的 AI 编程 Agent 工具，采用 MIT 开源协议发布。保留了 OpenCode 的核心能力（多 Provider、TUI、LSP、MCP、插件），并在此基础上构建了持久化记忆、智能上下文管理、子智能体编排、目标驱动的自主循环、Compose 工作流和自进化能力。

## 关键信息

### 安装与使用
- 安装命令：`curl -fsSL https://mimo.xiaomi.com/install | bash`
- 启动命令：`mimo`
- 支持 MiMo Auto（限时免费）、小米 MiMo 平台 OAuth 登录
- 支持从 Claude Code 导入认证配置
- 支持自定义 Provider（任意 OpenAI 兼容 API）
- 集成 `ai-sdk.dev` SDK 和 `models.dev` 模型库

### Harness 架构三主题
MiMo Code 的 Harness 围绕计算、记忆、进化三个主题设计：

1. **计算**：[[max-mode]]（并行候选评估）、[[goals]]（目标验证器）、[[dynamic-workflow]]（代码化流程编排）
2. **记忆**：[[checkpoint-rebuild]]（上下文窗口管理）和四层记忆体系
3. **进化**：通过 dream/distill 机制实现自我进化

### 运行时新指令排队
支持在 Agent 运行中新指令排队，无需中断当前任务。

## 关联连接
- [[Xiaomi]] — 开发公司
- [[OpenCode]] — 底层框架
- [[AgentHarness]] — Harness 架构总称
- [[max-mode]] — 并行候选评估机制
- [[goals]] — 目标验证机制
- [[dynamic-workflow]] — 工作流编排
- [[checkpoint-rebuild]] — 上下文管理
- [[ClaudeCode]] — 同类产品
- [[摘要-mimo-code发布]] — 来源
