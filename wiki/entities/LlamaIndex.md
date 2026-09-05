---
title: "LlamaIndex"
type: entity
tags: [AI框架, RAG, 数据框架, Python]
sources: [raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 定义
LlamaIndex（原名 GPT Index）是专门为 RAG（检索增强生成）设计的数据框架，核心使命是把非结构化数据与 LLM 无缝连接。GitHub 44K+ Star，通过 LlamaHub 提供 300+ 数据连接器，覆盖 Notion、Google Drive、Slack、PDF、数据库等数据源。

## 关键信息
- **核心定位**：RAG 领域的天花板，数据摄取和检索能力极强
- **核心抽象**：Index / Query Engine / Retriever / Node / Document
- **开箱即用**：几行代码跑通企业知识库，支持混合搜索、重排序等高级功能
- **LlamaParse**：复杂 PDF 解析器（表格、图表、多栏布局），商业化组件
- **适用场景**：企业内部知识库、财务报告 PDF 解析、混合检索/重排序需求

## 关联连接
- [[摘要-langchain-langgraph-llamaindex对比]] — 三框架对比来源
- [[LangChain]] — 互补框架（基础层）
- [[LangGraph]] — 互补框架（编排层）
- [[RAG]] — 核心解决领域
- [[VectorStoreIndex]] — 核心索引类型
- [[LlamaParse]] — PDF 解析器
- [[苏三]] — 对比文章作者