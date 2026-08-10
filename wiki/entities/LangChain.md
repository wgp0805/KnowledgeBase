---
title: "LangChain"
type: entity
tags: [AI框架, Python, LLM]
sources: [raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md]
last_updated: 2026-07-06
---

## 定义
Python 生态最流行的 LLM 应用开发框架，提供统一的模型调用、Prompt 管理、Memory 管理和工具调用抽象。LangGraph 和 LangChain4j 都源于此生态。

## 关键信息
- 由 Harrison Chase 创立，是 LLM 应用框架的标杆
- 核心抽象：ChatModel、Prompt Template、Chain、Memory、Tool、Agent
- **LangGraph** 是 LangChain 生态的子项目，专注 Agent 工作流图编排
- **LangChain4j** 受 LangChain 设计理念启发，但充分尊重 Java 工程习惯

### RAG 知识库构建组件的 LangChain 实现
- **DocumentLoader**（文档加载）：TextLoader / WebBaseLoader / CSVLoader / MinerU（见 [[DocumentLoader]]）
- **TextSplitter**（文本切分）：RecursiveCharacterTextSplitter（推荐）/ CharacterTextSplitter / MarkdownHeaderTextSplitter（见 [[TextSplitter]]）
- **Embeddings**（向量化）：OllamaEmbeddings / DashScopeEmbeddings / HuggingFaceEmbeddings / OpenAIEmbeddings（见 [[Embeddings]]）
- **VectorStore**（向量库）：统一接口 add_documents/delete/similarity_search，Chroma/Milvus/内存实现（见 [[VectorStore]]）
- **Retriever**（检索器）：vectorstore.as_retriever() 固化检索参数（见 [[Retriever]]）

## 关联连接
- [[LangGraph]] — LangChain 生态的 Agent 编排框架
- [[LangGraph4j]] — LangGraph 的 Java 移植版
- [[LangChain4j]] — 受 LangChain 启发的 Java LLM 框架
- [[RAG]] — LangChain 核心应用场景
- [[DocumentLoader]] / [[TextSplitter]] / [[Embeddings]] / [[VectorStore]] / [[Retriever]] — RAG 组件抽象
- [[MinerU]] — 推荐的 PDF 加载器
- [[摘要-langchain-rag构建知识库-理论]] — RAG 构建理论来源
- [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]] — 来源

