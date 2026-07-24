---
title: "context-compression"
type: concept
tags: [AI, Agent, 上下文, 优化]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md, raw/01-articles/面试官皱眉："让你负责一个生产级 Agent，你会怎么设计？"，我上来就开始背 ReAct、Function Calling、Skills。面试官听完摇头。.md]
last_updated: 2026-07-24
---

## 定义
上下文压缩（Context Compression）是指自动压缩 LLM 上下文窗口的技术，通过阈值控制、目标压缩比、保护最近消息数等参数，在保留关键信息的同时减少 Token 消耗。

## 关键信息
- **核心参数**：threshold（触发压缩的上下文长度）、target_ratio（目标压缩比例）、protect_last_n（保护最近的 N 条消息）
- **适用场景**：长对话、连续任务执行的上下文管理
- **实现方式**：可通过摘要总结、丢弃低优先级内容等方式实现

### Map-Reduce 分片摘要（PaiCLI 实现）
PaiCLI 采用的上下文压缩策略，分三步：
1. **切片**：把旧消息按每 5 条一组切成若干片段
2. **Map 摘要**：每个片段独立生成一段摘要，保留用户的需求和意图、已执行的操作和结果、做出的决策和结论
3. **Reduce 合并**：多个片段摘要再合并成一份整体摘要

压缩完成后，清空旧消息，把摘要作为一条新记录写回对话历史，再把最近 3 轮完整对话原样补回来。模型看到的是"摘要 + 最近几轮完整对话"。

### 压缩防护三层机制
1. **事实提取**：压缩前从旧对话中提取跨会话稳定事实，存进长期记忆，不参与压缩
2. **摘要指令**：压缩提示词明确要求保留关键信息，单片摘要 ≤ 200 字，合并摘要 ≤ 300 字
3. **近期缓冲**：最近几轮完整对话原样保留，不压缩

## 关联连接
- [[HermesAgent]] — 内置上下文压缩的 Agent 系统
- [[PaiCLI]] — 实现 Map-Reduce 分片摘要的 Agent 项目
- [[ContextManagement]] — AI 上下文窗口管理策略
- [[摘要-hermes-agent-complete-guide]] — 来源
- [[摘要-生产级Agent设计]] — 来源
