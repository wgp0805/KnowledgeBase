---
title: "摘要-霸榜github-ai逆向神器-rea-archify"
type: source
tags: [来源, REA, Archify, 逆向工程, MCP, 架构图]
sources: [raw/01-articles/霸榜 GitHub 的 AI 逆向神器，玩疯了！.md]
last_updated: 2026-10-20
---

## 核心摘要
开源逆向工程套件 [[REA]] 爆火：把应用交给 Coding Agent，用自然语言提问即可逆向分析功能实现，发文时 Star 已达 24.1 万（两天前 15 万），增速超过当年的 [[OpenClaw]]。REA 本质是基于 [[MCP协议]] 的逆向分析套件，可接入 Claude Code、Cursor、Codex、Gemini CLI 等主流 Coding Agent；Agent 依托它执行"提问、检查、读证据、实现和测试"的严密流程，用静态 AST 分析、解包 ASAR、调用本地 Ghidra/Hopper/IDA 反编译等能力输出带确凿证据的结构化分析报告，而非凭空猜测伪代码。

官方两个代表性案例：① Notion Desktop 7.6.1 剪贴板逆向——沿页面 API、预加载脚本和进程通信定位主进程调用 Electron 剪贴板接口的位置，解释复制的 HTML 如何通过 ID 关联本地文档块；② DX-Ball 声音算法重构——砖块横向位置影响左右声道偏向，结合原始指令、调用方和数值常量重建 C 函数，3205 组输入与原 x86 函数一致，63 个字节全部复现。

使用方式：`npx rea-agents setup` 一键配置（自动识别本地 Agent、多写 MCP 配置并备份、可选接入 Ghidra/Hopper/IDA），`npx rea-agents doctor` 健康检查，Node 建议 22.19+，支持 macOS 12+/Linux。作者推荐搭配 [[Archify]] 弥补 REA 出图风格不佳的短板：逆向拆解后让 Agent 以 Skill 形式生成交互式 HTML 架构图（`npx skills add tt-a1i/archify --skill archify`），也可做时序图；缺点是配色简约、图形支持较少。最佳实践建议用 GLM-5.3（非 Flash）+ REA，因其 Benchmark 逆向能力更强；REA 的最佳用法是做二开和定制化，"有了 REA 之后，你的所有 App 都被迫开源了"。

## 关联连接
- [[REA]] — 主角工具（24.1 万 Star 的逆向套件）
- [[Archify]] — 配套架构可视化 Skill
- [[MCP协议]] — REA 的接入协议
- [[OpenClaw]] — 爆火增速的对比参照
- [[GLM-5.3]] — 作者推荐的逆向搭配模型
- [[逆向工程]] — 核心概念
- [[ClaudeCode]] — 支持接入的 Coding Agent 之一
