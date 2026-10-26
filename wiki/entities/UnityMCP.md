---
title: "UnityMCP"
type: entity
tags: [实体, MCP, Unity, 游戏开发, 开源]
sources: [raw/09-archive/2026-10-01-Claude Code + MCP，让一个空文件夹变成了能玩的 Unity 游戏 - 张善友.md]
last_updated: 2026-10-08
---

## 定义
Unity-MCP（AI Game Developer 插件，github.com/IvanMurzak/Unity-MCP）是跑在 Unity Editor 里的 MCP 插件，提供 70+ 工具覆盖场景、资源、脚本、编辑器控制、测试、Profiler；配合独立的 GameDev-MCP-Server（.NET 服务）充当"传话筒"，让任何支持 [[MCP]] 的 AI 客户端（[[ClaudeCode]]、Cursor、Gemini、Copilot 等）用自然语言零代码开发 Unity 游戏。Apache-2.0 开源。

## 关键信息
- **三分钟起步**：`unity-mcp-cli create-project / install-plugin / open` 三条命令建工程装插件；开启 Generate Skills 后开箱生成 57 个命令供 Claude Code 自动发现，扩展包可热装（57→59+）
- **薄服务器设计**：GameDev-MCP-Server 一份代码同时服务 Unity-MCP、Godot-MCP、Unreal-MCP 三个引擎——仓库无引擎特定代码，工具由连上来的引擎插件经 SignalR 动态注册；拓扑：MCP 客户端 ⇄ gamedev-mcp-server ⇄ (SignalR) ⇄ 引擎插件；支持 dotnet tool/源码/Docker/预编译二进制多种启动
- **错误自愈**：Unity 报错（工具调用失败、C# 编译不过）原样详细反馈给 Agent，由其自行定位修复重试（如粉色材质=丢 shader，一句"这材质是粉的"即可修好）
- **并行 Agent 实战**：同一项目目录多开 Claude Code 终端，各管各的上下文，一个做材质、一个铺地板、一个调相机同时进行
- **上下文经验**：Skill 每次调用仅约 8 token 按需加载，MCP 工具始终挂 prompt 开销大——优先 Skills、任务间 `/clear`、关掉用不到的 MCP 工具、批量用 subagent、一个 agent 专注一件事，实测每任务只占上下文 3%–5%

## 关联连接
- [[摘要-claude-code-mcp-unity游戏]] — 来源
- [[MCP]] — 底层协议
- [[ClaudeCode]] — 主要驱动客户端
- [[Skill]] — 低上下文开销的能力暴露方式
