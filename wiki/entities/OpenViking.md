---
title: "OpenViking"
type: entity
tags: [火山引擎, Agent, 知识库, 开源项目]
sources: [raw/01-articles/2026-09-04-OpenViking 实战：把知识库、长期记忆和 Agent 技能统一到一个上下文文件系统.md]
last_updated: 2026-09-05
---

## 定义
OpenViking 是火山引擎开源的面向 AI Agent 的上下文数据库，以虚拟文件系统统一知识库、记忆与技能，通过分层加载优化 Agent 上下文检索。

## 关键信息
- 来源：火山引擎团队
- 三类内容统一：Resources（知识资料）、Memories（用户记忆）、Skills（技能工作流）
- 分层加载：L0摘要层→L1概览层→L2完整正文
- URI：viking:// 统一表示
- 核心价值：保留结构、可观察检索、减少无关内容、多Agent共享记忆
- 支持 Agent：Claude Code、Codex、Cursor、TRAE、OpenCode
- 地址：github.com/volcengine/OpenViking

## 关联连接
- [[摘要-openviking-agent上下文数据库]] — 来源
- [[VolcEngine]] — 火山引擎
- [[上下文分层]] — L0/L1/L2 三层加载
- [[可观察检索]] — 检索过程可追溯
- [[多Agent共享记忆]] — 跨 Agent 记忆共享
- [[传统RAG]] — 传统检索对比
