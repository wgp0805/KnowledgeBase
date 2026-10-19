---
title: "摘要-fbincon-claude-code-statusline"
type: source
tags: [来源, Claude Code, 状态栏, 工具教程, npm]
sources: [raw/01-articles/2026-10-18-Claude Code 自定义状态栏工具：安装、配置与 Subagent 状态展示 - fbincon.md]
last_updated: 2026-10-19
---

## 核心摘要

博客园作者 fbincon 的官方教程，介绍其开源 Claude Code 自定义状态栏工具 **claude-code-statusline**：主状态栏 60 个显示项 + 子 Agent 独立行 14 个显示项，把模型、Git、上下文余量、Token、任务用时集中到会话底部。**2026-10-18 更新：v3.0.0 起用 TypeScript 重构原 Python 实现，改由 npm 分发**（`@fbincon/claude-code-statusline`），pipx 只保留到 v2.0.0。

注意：与既有 [[摘要-claude-code-statusline]]（介绍 ccstatusline / claude-hud 两款第三方工具）是**不同工具**，本页介绍作者本人开发的第三款。

## 关键信息

### 版本与安装（v3 npm 版）
- **v2.0.0 及之前**：Python + pipx，包名 `fbincon-claude-code-statusline`；**v3.0.0 及之后**：Node.js 22.x/24.x + npm，包名 `@fbincon/claude-code-statusline`
- 安装：`npm install --global --ignore-scripts @fbincon/claude-code-statusline`（Windows 入口为 `claude-statusline.cmd`）
- **安装包 ≠ 接入**：需依次 `claude-statusline --version` → `install --dry-run`（预览）→ `install`（写入接入）→ `doctor`（体检），然后重启 Claude Code
- `pipx upgrade` 只管历史 Python 包，不能升到 v3.x；迁移需备份 `~/.claude` 配置目录，可用 `npm install --prefix ./statusline-node` 独立目录并存避免 PATH 同名冲突
- 卸载同样两步：先 `claude-statusline uninstall` 移除接入，再 `npm uninstall --global`

### 状态栏信息口径
- Git：`↑N/↓N` 领先/落后上游提交数，`●N` 暂存、`~N` 未暂存、`?N` 未跟踪、`!N` 冲突
- `Context 73% left` 是上下文窗口余量，与账户限额、会话累计 token 分别统计；tokens 的 `hit`（缓存读）/`miss`（普通输入+缓存创建）/`out`（输出），统计含可发现的子 Agent transcript
- 任务计时含排队、用户等待、子 Agent 工作与主 Agent 收尾；`⏱`运行 `✓`成功 `■`中断 `✗`失败；需排除用户等待可另选 `task-active-timer`

### 配置方式（三入口共享同一份配置）
1. 独立 TUI：`claude-statusline configure`（窗口 ≥64×18，Main/Subagents/Settings/Layout 四页，**保存统一用 Ctrl+S**）
2. 会话内 `/statusline-configure`（Claude Code 2.1.258+，外部 TUI）或 `/statusline-configure-native`（2.1.287+，面板内 S 保存/F 保存退出/Q 放弃）
3. `/statusline-config` 问答式配置（消耗模型回合）；状态栏渲染本身不发网络请求、不耗模型 token

### 三组现成配置
- 精简开发视图：`config set-items model-with-effort current-dir git context-remaining task-timer`（`set-items` 是**替换**启用集合，追加用 `enable`）
- 限额与 token 视图：`set-items five-hour-limit weekly-limit spend-limit tokens`
- 子 Agent 状态行（需 Claude Code 2.1.205+，逐任务 effort 需 2.1.214+）：`subagents set-items status-elapsed name model-with-effort context-remaining task` + `subagent-hide-completed on` + `subagent-row-limit 6`
- 四套预设 `minimal/developer/monitoring/multi-agent` 可 `preset developer --dry-run` 预览后应用；`config export/import ./statusline.json` 跨机器迁移（`--dry-run` 先检查）

### 实时指标与注意
- npm 新版**默认关闭**原生计时与高级实时采集：`install --native-timing`（仅计时）或 `install --live-metrics`（完整采集），均要求 Claude Code 2.1.289+，执行后 `doctor` 并重启
- 常见故障第一排查命令是 `claude-statusline doctor`；无有效观测时字段显示 `—`，有限覆盖或最近观测带 `*`；任务进度来自结构化任务记录，不能据此推算剩余时间
- 项目：MIT 许可，GitHub/Gitee 双仓库，npm + 中文使用指南 + CLI 参考

## 关联连接
- [[ClaudeCodeStatusline]] — 本文介绍的工具实体
- [[ClaudeCode]] — 宿主工具
- [[摘要-claude-code-statusline]] — 同主题既有摘要（介绍 ccstatusline/claude-hud 两款工具，与本文工具不同）
- [[ccstatusline]] — 既有状态栏工具
- [[claude-hud]] — 既有状态栏工具
- [[Subagent]] — 子 Agent 状态行展示对象
- [[Hooks]] — 工具接入 Claude Code 的机制之一
