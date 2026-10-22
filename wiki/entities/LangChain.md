---
title: "LangChain"
type: entity
tags: [AI框架, Python, LLM]
sources: [raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md, raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md, raw/01-articles/为什么越来越多人用Eino？.md]
last_updated: 2026-10-22
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

### Go 生态的对照物：Eino（2026-10-21，详见 [[摘要-为什么越来越多人用eino]]）
Go 微服务团队接 AI 时的现实困境——后端全是 Go，但大模型生态全是 Python，硬接就要在 Go 服务旁再起一个 Python 进程走 HTTP/gRPC，运维复杂度陡增。[[Eino]]（字节 [[CloudWeGo]] 出品）把同一套工程抽象用 Go 重新实现，差异集中在四点：
- **类型安全**：Eino 在 `graph.AddEdge` 时编译期检查上下游类型匹配，LangChain 运行时才报错
- **并发模型**：Goroutine 单机 2000+ 连接 vs Thread/Async 在 200+ 连接时延迟显著
- **内存占用**：启动约 30MB vs 约 200MB
- **编排方式**：显式 Graph 逻辑清晰 vs Chain 模式容易写成面条代码
- 作者的定性：**Eino 不是"把 LangChain 翻译成 Go"，而是用 Go 的工程哲学重新设计 AI 应用框架**——显式优于隐式，类型安全优于运行时灵活，并发原生优于异步模拟

## 关联连接
- [[LangGraph]] — LangChain 生态的 Agent 编排框架
- [[LangGraph4j]] — LangGraph 的 Java 移植版
- [[LangChain4j]] — 受 LangChain 启发的 Java LLM 框架
- [[RAG]] — LangChain 核心应用场景
- [[DocumentLoader]] / [[TextSplitter]] / [[Embeddings]] / [[VectorStore]] / [[Retriever]] — RAG 组件抽象
- [[MinerU]] — 推荐的 PDF 加载器
- [[摘要-langchain-rag构建知识库-理论]] — RAG 构建理论来源
- [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]] — 来源
- [[摘要-langchain-langgraph-llamaindex对比]] — 三框架对比来源
- [[LlamaIndex]] — 互补框架（数据层）
- [[苏三]] — 对比文章作者
- [[Eino]] — Go 生态的对照框架
- [[CloudWeGo]] — Eino 的开源团队
- [[摘要-为什么越来越多人用eino]] — 来源（Eino vs LangChain 对比）

