---
title: "Command-Agent-Skill编排"
type: concept
tags: [ClaudeCode, 工作流, 编排, Agent]
sources: ["raw/01-articles/夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！.md"]
last_updated: 2026-06-24
---

## 定义
**Command-Agent-Skill 编排** 是 [[ClaudeCode]] 生态被社区总结出的核心系统工程化模式：
- **Command** 负责**触发任务**（如 `/test`、`/review`、`/explain`）
- **Agent** 负责**扮演角色**（如安全审查员、性能审查员、前端工程师）
- **Skill** 负责**提供专业能力**（领域知识、SOP、工具组合）

三层组合，把"用户意图→角色化执行→专业能力供给"串成完整链路，是 Claude Code 区别于普通对话工具的关键工程范式。

## 关键信息

### 三角色职责
| 层 | 职责 | 实例 |
|---|---|---|
| Command | 入口触发 | `/test`、`/pr-review`、`/explain` |
| Agent | 角色与子任务编排 | Subagent（安全审查/性能审查/无障碍审查） |
| Skill | 专业能力供给 | 前端设计 Skill、Plan Skill、URule 规则 Skill |

### 与其他工作流的关系
- 与 [[Research-Plan-Execute-Review-Ship]] 互补：后者是**阶段流水线**，前者是**单阶段内的编排架构**
- 与 [[multi-agent-collaboration]] 衔接：Command 可以触发一个调度 Agent，再让它派发到子 Agent
- 与 [[Skill]] / [[Hooks]] / [[MCP]] 形成 Claude Code 自动化栈

### 典型示例
仓库给出的"天气系统"工作流：
- Command：`/weather-system-setup`
- Agent：系统编排 Agent，调用工具、查询记忆
- Skill：地理位置查询 Skill、天气接口调用 Skill、报表生成 Skill

## 关联连接
- [[摘要-claude-code-best-practice]] — 来源
- [[claude-code-best-practice]] — 提出仓库
- [[ClaudeCode]] — 落地平台
- [[Skill]] — 三角色之一
- [[Agent]] — 三角色之一
- [[Research-Plan-Execute-Review-Ship]] — 配套五阶段范式
- [[multi-agent-collaboration]] — 上层多 Agent 协作模式
- [[子Agent编排]] — 实现机制
