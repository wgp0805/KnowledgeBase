---
title: "ccstatusline"
type: entity
tags: [工具, Claude Code, 状态栏, 终端]
sources: [raw/09-archive/给 Claude Code 装上这个超酷的状态栏，逼格瞬间拉满！.md, raw/01-articles/2026-10-31 - 给ClaudeCode装上这个超酷的状态栏，逼格瞬间拉满！.md]
last_updated: 2026-11-02
---

## 定义

ccstatusline 是一款开源的 Claude Code 终端状态栏工具（GitHub `sirmalloc/ccstatusline`，9k+ Star，迭代至 v2.2.19），可以在终端底部常驻显示模型名称、Git 分支、上下文占用、Token 用量、费用估算、实时速度等关键信息，安装配置简单，支持交互式 TUI 配置界面与 Powerline 主题。

## 关键信息

- **GitHub 仓库**：https://github.com/sirmalloc/ccstatusline
- **中文版**：`huangguang1999/ccstatusline-zh`，包名 `ccstatusline-zh`
- **安装方式**：
  - 全局安装：`npm install -g ccstatusline-zh`（推荐，中文版）
  - npx：`npx -y ccstatusline@latest`
  - bunx：`bunx -y ccstatusline@latest`
- **配置方式**：
  - 交互式 TUI 界面配置（推荐）：`ccstatusline-zh setup`
  - 直接编辑 `~/.config/ccstatusline/settings.json`
  - 让 Claude Code 代装可以，但配置最好自己执行 `ccstatusline-zh setup` 来做
- **在 settings.json 中写入 statusLine 配置块**：

```json
{
  "statusLine": {
    "type": "command",
    "command": "ccstatusline-zh",
    "padding": 0,
    "refreshInterval": 10
  }
}
```

- **功能特性**：
  - **Token 与费用监控**：输入 Token、输出 Token、总量、会话费用（美元）；速度组件支持 0-120 秒滑动窗口
  - **上下文可视化**：长度、百分比、进度条、Compaction Counter（压缩次数，判断是否该开新对话）
  - **Git 信息**：分支、暂存/未暂存文件数、冲突数、ahead/behind、SHA、PR 信息（GitHub/GitLab）、增删行数；分支组件可配成终端内可点击链接
  - **Powerline 主题**：内置多套主题，16 色/256 色/真彩色
  - **交互式 TUI 配置**：一条命令弹出终端 UI，70 个组件可挑可排序，带模糊搜索
- **推荐显示项**：模型、思考程度、Git 分支、上下文、用量
- **工作原理**：向 Claude Code 的 `settings.json` 写入 `statusLine` 配置，通过命令渲染状态栏
- **refreshInterval**：1-60 秒；Claude Code 2.1.97 以下版本不支持该字段

## 关联连接
- [[摘要-ccstatusline-状态栏]] — 最新来源
- [[摘要-claude-code-statusline]] — 早期来源
- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[Token估算]] — Token 计量概念
- [[上下文压缩]] — Compaction 计数的对照概念
- [[终码一生]] — 最新来源作者
