---
title: "Pi"
type: entity
tags: [AI编程, Agent, 开源工具, 终端]
sources:
  - raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md
  - raw/01-articles/GitHub狂揽8.6万Star！为什么越来越多人用 Pi ？.md
  - raw/01-articles/2026-08-15-为什么越来越多人用 Pi ？ - 苏三说技术.md
last_updated: 2026-08-17
---

## 定义
Pi 是由 [[MarioZechner]]（[[libGDX]] 创始人）创建的开源终端 AI 编程 Agent，MIT 协议，GitHub 8.6 万 Star。核心理念是"大道至简"——系统提示词仅 200 Token（[[ClaudeCode]] 为 14000 Token），默认仅 4 个工具（read/write/edit/bash），通过"给你原语而不是预烹饪功能"的减法设计实现极简与高性能。被评为"目前唯一能真正平替 Claude Code 的 Agent 架构"。

## 关键信息

### 核心架构
- **双层循环 Agent Loop**：内层循环（Steering 实时引导）+ 外层循环（Follow-up 排队执行）
- **系统提示词**：仅 200 Token，工具定义不到 1000 Token，打招呼仅占 1100 上传 Token（0.4% 上下文）
- **核心工具**：4 个（Read/Write/Edit/Bash），bash 是万能工具（find/grep/ls）
- **无内置功能**：无 MCP/SubAgent/Plan Mode/Todo/btw，全部通过插件扩展

### 性能与成本
- [[Composio]] 基准测试：完成编程任务速度比其他 Coding Agent 快 1.5-2 倍
- [[Databricks]] 百万行代码测试：大部分场景优于 Claude Code 和 Codex，代码质量最高点是 Pi + Claude Opus 4.8
- 接入 [[DeepSeek]] 后 99.93% 缓存命中率，平均成本约 0.028 美元/任务，是 Claude Code 的七分之一

### 模型支持
- 支持 15+ 供应商：Claude、Kimi、DeepSeek、OpenAI、Google、xAI、Groq 等
- 支持 OAuth 订阅：Claude Pro/Max、ChatGPT Plus/Pro、GitHub Copilot、Google Gemini CLI
- 不锁模型，2026-06 Claude Code 大规模封号事件后成为重要优势

### 兼容性
- 自动读取 `~/.agents/skills` 和 `AGENTS.md`，[[ClaudeCode]] 积累无缝迁移
- 兼容 [[AgentSkills]] 标准协议
- 通过 `pi-mcp-adapter` 插件支持 MCP

### 插件生态
- `pi-web-access`（联网搜索）、`pi-subagents`（并行子代理）、`pi-mcp-adapter`（MCP 支持）
- `pi-btw`（旁路对话）、`pi-plan-mode`（计划模式）、`pi-goal`（目标模式）
- `pi-dynamic-workflows`（动态工作流，10+ 子代理协同）、`pi-wechat`（微信通信）
- 插件可全局装或项目级装（`-l`），`/reload` 重新加载

### 安装
- Windows：`powershell -c "irm https://pi.dev/install.ps1 | iex"`
- Mac：`curl -fsSL https://pi.dev/install.sh | sh`
- npm：`npm install -g @earendil-works/pi-coding-agent`（推荐 `--ignore-scripts`）

### 设计哲学
- "对 Agent 来说，你刻意不做什么，比你做什么更重要"
- "给你原语（Primitives），而不是预烹饪好的功能（Features）"
- "这一代大模型已经擅长读写改文件和调用 bash，不需要 10000 Token 教它们工作"
- "Claude Code 是给你一个 AI 助手，Pi 是给你造 AI 助手的工厂"
- 毛坯房比喻：其他工具是精装房不能改格局，Pi 是毛坯房水电齐全自己装修

### 缺点
- 默认功能太少，需要动手能力
- 终端门槛，虽有 Web UI（第四种黑猩猩开发，4200+ Star）
- 生态年轻

## 关联连接
- [[MarioZechner]] — 创始人
- [[libGDX]] — 创始人背景项目
- [[ClaudeCode]] — 主要对比对象
- [[Codex]] — 对比对象
- [[Composio]] — 基准测试方
- [[Databricks]] — 代码质量测试方
- [[AgentSkills]] — 扩展机制
- [[AGENTS-md]] — 跨 Session 记忆机制
- [[DeepSeek]] — 推荐模型供应商
- [[摘要-pi-agent-保姆级全攻略]] — 完整教程
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 追风视角解析
- [[摘要-为什么越来越多人用Pi-苏三]] — 苏三视角解析
