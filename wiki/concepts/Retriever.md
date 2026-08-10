---
title: "Retriever"
type: concept
tags: [RAG, 检索器, 信息检索]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
Retriever（检索器）是一种接口，能根据非结构化查询返回文档，比向量存储更通用——它不需要具备存储能力，只需能够返回文档即可，可向量库构建，也可由其他数据源构建。

## 关键信息
- **输入输出**：接收字符串形式的查询，返回文档对象列表
- **VectorStore 转换**：所有 VectorStore 都有 `as_retriever()` 方法转成检索器，可将调用参数提前固化（如固定 `search_type="similarity"` 和 `search_kwargs={"k": 3}`），简化后期查询
- **调用方式**：`retriever.invoke(query)`
- **注意**：retriever 不返回相似度得分

### 与其他 RAG 组件的关系
```text
DocumentLoader → TextSplitter → Embeddings → VectorStore → Retriever
```

## 关联连接
- [[RAG]] — 在线检索阶段的核心对外接口
- [[VectorStore]] — 检索器的常见构建来源
- [[DocumentLoader]] / [[TextSplitter]] / [[Embeddings]] — 检索器上游组件
- [[LangChain]] — 所属框架
- [[摘要-langchain-rag构建知识库-理论]] — 来源