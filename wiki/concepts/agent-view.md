---
title: "agent-view"
type: concept
tags: [概念, ClaudeCode, 后台会话, Supervisor, 多任务]
sources: [raw/09-archive/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md]
last_updated: 2026-09-28
---

## 定义

Agent 视图（`claude agents`）是 Claude Code v2.1.139 引入的集中管理所有后台会话的界面，依托独立的 **Supervisor 进程**托管会话：会话生命周期与终端窗口解耦，可关掉界面、开新终端甚至新交互会话而任务继续运行，状态在 `~/.claude/daemon/` 下维护。

## 关键信息

- **冷热分离**：后台会话完成并空置约 1 小时后 Supervisor 自动停止进程释放资源；下次 attach/peek 时从磁盘状态无缝重启（有状态服务的经典思路）
- **Worktree 隔离**：每个新后台任务自动隔离到 `.claude/worktrees/` 下的独立 git worktree，解决多并行会话改同一仓库的文件冲突，最后各自 merge/push
- **状态模型**：`Needs input` / `Working` / `Completed` 三态；图标 `✽`/`✻` 进程活跃可立即回复，`∙` 进程已退出但状态保留（reply 会重启），`✢` 是 `/loop` 循环任务的迭代间隙
- **被动通知取代盯屏**：会话打开 PR 时该行直接显示 PR 链接 + CI 状态，「PR opened + CI green」即全部所需信息——人不该主动盯工具，工具应在需要时才来找人
- **踩坑**：多后台会话配额消耗是乘法不是加法（8 个并行半天吃掉 Max 约 60% 配额，先 `/usage` 看余量）；机器睡眠会暂停全部后台会话，开盖后需手动 `claude respawn --all`；异常终止会留下孤儿 worktree，用 `git worktree list/remove` 清理
- 状态：研究预览（Research Preview），企业管理员可用 `disableAgentView` 关闭；资源按需分配，全部完成且无终端 attached 时 Supervisor 自身退出

## 关联连接
- [[ClaudeCode]] — 所属产品
- [[Subagent]] — 后台并行执行单元
- [[Worktree]] — 会话隔离机制
- [[goals]] — 同版本引入的目标收敛命令
- [[摘要-claude-code-agent视图与goal]] — 来源
