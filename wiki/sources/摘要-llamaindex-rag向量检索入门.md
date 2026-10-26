---
title: "摘要-llamaindex-rag向量检索入门"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/2026-09-17-基于 LlamaIndex 实现RAG向量检索入门 - lyshark.md]
last_updated: 2026-09-18
---

## 核心摘要
lyshark 撰写的基于 LlamaIndex 实现本地 RAG 向量检索的完整入门教程。使用 llama-server 分别启动 Qwen2.5 对话模型（11433端口）和 Qwen3-Embedding 向量模型（11434端口），通过自定义 LocalLlamaServerEmbedding 类对接本地 Embedding 服务，实现文档加载、分块向量化、索引持久化、语义检索和大模型总结的完整 RAG 流程。支持 VectorStoreIndex 和 SummaryIndex 两种索引模式，提供索引管理器封装创建/加载/查询操作。

## 关联连接
- [[LlamaIndex]] — RAG 框架
- [[RAG]] — 检索增强生成
- Qwen2.5 — 对话模型
- Qwen3-Embedding — 向量模型
- [[向量检索]] — 核心能力
