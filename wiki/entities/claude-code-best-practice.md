---
title: "claude-code-best-practice"
type: entity
tags: [GitHub, ClaudeCode, 最佳实践, 开源仓库]
sources:
  - "raw/01-articles/夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！.md"
  - "raw/01-articles/开源了！Claude Code 最佳实践 60 天斩获 54k Star，前后端开发直接起飞了！.md"
last_updated: 2026-06-26
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

### 三条最值得抄走的实战技巧（苏三视角补充）
- **上下文 40% 阈值**：Context rot 在 300-400k token 处显现，维持总 context 利用率 < 40%，超过 300k 主动 `/compact`
- **Plan 与 Execute 分 Session**：Plan 阶段产出 commit 到 Markdown，新开 Session 读 markdown 执行，避免中间稿污染 context
- **Hook 用于强制纪律而非加功能**：`PostToolUse` hook 在改 src/ 时自动 `mvn test`，消除"忘跑测试就 commit"的坑

### 跨模型工作流的三种接入方式
- **插件（Plugin）**：另一个模型的 CLI 在 Claude Code 内部运行（如 codex-plugin-cc）
- **MCP**：Claude Code 通过 Model Context Protocol 将另一模型作为工具调用
- **路由器（Router）**：Claude Code 的 API 端点被切换到不同的模型提供商

### 推荐的跨模型组合
**Claude Code 写代码 + [[Codex]] 评审**：不同模型互相挑刺，比单一模型自审更客观，能发现 Claude 自己看不出的边界问题。

## 关联连接
- [[摘要-claude-code-best-practice]] — 来源（首次摘要）
- [[摘要-claude-code-best-practice-苏三视角]] — 来源（实战技巧深读）
- [[ClaudeCode]] — 被实践的目标 Agent
- [[Command-Agent-Skill编排]] — 核心编排架构
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发范式
- [[跨模型工作流]] — 跨模型协作机制
- [[Superpowers]] — 收录的工作流之一
- [[SpecKit]] — 收录的工作流之一
- [[OpenSpec]] — 收录的工作流之一
- [[Codex]] — 可接入的模型 / 跨模型评审搭档
- [[DeepSeek]] — 可接入的模型
- [[Gemini]] — 可接入的模型
- [[CLAUDEmd]] — 实战技巧涉及
- [[Skill]] — 仓库整理的核心能力
- [[Hooks]] — 仓库整理的核心能力
- [[MCP]] — 仓库整理的核心能力
- [[ContextManagement]] — 40% 阈值技巧涉及

- [[claude-code-增强框架对比]] — Claude Code 四大增强框架横向对比
