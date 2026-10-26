---
title: "Letta"
type: entity
tags: [AI, Agent, Memory, 开源项目]
sources: [raw/09-archive/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md]
last_updated: 2026-10-13
---

## 定义
Letta（原 MemGPT）是让 Agent 自主管理记忆的开源项目，核心类比是：**Context Window 类似计算机 RAM，外部存储类似磁盘**，Agent 在两者之间自主管理和交换信息。

## 关键信息
- **经典三层结构**：
  - **Core Memory**：持续存在于上下文中的重要信息
  - **Recall Memory**：可检索的历史对话
  - **Archival Memory**：更大规模的长期信息存储
- **核心特点**：让 Agent 参与记忆管理——通过工具读取、修改或维护相关记忆
- **优势**：灵活，强调 Agent 自主性
- **缺点**：记忆管理的质量会受到 Agent 决策能力的影响
- 与 [[Mem0]]（自动化记忆服务）、[[ClaudeCode]]（文件系统记忆）构成三条不同工程路线，不互斥

## 关联连接
- [[AgentMemory]] — 上位概念
- [[Agent记忆三型]] — 记忆分类
- [[MemGPT]] — 前身项目名
- [[Mem0]] — 另一路线
- [[ClaudeCode]] — 文件系统记忆路线
- [[Token级记忆]] — 存储形态
- [[摘要-一文搞懂agent-memory]] — 来源
