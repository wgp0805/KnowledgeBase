---
title: "MiniMaxCode"
type: entity
tags: [实体, MiniMax, Code CLI, 开源, Agent]
sources: [raw/01-articles/2026-09-19 - MiniMax 版 Claude Code 开源，夯。.md]
last_updated: 2026-09-20
---

## 定义
MiniMax 开源的 Code CLI（v0.4.12，MIT 协议），在 FrontierHarness Eval 上拿到 SOTA 通过率、最快完成时间、第二低 token 消耗。作者用 MiniMax Code CLI + DeepSeek V4.1 Flash 开发魂斗罗录屏，长程任务跑 32 分钟没出问题。

## 关键信息
- **架构**：基于 Pi 开源编码 Agent 框架
  - `agent-core`：定义 Turn 数据结构/工具协议/事件类型
  - `agent-runtime`：提供扩展注册表
  - `agent-extension`：实现内置 Skills/权限/MiniApp
  - `local-runtime-v2`：完整宿主实现（SQLite 持久化）
  - `tui`：终端渲染
- **通信**：界面和运行时通过事件流通信，支持 TUI/无头/ACP 三种入口
- **核心循环**：Turn Loop（每轮状态隔离 + 钩子机制）
- **工具定义**：把 LLM 看到的 schema 和运行时执行代码分开存放
- **扩展系统**：建在工具系统之上，注册表有生命周期状态机

## 关联连接
- [[摘要-minimax-code-cli开源]] — 来源
- [[MiniMax]] — 公司
- [[Pi]] — 底层 Agent 框架
- [[DeepSeek-V4.1-Flash]] — 搭配模型
- [[Turn Loop]] — 核心循环
- [[Hook机制]] — 钩子机制
- [[扩展注册表]] — 扩展系统
- [[PaiCLI]] — 作者要升级的终端 Agent
- [[沉默王二]] — 作者