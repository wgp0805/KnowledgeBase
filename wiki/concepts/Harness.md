---
title: "Harness"
type: concept
tags: [概念, Agent, 架构, 框架]
sources:
  - raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
  - raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md
last_updated: 2026-08-17
---

## 定义
Harness 是指 AI Agent 中模型之外的一切基础设施层，包括工具调用、记忆管理、上下文控制、桌面集成、MCP 协议、Skills 体系等。核心公式为 **Model + Harness = Agent**：模型负责推理，Harness 负责将模型的推理能力转化为可执行的工程化操作。

## 关键信息
- Harness 是未来五年 AI 工程化的核心主题，各大模型厂商都在争先恐后构建自己的 Harness
- 国内主要 Harness 产品：DeepSeek Harness（DSH）、阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode
- 所有 Agent 本质上都是在做 Harness——让模型更好用、更匹配业务
- **Harness 最关键的能力**：上下文管理、Memory 管理、多 Agent 协作、提示词优化

### 核心组件
1. **工具调用系统**：工具注册表、Schema 校验、HITL 审批
2. **记忆管理系统**：短期记忆（会话级）、长期记忆（跨会话持久化）、项目记忆（规则文件）
3. **上下文控制**：窗口管理、摘要压缩、Token 预算控制
4. **MCP 协议**：外部服务集成
5. **Skills 体系**：可复用的行为模块
6. **多 Agent 协作**：Sub-agent 编排、任务分解

### DSH 四种运行模式（详见 [[摘要-deepseek-harness教程-掉落的果实]]）
1. **TUI 模式**：终端交互（默认），`dsh` 启动
2. **Headless 模式**：无界面自动化，`dsh --headless -p "任务"`，适合 CI/CD
3. **Web UI 模式**：`dsh --web`，浏览器访问，支持可视化调试
4. **SDK 模式**：作为库嵌入，`import { DSH } from '@deepseek/harness'`

### DSH 插件协议
- 定义 `name`、`version`、`tools`、`skills`、`hooks`
- 支持生命周期钩子：`onSessionStart`、`onToolCall`、`onSessionEnd`
- 脚手架：`dsh plugin create <name>`
- 配置文件：`dsh.config.json`

## 关联连接
- [[DeepSeekHarness]] — DeepSeek 原生 Harness 实现
- [[PaiCLI]] — 开源终端 Agent Harness 实现
- [[ReAct_Agent]] — ReAct 推理循环是 Harness 的核心模式
- [[摘要-deepseek-harness内测]] — 来源
- [[摘要-deepseek-harness教程-掉落的果实]] — 来源（DSH 完整教程）
- [[ClaudeCode]] — Claude 的 Harness 实现
- [[Codex]] — Codex 的 Harness 实现
- [[HITL]] — 人机协作审批机制
- [[context-compression]] — 上下文压缩策略
- [[Pi]] — 极简 Harness 实现（系统提示词仅 200 Token）