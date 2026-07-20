---
title: "FAISS"
type: entity
tags: [向量数据库, 相似度搜索, Facebook]
sources: [raw/01-articles/2026-07-19-【RAG扫盲系列·3】从零开始构建你的RAG项目第二弹：API 调用大模型问答 - Alkaid2077.md]
last_updated: 2026-07-20
---

## 定义
FAISS（Facebook AI Similarity Search）是 Facebook AI Research 开源的向量相似度搜索库，用于高效的高维向量最近邻检索。在 RAG 架构中常作为本地向量存储使用，支持 CPU 和 GPU 加速。

## 关键信息
- 在 RAG 流水线中的作用：存储 Embedding 向量，根据查询向量返回最相似的文档片段
- 通过 `langchain_community.vectorstores.FAISS` 集成到 LangChain 生态
- `allow_dangerous_deserialization=True` 仅应在本地可信环境使用

## 关联连接
- [[摘要-rag-api-call]] — RAG API 调用中的向量存储
- [[RAG]] — 检索增强生成架构
- [[LangChain]] — Python LLM 框架集成
