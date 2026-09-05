---
title: "KAG"
type: concept
tags: [AI, 知识图谱, RAG增强]
sources: ["raw/09-archive/推荐一个牛逼的RAG+KAG双引擎系统.md"]
last_updated: 2026-07-13
---

## 定义

KAG（Knowledge-Augmented Generation，知识增强生成）是一种结合知识图谱中实体关系来增强 LLM 上下文的技术，弥补纯 RAG 在结构化推理方面的不足。

## 关键信息

- **与 RAG 的区别**：RAG 基于文档内容向量化检索，KAG 基于知识图谱的实体关系遍历
- **核心优势**：结构化推理，发现隐含关联
- **实现方式**：LLM 实体识别 → Neo4j 多跳遍历 → 关联推理
- **适用场景**：需要理解系统间依赖关系、因果链路等复杂关联的问答

## 关联连接
- [[摘要-RAG-KAG双引擎知识库系统]] — 来源
- [[RAG]] — 检索增强生成
- [[Neo4j]] — 知识图谱数据库
- [[GraphRAG]] — 图检索增强生成
