---
title: "RAG"
type: concept
tags: [AI, RAG, 检索增强, 知识库]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md]
last_updated: 2026-05-19
---

## 定义
Retrieval-Augmented Generation（检索增强生成），把资料切块向量化存入向量库，提问时先检索相关片段再拼入 Prompt 给模型，解决模型无法知道私有/最新知识的问题。

## 关键信息

### LangChain4j RAG 架构
- **DocumentLoader**：从文件/URL/数据库加载原始文档
- **DocumentSplitter**：切块（按段落/句子/token）
- **EmbeddingModel**：文本转向量
- **EmbeddingStore**：向量库（Pinecone/Milvus/PgVector/Elasticsearch）
- **ContentRetriever**：组合以上，对外提供检索

### 两条流水线
1. **Indexing Pipeline（离线）**：原始数据→加载文档→切块→向量化→写入向量库
2. **Retrieval & Generation Pipeline（在线）**：用户问题→向量化→相似度检索→Top-K→拼入 Prompt→LLM→答案
3. 两条流水线共享同一个 Embedding 模型和向量库（一致性是关键）

### 关键实践
- RAG 关键不在框架，而在切分策略（段落完整性、块大小、重叠设置）
- 换向量库的影响往往不如调切分策略大

## 关联连接
- [[LangChain4j]] — RAG 框架实现
- [[ChatMemory]] — 对话记忆
