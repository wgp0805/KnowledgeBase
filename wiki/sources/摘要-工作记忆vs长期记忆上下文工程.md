---
title: "摘要-工作记忆vs长期记忆上下文工程"
type: source
tags: [来源, 原始文件, 上下文工程, 工作记忆, 长期记忆, Context Engineering]
sources: [raw/01-articles/2026-09-19-长对话先收口：用“工作记忆 vs 长期记忆“管理 AI 上下文 - Jessica_留学中.md]
last_updated: 2026-09-20
---

## 核心摘要
大模型本身没有记忆，唯一能"想起来"的是当前窗口里那几万 token 的上下文。文章用"工作记忆/长期记忆"框架重新看长对话管理，提出"长对话先收口、再开新对话"是有理论支撑的方法论——上下文工程（Context Engineering）。相关术语：Context Rot（上下文腐烂，长上下文注意力被稀释、早期约束最先失效）、Lost-in-the-Middle（中间迷失，Liu et al. 2023，模型对长文本中间位置注意力显著弱于首尾）、Agent Memory/Long-term Memory Layer（Mem0、Zep、LangMem 自动收口+按需检索）。收口收三样：决策、关键事实/结论、下一步。实战：在 WorkBuddy 里用 Prompt 收口，记忆分三层（云端档案、用户级 ~/.workbuddy/MEMORY.md、工作区级 项目/.workbuddy/memory/），对应"写—读—沉淀"闭环。

## 关联连接
- [[上下文工程]] — 核心概念
- [[工作记忆]] — 概念
- [[长期记忆]] — 概念
- [[ContextRot]] — 上下文腐烂
- [[Lost-in-the-Middle]] — 中间迷失
- [[Mem0]] — 长期记忆框架
- [[Zep]] — 长期记忆框架
- [[LangMem]] — 长期记忆框架
- [[WorkBuddy]] — 实战工具
- Jessica_留学中 — 作者