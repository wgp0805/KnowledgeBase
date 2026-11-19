---
title: "摘要-orca多agent编排桌面应用"
type: source
tags: [来源, 多Agent, 开源项目, 桌面应用, Worktree]
sources: [raw/09-archive/GitHub标星120K+的开源多Agent编排处理神器，就用它了，嘎嘎强！！.md]
last_updated: 2026-11-19
---

## 核心摘要
冰河技术（冰河）2026-11-19 文章，介绍 [[Orca]]——Stably AI 开源（MIT 协议）的桌面端多 Agent 会话编排工具（GitHub 标星 120K+，创始团队有 Chrome 和 Uber 背景）。它不生产模型、不替代惯用 Agent，而是把多个编码 Agent（Claude Code、Codex CLI、OpenCode、Cursor CLI 等）的会话、工作目录和审查动作收进一个桌面应用，核心价值是自动 git worktree 让多 Agent 并行成为默认行为，并把 review 揉进 diff 批注界面。桌面端之外有 iOS/Android 移动端。

## 关键要点
- **统一会话列表**：左侧一列 Agent 会话点选切换，每个 Agent 仍在自己环境里跑，用户不必关心环境散落何处；终端基于 Ghostty 一档实现（WebGL 渲染、分屏可继续拆、重启后滚动缓冲保留）
- **自动 worktree（多 Agent 并行的前提）**：新建 Agent 时自动创建独立 git worktree，删除 Agent 时清理；激进用法——同一提示交给 5 个 Agent 各自在独立 worktree 跑，结果并排比较选最优合并；worktree 共享 git 对象库，磁盘不会因多开迅速膨胀
- **diff 批注反馈**：在 diff 旁直接高亮、写意见、发送给 Agent 修改，减少"看 diff→切聊天窗→等改完→再看 diff"的切换；Markdown 编辑器支持实时预览与文档批注，多处修改意见打包发 Agent 统一处理
- **会话存档与移动端**：所有 Agent 会话存档（对话/diff/改过的文件）支持关键词搜索，旧会话可拖回终端继续聊；iOS App"Orca IDE"与 Android APK 可连本机 Agent 做 review/编辑/查看进度，适合通勤时批 diff 发指令
- **其他能力**：内嵌 Chromium 浏览器（Agent 打开网页/跑交互测试/抓 DOM/端到端流程）；每个 worktree 可挂 iOS/Android 模拟器；Claude Code 多账号一键切换（限流不断上下文，需自备多账号）；拖文件/图片进聊天；SSH 连远程机器跑 Agent（文件编辑/git/终端/自动重连/端口转发）；应用内打开 GitHub 与 Linear 的 PR/Issue；Orca CLI（`orca worktree create`/`snapshot`/`click`/`fill` 等命令可写进脚本）；全局快速打开搜索 worktree/文件/Agent/命令
- **安装与成本**：macOS/Windows/Linux 全平台（包体两百多兆），Homebrew `brew install --cask stablyai/orca/orca`、Arch AUR `yay -S stably-orca-bin`；Orca 本身免费但只当"壳"，模型消耗走用户自己的 API/订阅额度
- **定位与风险**：不是 IDE 也不是项目管理工具，定位"Agent 会话编排层"，适合已大量使用 Agent 的人；仓库开放 issue 达 4.6K 条——功能迭代快但坑不少，应视为快速演进中的工具而非稳定基础设施

## 关联连接
- [[Orca]] — 文章主角（第三篇来源）
- [[Worktree]] — 自动创建的并行隔离机制
- [[multi-agent-collaboration]] — 多 Agent 并行协作模式
- [[ClaudeCode]] — 可接入的 Agent
- [[Codex]] — 可接入的 Agent（Codex CLI）
- [[Cursor]] — 可接入的 Agent（Cursor CLI）
- [[agent-development-environment]] — 所属品类概念
- [[冰河]] — 作者
