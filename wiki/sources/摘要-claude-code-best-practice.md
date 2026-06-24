---
title: "摘要-claude-code-best-practice"
type: source
tags: [来源, ClaudeCode, 最佳实践, 工作流, GitHub]
sources: ["raw/01-articles/夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！.md"]
last_updated: 2026-06-24
---

## 核心摘要
GitHub 上斩获 **57k+ Star** 的开源仓库 **claude-code-best-practice** 系统整理了 [[ClaudeCode]] 生态的社区验证经验，分五大板块：(1) **核心能力**：Subagents、Commands、Skills、Workflows、Hooks、MCP Servers、Plugins 的最佳实践；(2) **热门功能**：Ultrareview、Devcontainers、Channels、Ultraplan、No Flicker Mode、Auto Mode、Power-ups、Fast Mode、Computer Use 等高级能力；(3) **工作流**：核心提出 [[Command-Agent-Skill编排]] 架构（Command 触发→Agent 扮演角色→Skill 提供专业能力），及统一的 [[Research-Plan-Execute-Review-Ship]] 五阶段开发范式，外加 [[跨模型工作流]]（通过 Plugin/MCP/Router 三种机制接入 Codex/Gemini/GPT/Kimi/DeepSeek 等模型）；(4) **Skill/Agent 精选集**：包括 Superpowers、Everything Claude Code、Matt Pocock Skills、Spec Kit、gstack、Get Shit Done、[[OpenSpec]] 等主流工作流项目；(5) **83 条实战技巧**：覆盖 Prompting、Planning、Context、Memory、Git/PR、Debugging 等方向（例：CLAUDE.md 单文件应控制在 200 行以下、`.claude/rules/*.md` 在每个会话自动加载）。核心理念：Claude Code 必须**拆阶段执行**（先研究→再计划→再执行→再审查→交付），而不是上来就让它写代码。

## 关联连接
- [[claude-code-best-practice]] — 本文核心实体（仓库）
- [[ClaudeCode]] — 被实践的目标 Agent
- [[Command-Agent-Skill编排]] — 核心编排架构
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发工作流
- [[跨模型工作流]] — 多模型协作机制
- [[Skill]] — 核心能力之一
- [[Hooks]] — 核心能力之一
- [[MCP]] — 核心能力之一
- [[CLAUDEmd]] — 实战技巧涉及的指令文件
- [[OpenSpec]] — 收录的工作流项目
- [[Codex]] — 跨模型工作流可接入的模型
- [[DeepSeek]] — 跨模型工作流可接入的模型
- [[Gemini]] — 跨模型工作流可接入的模型
