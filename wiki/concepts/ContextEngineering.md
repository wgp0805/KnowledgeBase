---
title: "ContextEngineering"
type: concept
tags: [AI, RAG, 上下文, Prompt工程, 检索增强]
sources: [raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md]
last_updated: 2026-06-02
---

## 定义
上下文工程（Context Engineering）是 2025 年 RAG 领域最重要的认知转变——RAG 的本质不是"检索增强生成"，而是"上下文工程"。核心关注点从"怎么检索到相关文档"升级为"怎么为模型构造最合适的上下文"。

## 关键信息

### 认知升级
- **旧视角**：RAG = 检索 + 拼接 + 生成，重点是检索质量
- **新视角**：RAG = 上下文工程，重点是构造最合适的上下文

### 上下文工程的核心关注点
1. **选取**：从大量候选文档中选取最相关的内容
2. **排序**：按重要性排列上下文中的信息
3. **压缩**：去除冗余，精炼上下文长度
4. **冲突处理**：当检索到的文档之间存在矛盾信息时如何处理

### 与 Prompt Engineering 的区别
- Prompt Engineering 关注指令措辞
- Context Engineering 关注给模型"看什么内容"，是更底层的工程问题

### 实践意义
- 单纯优化检索召回率已不够，需要端到端地优化上下文质量
- Rerank、压缩、去重、冲突消解都是上下文工程的子问题

## 关联连接
- [[RAG]] — 基础概念，Context Engineering 是其认知升级
- [[AgenticRAG]] — 同为 RAG 前沿演进方向
- [[GraphRAG]] — 同为 RAG 前沿演进方向
- [[ContextManagement]] — AI 上下文窗口管理策略
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 来源
