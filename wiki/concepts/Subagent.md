---
title: "Subagent"
type: concept
tags: [概念, AI工程, ClaudeCode, 多智能体]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md, raw/01-articles/2026-08-26-Claude Code 与 Grok Bot 被拆开后：AI Agent 真正难复制的是什么？.md, raw/01-articles/2026-09-23-开多个 Agent 后 Claude Code 账单翻了 4 倍，一个配置解决了 - 码哥字节.md]
last_updated: 2026-09-28
---

## 定义
Subagent（子 Agent）是 [[ClaudeCode]] 的并行执行单元。在 [[AINativeSDLC]] 中，并行会话用各自 git worktree 隔离，子 agent 定义在 .claude/agents/，拥有独立上下文和工具权限。子 Agent 让复杂任务可分解、可并行，是 [[TaskDelegationSystem]] 中"控制能力"的体现。

## 关键信息
- **自动创建**：子 Agent 不是用户手动启动的，Claude Code 判断任务需要并行时自动拆分子任务并创建多个独立 Agent 实例；各自工具权限、各自上下文窗口、互相不可见，完成后只向主 Agent 汇报结果（详见 [[摘要-claude-code-多agent账单分层路由]]）
- **独立计费**：每个子 Agent 是独立 Claude 实例，各自消耗 token——一条指令开出 3-5 个子 Agent 是账单翻倍的直接原因
- **模型可单独路由**：子 Agent 默认走「Haiku 级」模型，可用 `ANTHROPIC_DEFAULT_HAIKU_MODEL` + `CLAUDE_CODE_SUBAGENT_MODEL` 显式绑定更便宜的模型，把读文件、搜索这类简单任务与主 Agent 的深度推理分离（见 [[模型路由]]）
- **自定义子 Agent**：`.claude/agents/*.md` 的 YAML frontmatter 可用小写 `model` 字段覆盖全局路由（如 code-reviewer 用 Flash、architect 用带 1M 上下文的 Pro）
- **成本核算示例**：15 文件重构开 4 个子 Agent（2 Explore + 1 General-purpose + 1 Plan），全 Sonnet 与分层路由的成本差可达 17 倍

## 关联连接
- [[AINativeSDLC]] — 所属框架
- [[ClaudeCode]] — 所属工具
- [[TaskDelegationSystem]] — 任务托付能力
- [[子Agent编排]] — 相关概念
- [[subagent-driven-development]] — 相关实践
- [[Worktree]] — 并行会话的隔离手段
- [[模型路由]] — 子 Agent 独立绑定模型
- [[agent-view]] — 子 Agent 后台会话的集中管理
- [[摘要-claude-code-多agent账单分层路由]] — 来源（子 Agent 计费与路由）
