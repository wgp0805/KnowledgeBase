---
title: "OhMyPi"
type: entity
tags: [AI编程, Agent, 终端, IDE, LSP, DAP, 开源工具]
sources: [raw/01-articles/GitHub 38.1k Star 杀疯了！这个能联动 IDE 的终端 AI 编程神器你用了吗？.md]
last_updated: 2026-11-26
---

## 定义
OhMyPi（命令名 omp）是 Stencil Labs 出品的终端 TUI 编码代理，基于 [[MarioZechner]] 的 [[Pi]] 项目 fork 扩展，MIT 协议，TypeScript + Rust 编写（Rust 核心约 8 万行），运行时用 Bun，跨 macOS/Linux/Windows（Windows 无需 WSL）。GitHub 38.1k Star。与普通终端代理最大的区别是把 LSP、调试器这些 IDE 才有的能力接进了终端，让它"懂类型、引用和调试符号"。

## 关键信息
- **官方数据**：60+ 模型提供商、31 个内置工具、14 个 LSP 操作、28 个 DAP 调试操作
- **IDE 能力（核心差异）**：LSP 每次写文件都经语言服务器，重命名调 `workspace/willRenameFiles`，re-export/barrel/别名导入一起更新（与 VS Code 同机制）；DAP 能驱动真实调试器——C 段错误挂 lldb 单步到出错指针、Go 挂 dlv 看 goroutine、Python 挂 debugpy 暂停检查变量
- **原生工具**：ripgrep/glob/find 进程内运行，自带 bash 5.3 引擎和 58 个命令（ls/sed/sort/jq），省掉 fork/exec 开销，没装命令的机器也能用
- **持久内核**：提供持久 Python 与 Bun 内核，内核能反向调用代理自己的 read/search 工具，可 Python 读 CSV 再到 JS 画图不离开会话
- **编辑与流式规则**：文件编辑用 hashline 按内容哈希定位锚点而非重写整段，减少空白冲突与"字符串找不到"、降低输出 token；流式规则平时不占上下文，模型偏离要求时正则匹配在生成中途中断、注入规则后从断点重新生成
- **模型与配置**：不锁厂商，60+ provider（Anthropic/OpenAI/Gemini/Grok/MiniMax）`/model` 随时切换，可额外配 advisor 模型审查每轮输出；直接读 Cursor/Cline/Codex 的 AGENTS.md 等八种文件无需迁移；扩展中心统一管理 skills 与各 provider 配置
- **协作**：子代理用 `task` 命令拆到隔离 worktree 并行、返回带 schema 校验结果、`Alt+A` 看实时状态；`/collab` 生成链接二维码让同事在别的终端/浏览器加入同一会话（数据帧客户端加密）；`/review` 针对分支/提交/未提交改动出结论，问题按 P0–P3 分级
- **安装**：macOS/Linux `curl -fsSL https://omp.sh/install | sh`（校验 SHA-256）；`bun install -g @oh-my-pi/pi-coding-agent`；Homebrew `brew install can1357/tap/omp`；Windows PowerShell `irm https://omp.sh/install.ps1 | iex`
- **短板**：项目很新（2025 年 12 月底建仓）迭代快、open issues 4000+ 可能不稳定；功能配置项多上手成本高、需理解 LSP/DAP 概念；完整能力要配模型 API Key；面向需要 IDE 级操作、认真写代码的开发者
- **与 Pi 的关系**：Pi 是"大道至简、只给 4 个原语工具"的极简代理，OhMyPi 则在其基础上大幅扩展（内置 31 工具、LSP/DAP、持久内核），走的是"把 IDE 能力塞进终端"的重装路线，与上游哲学形成对照

## 关联连接
- [[Pi]] — fork 的上游项目
- [[MarioZechner]] — Pi 原作者
- [[LSP]] — 核心能力概念
- [[DAP]] — 核心能力概念
- [[Codex]] — 配置兼容对象
- [[Cline]] — 配置兼容对象
- [[MiniMax]] — 支持的 provider
- [[AIAgentsTerminal]] — 终端 AI 编程代理品类
- [[程序汪]] — 来源作者
- [[摘要-oh-my-pi-ide级终端agent]] — 来源
