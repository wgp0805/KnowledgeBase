---
title: "摘要-opencodereview-workbuddy代码体检"
type: source
tags: [来源, 代码审查, VibeCoding, 阿里]
sources: [raw/01-articles/2026-10-08-阿里开源了个神器，给WorkBuddy、豆包挑毛病.md]
last_updated: 2026-10-09
---

## 核心摘要
阿里开源 Open Code Review（AI 代码质检员，源自集团内部、服务数万开发者），可检查逻辑错误、安全漏洞、性能问题，支持单次修改审查与全项目扫描（`npm install -g @alibaba-group/open-code-review`，`ocr scan` / `ocr scan --preview`）。文章提出 Vibe Coding 的下一机会在"验收"：WorkBuddy 开发 → Open Code Review 检查 → WorkBuddy 修复 → 再检查的闭环流程，并给出可直接复制给 WorkBuddy 的代码检查提示词；Open Code Review 还提供 Delegation Mode，可把审查工作委托给 Qoder、Cursor、Claude Code、Codex 等工具自带模型。观点：AI 解决了"不会开发"，普通人接下来要解决"开发完了怎么验收"；多个 AI 互相检查可能存在共同盲区，支付/隐私类仍需专业测试。

## 关联连接
- [[OpenCodeReview]] — 文章主角
- [[WorkBuddy]] — 配合使用的开发 Agent
- [[Qoder]] — Delegation Mode 支持的工具
- [[ClaudeCode]] — Delegation Mode 支持的工具
- [[Vibe Coding]] — 所讨论的开发范式
- [[代码审查]] — 核心概念
