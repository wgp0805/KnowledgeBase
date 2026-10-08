---
title: "摘要-claude-code-mcp-unity游戏"
type: source
tags: [来源, 原始文件, ClaudeCode, MCP, Unity, 游戏开发]
sources: [raw/01-articles/2026-10-01-Claude Code + MCP，让一个空文件夹变成了能玩的 Unity 游戏 - 张善友.md]
last_updated: 2026-10-08
---

## 核心摘要
实战记录：用三条命令（unity-mcp-cli create-project / install-plugin / open）搭建 Unity 工程 + AI Game Developer 插件，配合 Claude Code 语音指令全程零手写代码做出可玩的 Unity 物理游戏。核心经验是"上下文省着用"：Skill 每次调用仅约 8 token 按需加载，而 MCP 工具始终挂在 prompt 里开销大得多，建议禁用用不到的 MCP 工具、任务间 `/clear`、批量用 subagent、一个 agent 只做一件事，实测每任务仅占上下文窗口 3%–5%。架构上 Unity-MCP 插件（70+ 工具）与独立的 GameDev-MCP-Server（.NET"传话筒"）分离，后者一份代码同时服务 Unity/Godot/Unreal 三引擎（MCP 客户端 ⇄ server ⇄ SignalR ⇄ 引擎插件），任何支持 MCP 的客户端（Cursor、Gemini、Copilot 等）都能接入，项目 Apache-2.0 开源。

## 关联连接
- [[UnityMCP]] — 文章实操的引擎插件与共享服务器
- [[MCP]] — 底层连接协议
- [[ClaudeCode]] — 驱动开发的 Agent 客户端
