---
title: "摘要-一文讲透RAG原理优化与落地"
type: source
tags: [RAG, 向量检索, 大模型]
sources: [raw/09-archive/一文讲透 RAG：原理、优化与落地.md, raw/09-archive/一文讲透 RAG：原理、优化与落地（苏三重发版）.md]
last_updated: 2026-10-14
---

## 核心摘要
RAG 就是开卷考试，模型没变，变的是它答题前能不能翻到对的一页。文章从原理到生产一次讲透，涵盖离线四步（文档加载、Chunk分块、Embedding向量化、存入向量库）和在线四步（向量检索召回、Rerank重排、拼进Prompt、LLM生成），以及检索优化（混合检索、Rerank、Agentic RAG）。

## 版本说明
- 原版：楼仔，2026-09-23 发布（[mp.weixin.qq.com/s/_K_PDJMpSUZh2GwWYFQHiA](https://mp.weixin.qq.com/s/_K_PDJMpSUZh2GwWYFQHiA)），2026-09-23 ingest 入库
- 重发版：苏三说技术，2026-10-14 转发（[mp.weixin.qq.com/s/7lZKwQpiAKEFDfDwSL8Sbw](https://mp.weixin.qq.com/s/7lZKwQpiAKEFDfDwSL8Sbw)），仅替换首尾引流文案（RAG+KAG 双引擎系统推广），正文六章与原版完全一致，无新增知识

## 关联连接
- [[RAG]] — 核心概念
- [[向量检索]] — 检索方式
- [[混合检索]] — 检索优化
- [[Rerank]] — 精排方法
- [[AgenticRAG]] — 智能检索
- [[Chunk分块]] — 数据处理
- [[Embedding向量化]] — 数据处理
- [[元数据过滤]] — 检索优化
- [[ContextualRetrieval]] — 检索优化
