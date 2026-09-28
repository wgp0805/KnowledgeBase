---
title: "Worktree"
type: concept
tags: [Git, 隔离, Agent, 工作流, Codex]
sources: [raw/01-articles/3 分钟掌握 Codex 97% 的功能，超实用教程！.md, raw/01-articles/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md, raw/01-articles/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md]
last_updated: 2026-09-28
---

## 定义
Worktree（工作树隔离）是给 AI Agent 开一个隔离工作区的机制，Agent 可以在其中改代码、试功能、跑实验，但不直接污染主项目。做坏了直接丢掉，不用在主目录收拾残局。

## 关键信息
- 核心价值：多个需求并行时互不影响（一个分支做登录、一个做支付、一个修 bug）
- 选择标准：
  - **Local**：小修补（如改一句文案）
  - **Worktree**：重要构建、大范围改代码、多需求并行
  - **Cloud**：长时间运行的自动化任务
- 大部分情况下 Worktree 是最安全的选择

### Claude Code 的自动 Worktree 隔离（2026-09）
来自 [[摘要-claude-code-agent视图与goal]]。Agent 视图开启新后台任务时，Claude 自动把它隔离到 `.claude/worktrees/` 下的独立 worktree——解决多个并行会话改同一仓库的文件冲突，各自 merge/push 后互不干扰。坑：会话异常终止会遗留孤儿 worktree，用 `git worktree list` 排查、`git worktree remove <path>` 清理。

### Orca 的并行 Worktree 对比挑选（2026-09）
来自 [[摘要-orca-ade多agent协作]]。Orca 把 worktree 用成「多方案竞速」：同一需求派给多个 Agent，每个分到独立目录+独立分支，跑完在统一界面并排看 diff，挑一份最满意的合并、其余丢弃；还可从 GitHub/Linear 任务一键开出新 worktree。

## 关联连接
- [[Codex]] — 核心使用工具
- [[Git]] — 底层版本控制机制
- [[ClaudeCode]] — 自动创建 worktree 的工具
- [[Orca]] — 并行 worktree 对比挑选的 ADE
- [[agent-view]] — 后台会话的 worktree 隔离
- [[Subagent]] — 隔离的并行执行单元
- [[摘要-codex-97percent-技巧]] — 来源
- [[摘要-claude-code-agent视图与goal]] — 来源（Claude Code 自动隔离）
- [[摘要-orca-ade多agent协作]] — 来源（Orca 并行对比）
