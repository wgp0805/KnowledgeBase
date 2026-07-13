---
title: "摘要-RAG-KAG双引擎知识库系统"
type: source
tags: [来源, RAG, KAG, 知识库, 微服务]
sources: ["raw/01-articles/推荐一个牛逼的RAG+KAG双引擎系统.md"]
last_updated: 2026-07-13
---

## 核心摘要

本文介绍一个完整的企业智能知识库系统，采用 RAG + KAG 双引擎架构。系统提供 Java（Spring Cloud Alibaba）和 Python（FastAPI + LangChain）两套后端实现，功能完全对等，共享同一套 React 前端。

核心能力包括：文档全生命周期管理、Elasticsearch 混合检索（BM25 + 向量）、RAG/KAG/标准对话三种 AI 模式、Neo4j 知识图谱可视化、企业级 RBAC 权限。项目规模：50,000+ 行代码，10 个微服务模块，近 200 个 API 端点。

## 关联连接
- [[RAG]] — 检索增强生成
- [[KAG]] — 知识增强生成
- [[Neo4j]] — 知识图谱数据库
- [[LangChain4j]] — Java LLM 框架
- [[LangGraph]] — Agent 编排框架
- [[FastAPI]] — Python Web 框架
