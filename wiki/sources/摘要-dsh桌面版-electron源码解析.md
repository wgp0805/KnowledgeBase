---
title: "摘要-dsh桌面版-electron源码解析"
type: source
tags: [来源, DeepSeekHarness, 桌面版, Electron, 插件]
sources: [raw/01-articles/DeepSeek桌面版真不错，再见了WebUI。.md]
last_updated: 2026-09-29
---

## 核心摘要

[[沉默王二]]（2026-09-28）实测 DeepSeek Harness 官方桌面版（自动升级 v0.1.7-rc.2），并拉源码解析其实现。核心结论：**桌面版没有重写界面**——用 Electron 打包，主窗口加载完整 WebUI 页面，子进程跑 `dsh web` 同一套本地服务（端口 3080→19387）。桌面版补上的是"Agent 常驻本机"的能力：electron-updater 自动更新（nightly 通道、10 分钟检查、需手动确认下载）、关窗口任务继续跑、自带 Python/Node/pnpm 与 Office Skills、内置浏览器。登录走 OAuth PKCE，令牌存 `~/.dsh/credentials.yaml`（0600 权限）。

**插件推荐**：DSH-better-sidebar（侧边栏/分栏底座，支持上下文自动注入的 Side Chat）、dsh-TUI（终端界面，Sixel/Kitty 图片预览、时间回溯）、DeepSeek Harness 插件库（deepseek-harness-plugin.com）。作者观点：插件够用即可，模型能力提升后部分 Skills/MCP/插件会被吃掉，Memory 官方做法就是最优解。

**Everything is a Plugin 源码级拆解**：
- Agent loop、工具注册表、会话日志、上下文压缩、Sub-agent、Skills 加载、MCP 客户端**全部是插件**，建立在 [[Cordis]] 框架上（导出 `apply(ctx)` + `inject` 声明服务依赖）
- 插件打成 npm 包（bundle），`package.json` 的 `dsh` 字段指向 `cordis.patch.yml` 增量补丁，启动时基础 bundle → 各 bundle patch → profile patch → 用户 patch 逐层叠加
- **profile 隔离**：WebUI 用 `~/.dsh/profiles/web`，桌面版用 `~/.dsh/profiles/desktop`，会话/设置/凭证共享但**插件不共享**；`desktop` profile 只归 Electron 应用管，命令行拒绝访问
- **插件无沙箱**：服务端代码直接跑在 Agent 宿主进程里，桌面版上宿主与所有插件共用同一 Electron Node 进程，页面部分同页运行无 iframe 隔离——官方 SAFETY.md 提醒不要装来路不明的插件

**跨会话记忆现状**：无官方长期记忆工具，靠 `~/.dsh/AGENTS.md` + 项目 AGENTS.md/CLAUDE.md（首次请求注入，预算 65536 字节）；会话内靠 JSONL 日志 + 自动压缩/`/compact`；`session_search` 工具源码存在但未在内置预设启用。

## 关联连接
- [[沉默王二]] — 文章作者
- [[DeepSeekHarness]] — 解析对象
- [[Cordis]] — DSH 插件框架
- [[everything-is-a-plugin]] — 该文提炼的核心概念
- [[摘要-deepseek-harness桌面客户端]] — 另一篇桌面客户端实测（欧阳俊杰视角）
- [[摘要-deepseek-harness必装10个插件-程序汪]] — 插件推荐的前作
- [[Electron]] — 桌面版打包框架
- dsh-TUI — 推荐插件（终端界面）
- [[WorkBuddy]] — 同赛道产品
- [[豆包工作]] — 同赛道产品
