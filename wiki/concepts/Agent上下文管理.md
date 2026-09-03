---
title: "Agent上下文管理"
type: concept
tags: [概念, Agent, 上下文, 技术]
sources: [raw/01-articles/2026-09-01-Agent上下文管理概述-1 - Big-Yellow-J.md]
last_updated: 2026-09-01
---

## 定义
Agent在运行过程中对历史、任务状态、记忆等内容进行"选择拼接"，构成完整上下文交给大模型处理的技术方案。

## 关键信息
1. **上下文组织**：
   - 静态提示词：系统提示词、工具介绍等不会改变的内容
   - 动态提示词：用户内容输入等经常改变的内容
   - 架构：静态内容 + 用户消息 + Agent交互轨迹 + 工具结果

2. **上下文压缩**：
   - 自动触发条件：ContextTokens > ContextWindow - ReserveTokens
   - 工业级方案：确定性选择与清理 + 专用LLM生成任务交接摘要 + 原始尾部 + 外部可恢复状态
   - Pi Agent：基于提示词的结构化压缩
   - OpenCode：Tool Result Pruning + Conversation Compaction两层压缩

## 关联连接
- [[摘要-Agent上下文管理概述]] — 来源文章
- [[上下文压缩]] — 关键技术
- [[Tool Result Pruning]] — OpenCode的压缩策略
- [[结构化压缩]] — Pi Agent的压缩策略
- [[KV Cache压缩]] — 模型层压缩技术
