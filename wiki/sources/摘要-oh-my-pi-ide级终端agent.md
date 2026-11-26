---
title: "摘要-oh-my-pi-ide级终端agent"
type: source
tags: [来源, 原始文件, AI编程, Agent, 终端, LSP, DAP]
sources: [raw/01-articles/GitHub 38.1k Star 杀疯了！这个能联动 IDE 的终端 AI 编程神器你用了吗？.md]
last_updated: 2026-11-26
---

## 核心摘要
程序汪视角介绍 oh-my-pi（命令名 omp）——一个把 LSP、调试器这些 IDE 才有的能力接进终端的开源编码代理。它由 Stencil Labs 出品，基于 [[MarioZechner]] 的 [[Pi]] 项目 fork 扩展，MIT 协议，TypeScript + Rust 编写（Rust 核心约 8 万行），运行时用 Bun，跨 macOS/Linux/Windows（Windows 无需 WSL）。官方数据：60+ 模型提供商、31 个内置工具、14 个 LSP 操作、28 个 DAP 调试操作。与普通终端代理最大的区别在于"懂类型、引用和调试符号"，而不是停留在文本层面靠字符串匹配改代码。

## 关键信息
- **把 IDE 能力接进终端**：LSP 方面每次写文件都经过语言服务器，重命名调用 `workspace/willRenameFiles`，文件移动前 re-export/barrel 文件/别名导入一起更新，与 VS Code 同一套机制；DAP 方面能驱动真实调试器——C 段错误挂 lldb 单步到出错指针、Go 服务卡住挂 dlv 看 goroutine、Python 挂 debugpy 暂停检查变量，不用到处加 print
- **工具与代码执行**：内置工具是原生实现而非 shell 调外部命令——ripgrep/glob/find 进程内运行，自带 bash 5.3 引擎和 58 个命令（ls/sed/sort/jq），省掉 fork/exec 开销，没装这些命令的机器也能用；提供持久 Python 和 Bun 内核且内核能反向调用代理自己的 read/search 工具，可在 Python 读 CSV 再到 JS 画图不离开会话
- **编辑机制**：文件编辑用 hashline 按内容哈希定位锚点而非重写整段，减少空白冲突与"字符串找不到"，输出 token 下降；有流式规则机制——规则平时不占上下文，模型偏离要求时正则匹配在生成中途中断、注入规则后从断点重新生成
- **模型/配置/协作**：不绑定厂商，60+ provider（Anthropic/OpenAI/Gemini/Grok/MiniMax）用 `/model` 随时切换，可额外配 advisor 模型审查每轮输出；直接读取 Cursor/Cline/Codex 的 AGENTS.md 等八种已有文件无需迁移，扩展中心统一管理 skills 与各 provider 配置；子代理用 `task` 命令拆到隔离 worktree 并行、返回带 schema 校验结果、`Alt+A` 看实时状态；`/collab` 生成链接二维码让同事在别的终端或浏览器加入同一会话（数据帧客户端加密）；`/review` 针对分支/提交/未提交改动出结论，问题按 P0–P3 分级
- **安装**：macOS/Linux `curl -fsSL https://omp.sh/install | sh`（校验 SHA-256）；`bun install -g @oh-my-pi/pi-coding-agent`；Homebrew `brew install can1357/tap/omp`；Windows PowerShell `irm https://omp.sh/install.ps1 | iex`
- **短板与适用人群**：项目很新（2025 年 12 月底建仓）迭代快、open issues 4000+ 可能不稳定；功能配置项多上手成本高于聊天式代理、需理解 LSP/DAP 概念；完整能力要配模型 API Key、本地跑大模型另算；面向需要 IDE 级操作、认真写代码的开发者，不是简单问答工具

## 关联连接
- [[OhMyPi]] — 本文主角实体
- [[Pi]] — fork 的上游项目（Mario Zechner 原版）
- [[MarioZechner]] — Pi 原作者
- [[程序汪]] — 来源作者
- [[LSP]] — 核心能力概念（语言服务器协议）
- [[DAP]] — 核心能力概念（调试适配器协议）
- [[Codex]] — 配置兼容对象
- [[Cline]] — 配置兼容对象
- [[MiniMax]] — 支持的模型 provider
