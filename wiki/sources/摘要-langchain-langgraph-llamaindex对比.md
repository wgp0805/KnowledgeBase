---
title: "摘要-langchain-langgraph-llamaindex对比"
type: source
tags: [来源, 原始文件, LangChain, LangGraph, LlamaIndex, 框架对比]
sources: [raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 核心摘要
苏三详细对比了 LangChain、LangGraph、LlamaIndex 三大 Python AI 框架的核心定位、架构差异、优缺点及适用场景。核心结论：三者各管一摊、互补不替代——LangChain 是"零件箱"（通用 LLM 应用框架，生态最全 95K+ Star），LangGraph 是"流水线图纸"（有状态 Agent 编排运行时，解决循环推理/条件分支/检查点恢复，15K+ Star），LlamaIndex 是"数据仓库管理员"（专注 RAG 数据框架，300+ 数据连接器 44K+ Star）。最佳实践是组合使用：LlamaIndex 做数据层（摄取/索引/检索），LangGraph 做编排层（状态图/多轮推理/工具调用），LangChain 做基础层（模型调用/工具定义/Prompt 管理）。

## 关联连接
- [[LangChain]] — 通用 LLM 应用框架，零件箱
- [[LangGraph]] — 有状态 Agent 编排运行时，流水线图纸
- [[LlamaIndex]] — RAG 数据框架，数据仓库管理员
- [[苏三]] — 作者，微信公众号「苏三说技术」
- [[StateGraph]] — LangGraph 核心抽象：状态图
- [[检查点机制]] — LangGraph 状态持久化与故障恢复
- [[VectorStoreIndex]] — LlamaIndex 核心抽象：向量存储索引
- [[LlamaParse]] — LlamaIndex 复杂 PDF 解析器
- [[RAG]] — LlamaIndex 核心解决领域
- [[Agent编排]] — LangGraph 核心解决领域