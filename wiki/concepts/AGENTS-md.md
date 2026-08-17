---
title: "AGENTS-md"
type: concept
tags: [AI编程, Agent, 记忆机制, 协议]
sources:
  - raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md
  - raw/01-articles/GitHub狂揽8.6万Star！为什么越来越多人用 Pi ？.md
last_updated: 2026-08-17
---

## 定义
AGENTS.md 是 AI Agent 的跨 Session 记忆机制标准文件，存放项目级或全局级的指令、规范、上下文信息。Agent 在每次会话启动时自动读取该文件，实现跨会话的持久化记忆。[[Pi]]、[[ClaudeCode]] 等主流 Agent 均支持该机制，使 Claude Code 积累的项目知识可无缝迁移到 Pi。

## 关键信息

### 存放位置
- **项目级**：项目根目录 `AGENTS.md`（仅对该项目生效）
- **全局级**：`~/.pi/agent/AGENTS.md`（对所有项目生效，Pi 专用路径）
- 项目级优先级高于全局级

### 优先级机制
- `AGENTS.md`：基础项目上下文
- `APPEND_SYSTEM.md`：追加系统提示词，优先级更高，可覆盖 AGENTS.md
- Agent 启动时按优先级合并加载

### 自动生成
- 可让 Agent（如 [[Pi]]）自动通读项目代码生成 AGENTS.md
- 内容包括：项目结构、编码规范、常用命令、技术栈、注意事项

### 兼容性
- [[Pi]] 自动读取 `AGENTS.md`，[[ClaudeCode]] 积累无缝迁移
- [[ClaudeCode]] 原生支持 AGENTS.md
- 是 Agent 跨工具迁移项目知识的关键桥梁

### 与 .agents/skills 的关系
- `AGENTS.md`：项目级指令和规范（"做什么"）
- `.agents/skills/`：可复用行为模块（"怎么做"）
- 两者配合构成完整的项目级 Agent 配置

## 关联连接
- [[Pi]] — 支持 AGENTS.md 的 Agent
- [[ClaudeCode]] — 原生支持 AGENTS.md
- [[AgentSkills]] — 配套的技能扩展机制
- [[摘要-pi-agent-保姆级全攻略]] — 来源
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 来源
