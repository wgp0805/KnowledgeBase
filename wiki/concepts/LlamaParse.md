---
title: "LlamaParse"
type: concept
tags: [LlamaIndex, PDF解析, 文档处理]
sources: [raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 定义
LlamaParse 是 LlamaIndex 生态的商业化 PDF 解析器，专门处理复杂 PDF（表格、图表、多栏布局、公式等），输出 Markdown 格式便于后续切分和向量化。

## 关键信息
- **核心能力**：复杂 PDF 结构化解析，保留表格、图表、多栏、公式等布局信息
- **输出格式**：Markdown，兼容 LlamaIndex 标准切分流程
- **使用方式**：`parser = LlamaParse(result_type="markdown")` → `parser.load_data("./complex_report.pdf")`
- **定位**：LlamaIndex RAG 流程中"数据摄取"环节的关键增强组件

## 关联连接
- [[摘要-langchain-langgraph-llamaindex对比]] — 来源
- [[LlamaIndex]] — 所属框架
- [[VectorStoreIndex]] — 解析后文档的索引目标
- [[RAG]] — 核心应用场景
- [[MinerU]] — 开源替代方案