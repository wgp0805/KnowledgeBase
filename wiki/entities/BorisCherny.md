---
title: "BorisCherny"
type: entity
tags: [人物, Anthropic, Claude-Code]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 定义
Anthropic 首席工程师，Claude Code 核心工程师。2025 年 5 月 7 日在 Latent Space 播客上公开阐述 Claude Code 为何放弃 RAG 改用 Agentic Search。

## 关键信息

### 关于 Agentic Search vs RAG 的核心观点
- Claude Code 早期版本确实用过 RAG（使用 Voyage Embedding 模型做本地向量索引）
- 试用 Glob + Grep + Read 后发现全面超越 RAG，原话 "outperformed everything, by a lot"
- 放弃 RAG 的两大原因：
  1. **性能**：Agentic Search 搜索质量更高，grep 返回精确代码行可直接使用，RAG 返回"相关"片段需二次筛选
  2. **简洁**：RAG 需维护索引同步、增量更新、向量数据库生命周期；Agentic Search 无需预处理

### 信息来源
- 2025 年 5 月 7 日 Latent Space 播客，同场嘉宾 Catherine Wu

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[ClaudeCode]] — 主导产品
- [[Anthropic]] — 所属公司
- [[AgenticSearch]] — 力推的搜索范式
- [[RAG]] — 放弃的检索方案
