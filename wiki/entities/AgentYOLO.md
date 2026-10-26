---
title: "AgentYOLO"
type: entity
tags: [IDE插件, Agent, 终端, 开发工具, 跨平台]
sources: ["raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 定义
Agent YOLO 是一个"AI Agent 扩展器"（Cn#工作室出品）：常驻 YOLO 面板列出本机 PATH 上已装的 AI 命令行 Agent，一次点击在 IDE 内真实可交互 PTY 终端拉起，输出中的文件路径、堆栈、类型名、URL 全部可点击直达代码，同一套体验覆盖 IntelliJ、Visual Studio、VS Code 三端。

## 关键信息
**三端差异：**
- **IntelliJ 端**：所有 IntelliJ 平台 IDE 可用，最低 IntelliJ IDEA 2023.3（`233`）；基于 JediTerm + PTY4J（IntelliJ 平台自带的第三方库，非 `@ApiStatus.Internal` 的 Terminal API），不碰内部 API，因此能通过 JetBrains 官方市场审核、像普通插件一样发布（插件 33442-agent-yolo）。另有 `exp` 实验分支：不走独立面板，直接挂到 IDEA 内置 Terminal 的 "AI Agents" 下拉（用内部 Terminal 扩展点），代价是依赖内部 API、无法通过市场审核、最低要 2026.1、不含 main 分支那套链接过滤器；已发布、受支持的主线始终是 main。面板位置：右侧工具窗（`y` 图标），配置在 `Settings > Tools > Agent YOLO`。
- **Visual Studio 端**：版本范围 `[17.0, 19.0)`，覆盖 VS2022 / VS2026；右侧工具窗，从 View 菜单或 `Ctrl+W, Y` 打开；终端为**手绘 ConPTY**（WPF/net472，自实现 VT/ANSI 转义解析与字符网格渲染，不用 WebView2 或 Windows Terminal 控件），文本选择、复制在 TUI 里都正常，Ctrl+C 也能按预期工作；内置 51 个 Agent；配置在 `Tools > Options > Agent YOLO`，图标会校验成真实图片、网络图标 URL 自动下载缓存。
- **VS Code 端**：Activity Bar 的 Agents 面板，node-pty + 内嵌 xterm.js；配置走 `yolo.*` 命名空间、没有面板内设置视图（改完下一次启动 Agent 时生效）；文件路径链接开箱即用（文件系统解析），但类型/成员链接要经 LSP `workspace/symbol` 解析，需装对应语言的 language server（Java 用 Red Hat、TS 内置、Python 用 Pylance……），否则报 "no symbol found"。

**六大共性（三端完全一致）：**
1. 面板只列 PATH 上探测得到的已装 Agent——没装的不出现，列表永远跟当前机器相关（Claude Code、Codex、CodeBuddy、Cursor、Kimi 等一行一个，图标加名称）；
2. 一次点击在 IDE 内真实、可交互的 PTY 终端拉起，不是聊天框模拟；rc 里定义的 PATH（nvm / fnm / npm global bin）照样生效；
3. 输出全可点（详见 [[Agent输出链接化]]）；
4. Y（跳过权限）/ R（恢复会话）双开关按 Agent 独立可定制，**默认关闭、且永远不会自己打开**——Y 追加该 Agent 的跳过权限旗标（Claude Code `--dangerously-skip-permissions`、Codex `--yolo`、CodeBuddy `-y`……），R 追加恢复会话旗标（`-r` / `--resume`）；
5. `agents.json` 数据驱动，增删改都靠改 JSON 而非改源码，自定义工具也能填进去；
6. 每次 Launch 新开一个标签页，多个 Agent 并排跑，像 IDE 自带 Terminal 一样切换。

**维护侧**：三端共用一套 `Meta/` 元数据（图标、i18n、链接正则、范围约束），"改一处 Agent 或图标，要同步三端"（见 [[多端共享元数据]]）。

仓库：https://github.com/cnsharp/agent-yolo

## 关联连接
- [[摘要-agent-yolo-三端ide面板]] — 来源文章
- [[CnSharpStudio]] — 作者工作室
- [[AIAgentsTerminal]] — 同作者前作（VS Code 状态栏版）
- [[Agent输出链接化]] — 输出可点击的核心机制
- [[多端共享元数据]] — Meta/ 三端一致性策略
- [[YOLO模式]] — Y 开关（跳过权限）的理论基础
- [[Resume模式]] — R 开关（恢复会话）
- [[ClaudeCode]] — 支持的 Agent
- [[Codex]] — 支持的 Agent
- [[CodeBuddy]] — 支持的 Agent
- [[IntelliJIDEA]] — IntelliJ 端宿主平台
- [[VSCode扩展]] — VSC 端所属插件生态
