---
title: "claude-code-best-practice"
type: entity
tags: [GitHub, ClaudeCode, 最佳实践, 开源仓库]
sources: ["raw/01-articles/夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！.md"]
last_updated: 2026-06-24
---

## 定义
**claude-code-best-practice** 是 GitHub 上斩获 **57k+ Star** 的 [[ClaudeCode]] 最佳实践开源仓库，系统整理了 Claude Code 生态被社区验证过的核心能力分类、热门功能、工作流模式、Skill/Agent 精选集与 83 条实战技巧。

## 关键信息

### 五大板块
1. **核心能力（Concepts）**：Subagents、Commands、Skills、Workflows、Hooks、MCP Servers、Plugins
2. **热门功能（Features）**：Ultrareview、Devcontainers、Channels、Ultraplan、No Flicker Mode、Auto Mode、Power-ups、Fast Mode、Computer Use 等
3. **工作流（Workflows）**：
   - [[Command-Agent-Skill编排]] 架构
   - [[Research-Plan-Execute-Review-Ship]] 五阶段开发范式
   - [[跨模型工作流]]（Plugin / MCP / Router 三种机制）
4. **Skill/Agent 精选集**：Superpowers、Everything Claude Code、Matt Pocock Skills、Spec Kit、gstack、Get Shit Done、[[OpenSpec]] 等
5. **83 条实战技巧（Tips）**：覆盖 Prompting、Planning、Context、Session Management、Memory、Agents、Commands、Skills、Hooks、Workflows、Git/PR、Debugging、Utilities、Daily practices 等方向

### 经典 Tips 节选
- Tip #1：[[CLAUDEmd|CLAUDE.md]] 每个文件应控制在 **200 行以下**
- Tip #2：`.claude/rules/*.md` 会在每个会话中**自动加载**

### 核心理念
> **Claude Code 不是不能干复杂的活，而是必须拆阶段进行。**

推荐的使用顺序：
- 先读 **Concepts**（搞清楚有哪些能力）
- 再读 **Workflows**（学习工作流编排）
- 最后看 **Tips**（落地到日常项目）

### 跨模型工作流的三种接入方式
- **插件（Plugin）**：另一个模型的 CLI 在 Claude Code 内部运行（如 codex-plugin-cc）
- **MCP**：Claude Code 通过 Model Context Protocol 将另一模型作为工具调用
- **路由器（Router）**：Claude Code 的 API 端点被切换到不同的模型提供商

## 关联连接
- [[摘要-claude-code-best-practice]] — 来源
- [[ClaudeCode]] — 被实践的目标 Agent
- [[Command-Agent-Skill编排]] — 核心编排架构
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发范式
- [[跨模型工作流]] — 跨模型协作机制
- [[OpenSpec]] — 收录的工作流项目之一
- [[Codex]] — 可接入的模型
- [[DeepSeek]] — 可接入的模型
- [[Gemini]] — 可接入的模型
- [[CLAUDEmd]] — 实战技巧涉及
- [[Skill]] — 仓库整理的核心能力
- [[Hooks]] — 仓库整理的核心能力
- [[MCP]] — 仓库整理的核心能力
