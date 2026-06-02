---
title: "AgenticRAG"
type: concept
tags: [AI, RAG, Agent, 智能体, 检索增强]
sources: [raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md]
last_updated: 2026-06-02
---

## 定义
Agentic RAG（智能体化 RAG）是传统 Naive RAG 的升级范式，引入 Agent 的决策能力，使模型可以自主判断需不需要检索、检索什么、检索结果够不够用、要不要换个策略再搜一遍。从被动检索变成了主动决策。

## 关键信息

### 与 Naive RAG 的对比
- **Naive RAG**：用户问 → 检索 → 生成，单次流程，被动执行
- **Agentic RAG**：模型自主决策是否检索、检索策略、结果评估、多轮迭代

### 核心能力
1. **检索决策**：自主判断是否需要检索外部知识
2. **策略选择**：根据问题类型选择不同检索策略
3. **结果评估**：判断检索结果是否足够回答问题
4. **迭代优化**：结果不够时换个策略再搜

### 应用场景
- 复杂多步推理问答
- 需要跨多个知识源综合的场景
- 对回答准确性要求极高的企业级应用

## 关联连接
- [[RAG]] — 基础概念，Agentic RAG 是其演进方向
- [[Agent]] — Agent 决策能力是核心
- [[AgenticSearch]] — Agent 驱动的搜索范式
- [[ContextEngineering]] — 同为 RAG 前沿演进方向
- [[GraphRAG]] — 同为 RAG 前沿演进方向
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 来源
