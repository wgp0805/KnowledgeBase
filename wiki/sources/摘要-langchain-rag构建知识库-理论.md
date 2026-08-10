---
title: "摘要-langchain-rag构建知识库-理论"
type: source
tags: [RAG, LangChain, 知识库, 向量化]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 核心摘要
本文系统性讲解 LangChain 构建 RAG 知识库的完整理论流程，分为构建与检索两大部分。知识库构建链路为"加载文档 → 切分文本 → 向量化 → 存入向量库"，检索生成为"提问 → 向量化 → 检索文档 → 拼接上下文 → 生成回答"。逐个拆解五大组件：Document Loaders（MinerU 解析 PDF 推荐）、Text Splitters（递归字符切分推荐，参数 chunk_size/chunk_overlap/separators）、Embeddings（Ollama qwen3-embedding 与 DashScope text-embedding-v3 对比）、Vector Store（Chroma 增删查 + 多种检索类型）、Retriever（as_retriever 固化检索参数）。

## 关联连接
- [[RAG]] — 检索增强生成核心概念
- [[LangChain]] — 框架实体
- [[DocumentLoader]] — 文档加载组件
- [[TextSplitter]] — 文本切分组件
- [[Embeddings]] — 向量化组件
- [[VectorStore]] — 向量库组件
- [[Retriever]] — 检索器组件
- [[MinerU]] — PDF 解析工具
- [[Chroma]] — 向量数据库
- [[Ollama]] / [[DashScope]] — Embedding 模型平台
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 相关 RAG 面试解析