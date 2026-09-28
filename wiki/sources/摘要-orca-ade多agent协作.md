---
title: "摘要-orca-ade多agent协作"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md]
last_updated: 2026-09-28
---

# 摘要-orca-ade多agent协作

## 核心摘要

Orca 是 Stably AI（YC 孵化）开源的 ADE（Agent Development Environment，智能体开发环境），GitHub 已 6.7 万 Star：传统 IDE 里 AI 只是插件，Orca 里干活的主力是 Agent，人负责派任务、看进度、挑结果。它自己不含模型也不需注册账号，直接复用本地已登录的命令行 Agent（官方具名近 30 种：Claude Code、Codex、OpenCode、Cursor CLI、Kimi、Qwen Code 等），核心功能是并行 worktree——同一需求派给多个 Agent，各自独立目录+分支，跑完并排看 diff 挑一份合并，配套 WebGL 无限分屏终端、Design Mode 点选页面元素提需求、Diff 行级批注、GitHub/Linear 集成、SSH 远程 worktree、iOS/Android 手机 App 通知与远程发指令、多账号用量与限流管理、可被 Agent 反向驱动的 Orca CLI。注意 Orca 本身免费，但 token 消耗按 Agent 数量算，五个 Agent 就是五份消耗。

## 关联连接
- [[Orca]] — 该文介绍的开源项目实体
- [[agent-development-environment]] — 该文提炼的 ADE 概念
- [[Worktree]] — Orca 并行协作的核心隔离机制
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ClaudeCode]] — 可接入 Orca 的 Agent 之一
- [[Codex]] — 可接入 Orca 的 Agent 之一
- [[GitHub]] — 项目托管平台
- [[程序员追风]] — 文章作者
