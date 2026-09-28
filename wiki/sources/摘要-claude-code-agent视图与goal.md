---
title: "摘要-claude-code-agent视图与goal"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md]
last_updated: 2026-09-28
---

# 摘要-claude-code-agent视图与goal

## 核心摘要

Claude Code v2.1.139 的真正价值不在 30+ 个 bug fix，而在协作模型的改变：从「你说我做」变成「你给目标我自己搞定」。Agent 视图（`claude agents`）依托独立 Supervisor 进程托管后台会话，与终端解耦、空置约 1 小时自动停进程再从磁盘无缝重启（冷热分离），并自动把每个后台会话隔离到 `.claude/worktrees/` 下的独立 git worktree。`/goal` 命令则引入「目标状态收敛」执行模型：Claude 每个 turn 结束自动评估是否达标，不满足就继续，控制权从用户转给模型——与 Kubernetes Reconcile Loop 同构，但判断基于语言理解而非精确状态，因此目标必须写成可机器验证的命令。配套改动还包括 MCP Server 自动接收 `CLAUDE_PROJECT_DIR`、`claude plugin details` 输出插件 token 成本、`/context all` 按模型分词器精确计数。踩坑：多后台会话配额消耗是乘法、机器睡眠会中断会话（需 `claude respawn --all`）、worktree 需清理、模糊 goal 会让模型走捷径。

## 关联连接
- [[ClaudeCode]] — 更新所针对的产品
- [[agent-view]] — 该文提炼的 Agent 视图概念
- [[goals]] — /goal 目标收敛执行模型
- [[Worktree]] — 后台会话的隔离手段
- [[Subagent]] — 多会话并行的执行单元
- [[码哥字节]] — 文章作者
