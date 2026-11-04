---
title: "摘要-ccstatusline-状态栏"
type: source
tags: [来源, Claude Code, 工具, 终端]
sources: [raw/09-archive/2026-10-31 - 给ClaudeCode装上这个超酷的状态栏，逼格瞬间拉满！.md]
last_updated: 2026-11-02
---

## 核心摘要

「终码一生」介绍 Claude Code 终端状态栏工具 **ccstatusline**（GitHub `sirmalloc/ccstatusline`，9k+ Star，v2.2.19）。它把模型名称、Git 分支、上下文占用、Token 用量、费用估算、实时速度全部实时显示在终端底部，解决「用哪个模型、上下文吃了多少、这个会话花了多少钱、现在在哪个分支上」全两眼一抹黑的痛点。

核心功能：

- **Token 与费用监控**：输入 Token、输出 Token、总量、会话费用（美元）；Token 速度组件支持 0-120 秒滑动窗口（0 = 整个会话平均速度）
- **上下文可视化**：长度、百分比、进度条、Compaction Counter（压缩次数，判断是否该开新对话）
- **Git 信息**：分支名、暂存/未暂存文件数、冲突数、ahead/behind、SHA、PR 信息（GitHub/GitLab）、增删行数；分支组件可配成终端内可点击链接
- **Powerline 主题**：内置多套主题，箭头分隔符 + 渐变配色，支持 16 色、256 色、真彩色
- **交互式 TUI 配置**：一条命令弹出终端 UI，添加/删除/排序组件、设置颜色、切换主题、实时预览；70 个组件带模糊搜索

安装：

```bash
npm install -g ccstatusline-zh        # 全局安装中文版（推荐）
npx -y ccstatusline@latest            # 临时运行
```

随后在 `~/.claude/settings.json`（Windows 为 `%USERPROFILE%\.claude\settings.json`）中加 `statusLine` 配置块，指定 `type: command`、`command: ccstatusline-zh`、`padding`、`refreshInterval`（1-60 秒，Claude Code 2.1.97 以下不支持该字段）。

注意事项：让 Claude Code 帮忙装可以，但配置最好自己执行 `ccstatusline-zh setup` 来做，容易出问题。

## 关联连接
- [[ccstatusline]] — 被介绍的工具
- [[ClaudeCode]] — 宿主 CLI
- [[Token估算]] — Token 用量相关概念
- [[上下文压缩]] — Compaction 相关概念
