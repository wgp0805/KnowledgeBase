---
title: "MemGPT"
type: entity
tags: [AI, Agent, Memory, 研究项目]
sources: [raw/09-archive/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md]
last_updated: 2026-10-13
---

## 定义
MemGPT 是提出"LLM 操作系统式记忆管理"思路的研究项目，核心类比是：**Context Window 类似计算机 RAM，外部存储类似磁盘**，Agent 在两者之间自主管理和交换信息。即 Letta 的前身，Letta 延续并发展了该设计理念。

## 关键信息
- **经典三层结构**：Core Memory（持续存在于上下文的重要信息）/ Recall Memory（可检索的历史对话）/ Archival Memory（更大规模的长期信息存储）
- **核心思路**：让 Agent 通过工具主动读写、换入换出记忆，而不是由外部系统单向注入
- **优点**：灵活，强调 Agent 自主性
- **缺点**：记忆管理质量受 Agent 决策能力影响——Agent 判断错时会把不该留的记忆留下、该取的记忆漏掉

## 关联连接
- [[Letta]] — 延续该设计的开源项目
- [[AgentMemory]] — 上位概念
- [[Token级记忆]] — 存储形态
- [[Mem0]] — 另一条自动化路线
- [[摘要-一文搞懂agent-memory]] — 来源
