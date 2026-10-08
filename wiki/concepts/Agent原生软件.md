---
title: "Agent原生软件"
type: concept
tags: [Agent, 产品设计, primitives, malleable-software]
sources: [raw/01-articles/2026-10-03-一年前说 PM 会被淘汰，现在 Anthropic 说：人人都得学会当 PM.md]
last_updated: 2026-10-08
---

## 定义
Agent 原生软件（agent-native）：人能做的事 agent 也应该都能做的软件设计取向，其前提是产品内部建有 primitives（基础组件/一层基础设施），让人、agent 与 REST API 共用同一套底层通道；更进一步是 malleable software（可塑软件）——界面本身也能被 agent 改写。

## 关键信息
- **演进时间线（Mike Krieger）**：①AI 放在侧边栏/小窗口（与产品断开）→ ②功能本身由 AI 驱动 → ③agent-native（人能做的 agent 都能做）→ ④可塑软件（界面可被 agent 改写）
- **primitives 检验法**：让产品做一件"人能做但需要想一想"的事，看它是否与 agent 走同一条底层通道——每个入口各走各的，agent 就永远只是后加的访客；做了 20 年的老应用后补这层很难
- **实证**：Anthropic 内部至少四条独立工作线的项目让 Claude 一边盯进展一边生成界面（先给 TPM 再给全团队），日常大量软件由 Claude 构建、维护、迭代
- **新问题**：界面可改写带来数据权限问题——谁可以更新数据，人点击还是 Claude 在后台改，数据来源如何追溯
- **并行实验的底层条件**：chat 与 Cowork 的记忆系统、MCP、文件存储方式曾各不相同，导致新实验像被孤立；需 foundations 团队统一记忆等底层，且这类基础工作要交给不同于创新团队的人做

## 关联连接
- [[摘要-anthropic-人人都得学会当pm]] — 来源
- [[Anthropic]] — 提出与实践方
- [[产品经理角色]] — 与之对位的角色概念
- [[AI Native]] — 相邻的产品设计取向
