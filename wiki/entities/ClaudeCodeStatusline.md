---
title: "claude-code-statusline"
type: entity
tags: [工具, ClaudeCode, 状态栏, 开源, npm]
sources: [raw/01-articles/2026-10-18-Claude Code 自定义状态栏工具：安装、配置与 Subagent 状态展示 - fbincon.md]
last_updated: 2026-10-19
---

## 定义
claude-code-statusline 是博客园作者 fbincon 开源的 Claude Code 自定义状态栏工具：把模型、目录、Git、上下文余量、限额、Token、任务用时集中显示在会话底部，并提供**可配置的子 Agent 独立状态行**（主栏 60 个显示项 + 子 Agent 行 14 个显示项）。MIT 许可，GitHub/Gitee 双仓库同步。

## 关键信息
- **版本分水岭（2026-10-18）**：v3.0.0 起用 TypeScript 重构原 Python 实现，改由 npm 分发 `@fbincon/claude-code-statusline`（需 Node.js 22.x/24.x，正常安装无需 Python/pipx/编译器）；pipx 包 `fbincon-claude-code-statusline` 保留至 v2.0.0 为止
- **安装与接入两步走**：`npm install --global --ignore-scripts ...` 后必须 `claude-statusline install` 写入接入 + `doctor` 体检，重启 Claude Code 生效；Windows 入口是 `claude-statusline.cmd`
- **三配置入口共享一份配置**：独立 TUI `configure`（Ctrl+S 保存）、会话内 `/statusline-configure`（2.1.258+）/ `/statusline-configure-native`（2.1.287+，S 保存/F 退出/Q 放弃）、`/statusline-config` 问答式（耗模型回合）；状态栏渲染本身不发网络请求、不耗 token
- **子 Agent 状态行**：需 Claude Code 2.1.205+（逐任务 effort 需 2.1.214+）；每行显示任务状态用时/名称/模型/上下文/任务标签，可隐藏已完成、限 6 行
- **预设与迁移**：`minimal/developer/monitoring/multi-agent` 四预设；`config export/import ./statusline.json` 跨机器迁移（支持 `--dry-run`）
- **实时指标**：npm 新版默认关闭，`install --native-timing`（需 2.1.289+）或 `install --live-metrics` 开启；无观测显示 `—`，任务进度不能推算剩余时间
- **定位区分**：与 [[ccstatusline]]、[[claude-hud]] 是**不同工具**（后两者见 [[摘要-claude-code-statusline]]），本工具特色是子 Agent 独立状态行与任务计时

## 关联连接
- [[摘要-fbincon-claude-code-statusline]] — 来源（安装配置完整教程）
- [[摘要-claude-code-statusline]] — 同主题既有摘要（另外两款工具）
- [[ClaudeCode]] — 宿主工具
- [[Subagent]] — 子 Agent 状态行的展示对象
- [[Hooks]] — 接入 Claude Code 的机制之一
- [[Node.js]] — v3 版本运行环境
