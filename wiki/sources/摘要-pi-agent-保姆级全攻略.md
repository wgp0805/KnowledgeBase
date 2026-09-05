---
title: "摘要-pi-agent-保姆级全攻略"
type: source
tags: [来源, AI编程, Agent, Pi, 教程]
sources: [raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md]
last_updated: 2026-08-17
---

## 核心摘要
技术爬爬虾出品的 Pi Agent 完整教程（11 章节），覆盖安装、模型配置、基础操作、指令追加、会话管理、对话树、工具与插件、Agent Skills、Web UI、跨 Session 记忆、安全机制、DIY 插件、源码架构。Pi 是 libGDX 创始人 Mario Zechner 创建的极简开源终端 AI 编程 Agent，系统提示词仅 1000 Token，默认只有 4 个工具（Read/Write/Edit/Bash）。在 Pi 中打招呼仅占用 1100 上传 Token（0.4% 上下文），而 Codex 打招呼就消耗 18000 Token（7% 上下文）。根据 Composio 基准测试，Pi 完成编程任务速度比其他 Coding Agent 快 1.5-2 倍；Databricks 百万行代码仓库测试中，Pi 在大部分场景下优于 Claude Code 和 Codex，代码质量最高点是 Pi + Claude Opus 4.8 组合。

## 关键信息
- **安装**：Windows 用 `powershell -c "irm https://pi.dev/install.ps1 | iex"`，Mac 用 `curl -fsSL https://pi.dev/install.sh | sh`，自动装 Node.js 和 Git
- **模型配置**：`/login` 支持 40+ 模型供应商，可用 API key 或 OAuth 订阅（Claude Pro/Max、ChatGPT Plus/Pro、GitHub Copilot、Google Gemini CLI）；`/model` 切换，Shift+Tab 切思考强度，Ctrl+L 开模型选择器
- **指令追加两种模式**：Steering（默认，打方向盘实时引导，注入内层循环上下文）和 Follow-up（Alt+回车排队，等当前轮完成才执行，处于外层循环）；Pi 核心是双层循环 Agent Loop
- **会话管理**：Session 为单元，`/new` 新开，`pi -c` 从最近 Session 继续，`pi -r` 挑选；**对话树**（`/tree`）支持树状分支回退创建不同尝试；`/clone` 完整复制 Session，`/fork` 基于节点复制新 Session，`/compact` 手动压缩上下文
- **工具设计**：4 个基础工具 + Agent Skill，无 MCP/SubAgent/Plan Mode/Todo/btw；bash 工具是万能工具（find/grep/ls）
- **插件扩展**：`pi-web-access`（联网搜索，零配置 Exa MCP）、`pi-subagents`（并行子代理）、`pi-mcp-adapter`（MCP 支持，读 `.mcp.json`）、`pi-btw`（旁路对话）、`pi-plan-mode`（计划模式，生成 PLAN.md）、`pi-goal`（目标模式多轮迭代）、`pi-dynamic-workflows`（动态工作流，10+ 子代理协同）、`pi-wechat`（微信即时通信）；插件可全局装或项目级装（`-l`）
- **Agent Skills**：遵循标准 Skills 协议，放 `项目目录/.agents/skills/`（项目级）或 `~/.agents/skills/`（全局）；Playwright CLI 浏览器自动化、Markdown Converter 等；可从 SkillHub 检索
- **Web UI**：第四种黑猩猩开发，4200+ Star，`npx` 一键启动；支持项目切换、文件浏览器、模型配置、技能/插件管理、TTS 技能（Edge TTS 零成本）
- **跨 Session 记忆**：项目根目录 `AGENTS.md`（项目级）或 `~/.pi/agent/AGENTS.md`（全局）；`APPEND_SYSTEM.md` 追加系统提示词优先级更高；可让 Pi 自动通读项目生成 AGENTS.md
- **安全机制**：仅基础信任提示，无沙箱；推荐用 WSL/Hyper-V/Docker 容器运行，或装 `pi-permission-system` 插件弹窗审批
- **DIY 插件**：Pi 内置插件开发知识可自写插件，放 `项目目录/.pi/extensions/`（项目级）或 `~/.pi/agent/extensions/`（全局）；`/reload` 重新加载；示例：天气 UI 插件、.env 文件保护插件、rm 命令审批插件
- **源码架构**：packages 下 ai（模型调用统一接口）、agent（Agent loop 双层循环）、coding-agent（4 工具+系统提示词+Skills+插件机制）、tui（命令行界面）；均已封装为 SDK

## 关联连接
- [[Pi]] — 核心实体
- [[技术爬爬虾]] — 来源作者
- [[MarioZechner]] — Pi 创始人
- [[libGDX]] — 创始人背景项目
- [[Composio]] — 基准测试方
- [[Databricks]] — 代码质量测试方
- [[ClaudeCode]] — 对比对象
- [[Codex]] — 对比对象
- [[AgentSkills]] — 核心扩展机制
- [[AGENTS-md]] — 跨 Session 记忆机制
- [[摘要-为什么越来越多人用Pi-苏三]] — 同主题苏三视角
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 同主题追风视角
