---
title: "Orca"
type: entity
tags: [开源项目, ADE, 多Agent, 开发环境]
sources: [raw/09-archive/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md]
last_updated: 2026-09-28
---

## 定义

Orca 是 Stably AI（YC 孵化）开源的 ADE（Agent Development Environment，智能体开发环境），GitHub 约 6.7 万 Star。定位与传统 IDE 相反：AI 不是插件，干活的主力是 Agent，人负责派任务、看进度、跑完挑结果。

## 关键信息

- **不含模型**：无需注册 Orca 账号，直接复用本地已登录的命令行 Agent；官方具名近 30 种（Claude Code、Codex、OpenCode、Grok、Cursor CLI、GitHub Copilot CLI、Kimi、Qwen Code、MiMo Code 等）——只要能在终端跑，就能放进 Orca
- **并行 Worktree**：同一需求派给多个 Agent，各自独立目录+独立分支，跑完并排看 diff 挑一份合并，其余丢弃
- **其他功能**：WebGL 无限分屏终端（重启保留回滚记录、完成通知）、Design Mode（内置 Chromium，点选页面元素把 HTML/CSS/截图一起发给 Agent）、Diff 行级批注、GitHub 与 Linear 集成（从任务一键开 worktree）、SSH 远程 Worktree（断线重连+端口转发）、多账号用量与限流重置时间管理
- **手机端**：iOS/Android App 与桌面配对，Agent 完成后推送通知，人不在电脑前也能发后续指令
- **Orca CLI**：建 worktree、打快照、点界面均可脚本化，Agent 可反向驱动 Orca 接入自动化
- **成本提示**：Orca 本身免费，但 token 消耗按 Agent 数量算，5 个 Agent 并行就是 5 份消耗
- 安装：`brew install --cask stablyai/orca/orca`，Windows/Linux 走 onorca.dev 或 GitHub Releases

## 关联连接
- [[agent-development-environment]] — 所属品类概念
- [[Worktree]] — 并行协作的隔离机制
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ClaudeCode]] — 可接入的 Agent
- [[Codex]] — 可接入的 Agent
- [[GitHub]] — 项目托管平台
- [[程序员追风]] — 介绍文章作者
- [[摘要-orca-ade多agent协作]] — 来源
