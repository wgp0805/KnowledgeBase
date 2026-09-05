---
title: "DocumentLoader"
type: concept
tags: [RAG, LangChain, 文档加载]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
Document Loader（文档加载器）是 RAG 知识库构建流水线的第一环，负责从各种来源加载原始文档并统一转换为 Document 对象，是 LangChain 生态提供的组件抽象。

## 关键信息
- **统一接口**：所有加载器实现 BaseLoader 接口，拥有两个通用方法：
  - `load()`：一次性加载所有文档
  - `lazy_load()`：基于流式传输懒加载，适用于大数据集
- **统一输出**：Document 对象包含 `page_content`（文档内容）与 `metadata`（来源、页码等元数据）
- **常见加载器**：
  - TextLoader：加载 txt 文件（社区提供）
  - WebBaseLoader：剥离 HTML/CSS/JS 只保留文本
  - CSVLoader：加载 csv 文件，指定 source_column 作为来源
  - MinerU：PDF 解析（支持 OCR，见 [[MinerU]]）
- **MinerU 选型建议**：扫描件 PDF 设 `ocr=True`；除 PDF 外也支持 HTML/PPT/DOCX/XLSX/图片等，单一加载器理论可满足 90% 企业需求

## 关联连接
- [[RAG]] — 知识库构建第一环
- [[TextSplitter]] — 加载后的下一步处理
- [[LangChain]] — 所属框架
- [[MinerU]] — PDF 解析工具
- [[摘要-langchain-rag构建知识库-理论]] — 来源