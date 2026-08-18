---
title: "ACP"
type: entity
tags: [实体, 协议, Agent, JetBrains]
sources: [raw/01-articles/IDEA 里跑 Claude Code 和 Codex 的最佳搭子，5.4k Star 开源免费太爽了！.md]
last_updated: 2026-08-18
---

## 定义
ACP（Agent Client Protocol）是 JetBrains 官方支持的 Agent 接入层协议，已成为 IntelliJ IDEA 2026.2 AI Assistant 原生接入 Claude Agent、Codex 等 Agent 的统一通道。

## 关键信息
- **官方定位**：JetBrains 2026.2 官方文档明确列出 Claude Agent、Codex、Skills、MCP、项目上下文和变更回滚支持，ACP 是其中 Agent 接入层
- **能力范围**：官方维护、IDE 集成统一、Agent 注册和团队治理更顺
- **限制**：能力和登录方式受 JetBrains 版本、AI Assistant 与 Provider 支持范围影响
- **对比路线**：与 [[CCGUI]]（社区开源插件）、纯终端构成三条 Agent 使用路线，无绝对胜负，差别在维护责任和操作习惯

## 关联连接
- [[摘要-cc-gui-jetbrains插件]] — 来源资料
- [[JetBrains]] — 协议维护方
- [[IntelliJIDEA]] — 协议宿主 IDE
- [[ClaudeCode]] — 接入的 Agent 之一
- [[Codex]] — 接入的 Agent 之一
- [[CCGUI]] — 社区替代方案
- [[MCP]] — 相关协议
- [[Skills]] — 相关能力封装
