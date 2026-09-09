---
title: "Figma"
type: entity
tags: [设计工具, UI设计, MCP]
sources: [raw/09-archive/2026-09-08-小米MiMo Desktop开放邀测：腾讯、阿里、字节又多了一个对手.md]
last_updated: 2026-09-09
---

## 定义
主流的云协作界面设计工具。在小米 MiMo Desktop 的官方工作流中被作为 [[MCP]] 的可控执行目标，用于 AI 直接生成设计元素。

## 关键信息
- MiMo Desktop 的设计链路：自然语言输入 → 理解任务 → 规划工作流 → 调用 MCP 控制 Figma → 实时生成设计元素 → 交付成果
- 该链路表明 MCP 正在成为桌面 Agent 接入第三方工具的通用插头——把外部 SaaS 工具变成 Agent 可操控的执行环境
- 在 Codex 的实测对比中，构建 Figma 插件是 Codex 与 Claude Code 的 Token 效率对照用例之一（Codex 150 万 vs Claude Code 620 万）

## 关联连接
- [[MiMoDesktop]] — 通过 MCP 控制 Figma 的 Agent
- [[MCP]] — 接入 Figma 的通用协议
- [[Codex]] — Token 效率对比中涉及 Figma 插件用例
- [[摘要-小米mimo-desktop邀测]] — 来源
