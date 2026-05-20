---
title: "Cursor"
type: entity
tags: [AI编辑器, IDE, 代码搜索, RAG]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 定义
AI 驱动的代码编辑器，训练自有 Embedding 模型，采用混合检索（关键词 + 语义搜索）方案。

## 关键信息

### 检索架构
- 训练自有 Embedding 模型
- 使用 Turbopuffer 做向量数据库
- 构建完整的索引管道
- **混合检索**：grep 和向量搜索并用，而非只用向量搜索

### 性能数据
- 超过 1000 文件的大型仓库中，语义搜索使代码留存率提升 2.6%
- A/B 测试确认：加入语义搜索后 Agent 准确率显著提升

### 与 Claude Code 的关键区别
1. **IDE 级产品**：代码仓库相对稳定，索引同步压力小
2. **CLI 级产品**（Claude Code）：用户随时切换仓库，索引同步成本高
3. Cursor 结论是"两者配合效果最好"，grep 仍是不可或缺基础

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[ClaudeCode]] — 对比产品
- [[RAG]] — 语义检索方案
- [[AgenticSearch]] — 关键词搜索方案
