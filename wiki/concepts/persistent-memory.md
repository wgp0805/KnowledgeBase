---
title: "persistent-memory"
type: concept
tags: [AI, Agent, 记忆, 架构]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md, raw/01-articles/用好Agent，先从这4招开始！【小白教程】.md]
last_updated: 2026-08-10
---

## 定义
持久记忆（Persistent Memory）是指 AI Agent 在跨会话间保持和利用信息的能力，通过 MEMORY.md / USER.md 等持久化文件或外部记忆提供商存储关键信息，让 Agent 能在不同会话间保持一致的用户画像和上下文。

## 关键信息
- **实现方式**：本地记忆文件（MEMORY.md / USER.md）+ 外部记忆提供商
- **外部提供商**：Honcho、Mem0、Hindsight、Holographic、OpenViking、Byterover、RetainDB、Supermemory
- **与 ChatMemory 区别**：ChatMemory 是会话内记忆，Persistent Memory 是跨会话记忆
- **用户价值**：减少重复交代背景；Agent 主动记录关键决策与偏好，越用越懂你（[[DuMate]] 以此为卖点）

## 关联连接
- [[HermesAgent]] — 内置持久记忆系统的 Agent
- [[DuMate]] — 主打长期记忆的办公 Agent
- [[ChatMemory]] — 会话内对话记忆
- [[摘要-hermes-agent-complete-guide]] — 来源
- [[摘要-用好Agent四招]] — 来源（Agent 四类任务中的记忆支撑）
