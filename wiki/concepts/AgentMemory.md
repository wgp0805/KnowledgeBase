---
title: "AgentMemory"
type: concept
tags: [AI, Agent, 记忆系统, 概念]
sources: [raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md, raw/01-articles/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md]
last_updated: 2026-10-13
---

## 定义
智能体（Agent）的记忆系统，指 Agent 跨轮次、跨会话、跨用户保持与检索信息的能力。生产级 Agent 记忆通常划分为**短期会话记忆**（上下文续接）与**长期用户记忆**（个性化画像）两层，二者独立存储、能力互补。

## 关键信息
- **两层划分**（以 LangGraph 为典型）：
  - 短期会话记忆 → [[Checkpointer]]（如 [[PostgresSaver]]）：自动写入、thread_id 隔离、支持中断恢复
  - 长期用户记忆 → Store（如 [[PostgresStore]]）：手动写入、namespace+key 隔离、跨会话共享
- **常见误区**：混淆「会话运行状态记忆」与「用户业务长期记忆」，导致会话无法续连、用户记忆错乱、多线程数据互通异常
- **语义检索**：长期记忆可配合向量嵌入实现语义相似度匹配（非精准匹配），是个性化应答与知识库智能召回的核心能力，依赖 [[pgvector]]（生产）或 [[InMemoryStore]]（测试）
- **工具化**：记忆操作可封装为 Agent 工具（`@tool`），让智能体自主识别用户意图、读写用户档案、清理记忆，实现闭环
- **长上下文 ≠ 记忆**（2026-08-24 增补）：100 万 Token 上下文解决的是"一次对话里能容纳多少内容"，记忆解决的是"跨会话能记住什么"，是两个不同的问题，超大上下文窗口不能取代 Memory 系统
- **功能分类（2026-10-13 增补，详见 [[摘要-一文搞懂agent-memory]]）**：借鉴认知科学分三类——[[Agent记忆三型]]：情景记忆（发生过什么）、语义记忆（什么是事实）、程序记忆（应该怎么做），三者不互斥
- **存储形态（2026-10-13 增补）**：商业 LLM API 开发者首选 [[Token级记忆]]（外部文本 + 检索后注入 Prompt）；Latent Memory（KV Cache 复用等）需访问模型底层；Parametric Memory（微调/LoRA）不适合频繁更新的配置
- **生命周期（2026-10-13 增补）**：Write（摘要式/提取式/结构化写入）→ Maintain（合并、更新、遗忘）→ Retrieve（BM25 / Embedding / Hybrid / Reranking）。原则是"越相关越准确越好"，不是越多越好
- **与 RAG 的边界**：RAG 从外部知识源检索增强回答，Memory 关注信息如何产生、保存、更新与复用；RAG 可作为 Memory 的检索基础，但 Memory 不止检索
- **Memory ≠ 持续学习**：多数系统实现的是"系统层面经验积累"，模型参数并未更新

## 关联连接
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源
- [[摘要-ox-alpha模型与agent面试题]] — 来源（长上下文 vs Memory 辨析）
- [[LangGraph]] — 典型实现框架
- [[Checkpointer]] — 短期会话记忆概念
- [[PostgresSaver]] — 短期记忆实现
- [[PostgresStore]] — 长期记忆实现
- [[pgvector]] — 语义检索依赖
- [[AgentEngineering]] — 相关工程化概念
- [[摘要-agentmemory开源记忆层]] — 开源记忆层（含跨会话记忆）的落地来源
- [[摘要-一文搞懂agent-memory]] — 来源（记忆分类/存储形态/生命周期）
- [[Agent记忆三型]] — 功能分类
- [[Token级记忆]] — 最实用的存储形态
- [[Mem0]] — 自动化记忆服务路线
- [[Letta]] — Agent 自主管理路线
