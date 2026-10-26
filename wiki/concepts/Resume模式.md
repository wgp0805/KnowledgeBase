---
title: "Resume模式"
type: concept
tags:
  - Agent
  - 状态
sources: ["raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 定义
从已保存状态恢复执行的模式（Agent 会话、工作流、终端会话），减少重复上下文开销。

## 增量补充（2026-10-26）
- Agent YOLO 的 R 开关实例：打开后下次启动追加该 Agent 的恢复会话旗标（`-r` / `--resume`），按 Agent 独立、默认关闭、永不自动打开。

## 关联连接
- [[AIAgentsTerminal]]
- [[上下文压缩]]
- [[AgentYOLO]] — R 开关的提供者
- [[摘要-agent-yolo-三端ide面板]] — 来源
