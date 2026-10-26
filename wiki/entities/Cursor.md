---
title: "Cursor"
type: entity
tags: [AI编辑器, IDE, 代码搜索, RAG]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了.md, raw/09-archive/2026-09-24-A社O社，坐不住了.md]
last_updated: 2026-09-28
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

### 被 SpaceX 收购与 Grok 联动（2026-09）
SpaceX 收购 Cursor 后，Grok 系列模型保持高频更新：Cursor 手握大量开发者与代码、工具交互的数据可反哺模型训练，最新的 Grok 4.7 在 Artificial Analysis 编程智能体评测中比上一代提高 9 分、已超过 GPT-5.6 Sol。持续更新的模型 + Cursor 已有的开发者用户，让 Grok 具备争夺编程业务的底气。详见 [[摘要-a社o社价格战]]。

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[摘要-a社o社价格战]] — 来源（SpaceX 收购与 Grok 联动）
- [[ClaudeCode]] — 对比产品
- [[RAG]] — 语义检索方案
- [[AgenticSearch]] — 关键词搜索方案
- [[GPT-6]] — Grok 4.7 对标的闭源模型
